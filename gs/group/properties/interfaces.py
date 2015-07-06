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
from __future__ import absolute_import, unicode_literals
from zope.interface import Interface
from zope.schema import TextLine, Choice
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from zope.viewlet.interfaces import IViewletManager
from . import GSMessageFactory as _


replyToVocab = SimpleVocabulary([
    SimpleTerm(
        'group', 'group',
        _('reply-to-group', 'Group: replies go to the group.')),
    SimpleTerm(
        'sender', 'sender',
        _('reply-to-sender', 'Author: replies just go to the author of the post.')),
    SimpleTerm(
        'both', 'both',
        _('reply-to-both',
          'Both: replies go to the group, with an extra email to the author.')), ])


class IGroupProperties(Interface):
    title = TextLine(
        title=_('form-label-group-name', 'Group Name'),
        description=_('form-label-group-name-help',
                      'The name of the group'),
        required=True)

    description = TextLine(
        title=_('form-label-description', 'Short Description'),
        description=_('form-label-description-help',
                      'Who and what the online group is for. Shown on the '
                      'Groups page and the Group Home Page.'),
        required=False)

    short_name = TextLine(
        title=_('form-label-subject-line-prefix', 'Subject Line Prefix'),
        description=_('form-label-subject-line-prefix-help',
                      'Shown in the subject line of posts delivered via '
                      'email.'),
        required=True)

    replyTo = Choice(
        title=_('reply-to', 'Reply-to'),
        description=_('This setting determines the behaviour of the Reply-to email header.'),
        vocabulary=replyToVocab,
        required=True,
        default='group')

    mshipCriterion = TextLine(
        title=_('form-label-membership-criterion', 'Membership Criterion'),
        description=_('form-label-membership-criterion-help',
                      "Who is eligible to join the group in the future. "
                      "Displayed only when the group's privacy setting is "
                      '"private" or "secret".'),
        required=False)


class IGroupAdminPropertiesLinks(IViewletManager):
    '''A viewlet manager for the Properties tabs used by the group admin'''
