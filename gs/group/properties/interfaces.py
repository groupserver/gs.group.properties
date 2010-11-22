# coding=utf-8
from zope.interface import Interface
from zope.schema import TextLine

class IGroupProperties(Interface):
    title = TextLine(title=u'Group Name',
        description=u'The name of the group',
        required=True)
    description = TextLine(title=u'Short Description',
        description=u'Who and what the online group is for. '\
          u'Shown on the Groups page and the Group Home Page.',
        required=True)
    short_name = TextLine(title=u'Subject Line Prefix',
        description=u'Shown in the subject line of posts '\
          u'delivered via email.',
        required=True)
    mshipCriterion = TextLine(title=u'Membership Criterion — '\
          u'displayed only when the group\'s privacy setting '\
          u'is "private" or "secret".',
        description=u'Who is eligible to join the group in '\
          u'the future?',
        required=True)
    