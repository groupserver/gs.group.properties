# coding=utf-8
from zope.interface import Interface
from zope.schema import TextLine

class IGroupProperties(Interface):
    groupName = TextLine(title=u'Group Name',
        description=u'The name of the group.',
        required=True)
    description = TextLine(title=u'Description',
        description=u'A description of the group.',
        required=True)
    subjectPrefix = TextLine(title=u'Subject Prefix',
        description=u'A short identifier to be prepended '\
          u'to the subject line of all group emails, '\
          u'within square brackets',
        required=True)
    mshipCriterion = TextLine(title=u'Membership Criterion',
        description=u'A short identifier to be prepended '\
          u'to the subject line of all group emails, '\
          u'within square brackets',
        required=False)
    