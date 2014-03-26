# -*- coding: utf-8 -*-
##############################################################################
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
##############################################################################
from __future__ import unicode_literals
from zope.interface import Interface
from zope.schema import TextLine
from zope.viewlet.interfaces import IViewletManager


class IGroupProperties(Interface):
    title = TextLine(title='Group Name',
        description='The name of the group',
        required=True)

    description = TextLine(title='Short Description',
        description='Who and what the online group is for. '
            'Shown on the Groups page and the Group Home Page.',
        required=False)

    short_name = TextLine(title='Subject Line Prefix',
        description='Shown in the subject line of posts delivered via email.',
        required=True)

    mshipCriterion = TextLine(title='Membership Criterion — '
              'displayed only when the group\'s privacy setting '
              'is "private" or "secret".',
        description='Who is eligible to join the group in '
              'the future?',
        required=False)


class IGroupAdminPropertiesLinks(IViewletManager):
    '''A viewlet manager for the Properties tabs used by the group admin'''
