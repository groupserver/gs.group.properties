# coding=utf-8
from zope.interface import Interface
from zope.schema import TextLine

class IGroupProperties(Interface):
    title = TextLine(title=u'Group Name',
        description=u'The name of the group',
        required=True)
    description = TextLine(title=u'Short Description',
        description=u'Who and what the group is for',
        required=True)
    short_name = TextLine(title=u'Subject Line Prefix',
        description=u'Shown in the subject line of all group '\
          u'emails',
        required=True)
    mshipCriterion = TextLine(title=u'Membership Criterion (displayed '\
          u'only when the group\'s privacy setting is "private" or '\
          u'"secret")',
        description=u'Who is eligible to join the group',
        required=True)
    