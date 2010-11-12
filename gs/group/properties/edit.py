# coding=utf-8
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base.form import GroupForm
from interfaces import IGroupProperties

class EditPropertiesForm(GroupForm):
    pageTemplateFileName = 'browser/templates/editproperties.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    
    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        self.form_fields = form.Fields(IGroupProperties)
        self.label = u'Change Group Properties'
        
    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_change(self, action, data):
        self.status = u'Something changed!'

    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'
            