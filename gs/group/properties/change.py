# -*- coding: utf-8 -*-
from zope.cachedescriptors.property import Lazy
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.content.form import disabled_text_widget
from gs.content.form.utils import enforce_schema
from gs.group.privacy.visibility import GroupVisibility
from gs.group.base.form import GroupForm
from interfaces import IGroupProperties


class ChangePropertiesForm(GroupForm):
    pageTemplateFileName = 'browser/templates/changeproperties.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)

    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        enforce_schema(self.context, IGroupProperties)
        self.groupVisibility = GroupVisibility(self.groupInfo)
        self.label = u'Change Group Properties'

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

    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)
        # TODO: https://projects.iopen.net/groupserver/ticket/640
        self.status = u'Changed the properties of '\
          u'<a href="%s">%s</a>.' %\
           (self.groupInfo.relative_url(), self.groupInfo.name)

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
