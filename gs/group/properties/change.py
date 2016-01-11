# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014, 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from zope.cachedescriptors.property import Lazy
from zope.component import createObject
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import disabled_text_widget, radio_widget
from gs.content.form.base.utils import enforce_schema
from gs.group.privacy import GroupVisibility
from gs.group.base import GroupForm
from .interfaces import IGroupProperties
from . import GSMessageFactory as _


class ChangePropertiesForm(GroupForm):
    pageTemplateFileName = 'browser/templates/changeproperties.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        enforce_schema(self.context, IGroupProperties)
        self.groupVisibility = GroupVisibility(self.groupInfo)
        self.label = _('change-properties-page-title',
                       'Change group properties')

    @Lazy
    def mailingList(self):
        retval = createObject('groupserver.MailingListInfo',
                              self.context, self.groupInfo.id)
        return retval

    @staticmethod
    def check_replyTo(v):
        if v not in ('group', 'sender', 'both'):
            raise ValueError('Reply-to can be "group", "sender", or '
                             '"both", not "{0}"'.format(v))

    @Lazy
    def defaultReplyTo(self):
        'The default reply-to, from the ListManager object'
        listManager = self.mailingList.mlist.ListManager
        retval = listManager.getProperty(b'replyto', 'group')
        return retval

    @property
    def replyTo(self):
        'The reply-to property for a group'
        # --=mpj17=-- All this replyTo property stuff is great,
        # but it really needs to be moved to gs.group.list.base
        # at some stage.
        r = self.mailingList.get_property(b'replyto', self.defaultReplyTo)
        retval = 'group' if r is None else r
        retval = 'group' if retval == 'list' else retval  # For old GS installs
        self.check_replyTo(retval)
        return retval

    @replyTo.setter
    def replyTo(self, val):
        self.check_replyTo(val)
        # --=mpj17=-- Aquisition has a bad rep because of things like this aq_explicit
        if hasattr(self.mailingList.mlist.aq_explicit, b'replyto'):
            self.mailingList.mlist.manage_changeProperties(replyto=val)
        else:
            self.mailingList.mlist.manage_addProperty(b'replyto', val, b'string')

    @Lazy
    def form_fields(self):
        retval = form.Fields(IGroupProperties, render_context=True)
        if self.groupVisibility.isPublic:
            retval['mshipCriterion'].custom_widget = disabled_text_widget
        retval['replyTo'].custom_widget = radio_widget
        return retval

    def setUpWidgets(self, ignore_request=False):
        data = {}
        data['replyTo'] = self.replyTo

        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self, data=data,
            ignore_request=ignore_request)
        if self.groupVisibility.isPublic:
            self.widgets['mshipCriterion'].required = False

    @form.action(name='change', label=_('change-button', 'Change'),
                 failure='handle_change_action_failure')
    def handle_change(self, action, data):

        if data['replyTo'] != self.replyTo:
            self.replyTo = data['replyTo']
            del(data['replyTo'])

        form.applyChanges(self.context, self.form_fields, data)
        self.set_subject_prefix(data['short_name'])
        groupLink = '<a href="{groupUrl}">{groupName}</a>.'.format(
            groupUrl=self.groupInfo.relative_url(),
            groupName=self.groupInfo.name)
        self.status = _('changed-status',
                        'Changed the properties of ${groupLink}.',
                        mapping={'groupLink': groupLink})

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            s = 'There is an error:'
        else:
            s = 'There are errors:'
        self.status = '<p>{0}</p>'.format(s)

    def set_subject_prefix(self, prefix):
        '''Set the subject-line prefix by setting the title of the
        mailing list'''
        # Closes https://projects.iopen.net/groupserver/ticket/640
        self.mailingList.mlist.manage_changeProperties(title=prefix)
