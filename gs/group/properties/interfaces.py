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
from zope.interface import Interface
from zope.schema import TextLine
from zope.viewlet.interfaces import IViewletManager
from . import GSMessageFactory as _


class IGroupProperties(Interface):
    title = TextLine(
        title=_('Group Name'),
        description=_('The name of the group'),
        required=True)

    description = TextLine(
        title=_('Short Description'),
        description=_('Who and what the online group is for. Shown on the '
                      'Groups page and the Group Home Page.'),
        required=False)

    short_name = TextLine(
        title=_('Subject Line Prefix'),
        description=_('Shown in the subject line of posts delivered via '
                      'email.'),
        required=True)

    mshipCriterion = TextLine(
        title=_('Membership Criterion ? '
                'displayed only when the group\'s privacy setting '
                'is "private" or "secret".'),
        description=_('Who is eligible to join the group in '
                      'the future?'),
        required=False)


class IGroupAdminPropertiesLinks(IViewletManager):
    '''A viewlet manager for the Properties tabs used by the group admin'''
