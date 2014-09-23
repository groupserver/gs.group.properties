# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2013, 2014 OnlineGroups.net and Contributors.
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
from __future__ import absolute_import, unicode_literals
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form.base import disabled_text_widget
from gs.content.form.base.utils import enforce_schema
from gs.group.privacy import GroupVisibility
from gs.group.base import GroupForm
from .interfaces import IGroupProperties


class ChangePropertiesForm(GroupForm):
    pageTemplateFileName = 'browser/templates/changeproperties.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        enforce_schema(self.context, IGroupProperties)
        self.groupVisibility = GroupVisibility(self.groupInfo)
        self.label = 'Change group properties'

    @Lazy
    def form_fields(self):
        retval = form.Fields(IGroupProperties, render_context=True)
        if self.groupVisibility.isPublic:
            retval['mshipCriterion'].custom_widget = disabled_text_widget
        return retval

    def setUpWidgets(self, ignore_request=False):
        self.widgets = form.setUpWidgets(
            self.form_fields, self.prefix, self.context,
            self.request, form=self,
            ignore_request=ignore_request)
        if self.groupVisibility.isPublic:
            self.widgets['mshipCriterion'].required = False

    @form.action(label='Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)
        # TODO: https://projects.iopen.net/groupserver/ticket/640
        s = 'Changed the properties of <a href="{0}">{1}</a>.'
        self.status = s.format(self.groupInfo.relative_url(),
                               self.groupInfo.name)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = '<p>There is an error:</p>'
        else:
            self.status = '<p>There are errors:</p>'
