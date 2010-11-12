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
        self.form_fields = form.Fields(IGroupProperties, render_context=True)
        self.label = u'Edit Group Properties'
        