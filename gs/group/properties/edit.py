# coding=utf-8
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile
from gs.group.base.form import GroupForm
from gs.content.form.utils import enforce_schema
from interfaces import IGroupProperties

class EditPropertiesForm(GroupForm):
    pageTemplateFileName = 'browser/templates/editproperties.pt'
    template = ZopeTwoPageTemplateFile(pageTemplateFileName)
    
    def __init__(self, context, request):
        GroupForm.__init__(self, context, request)
        enforce_schema(self.context, IGroupProperties)
        self.form_fields = form.Fields(IGroupProperties, render_context=True)
        self.label = u'Edit Group Properties'
        
    @form.action(label=u'Change', failure='handle_change_action_failure')
    def handle_invite(self, action, data):
        form.applyChanges(self.context, self.form_fields, data)
        
        #auditor = Auditor(self.siteInfo, self.groupInfo)
        #admin = createObject('groupserver.LoggedInUser', self.context)
        #auditor.info(CHANGE_ABOUT, admin, '%d' % len(data['aboutText']))
        
        self.status = u'Changed the properties for for '\
          u'<a href="%s">%s</a> has been changed.' %\
          (self.groupInfo.relative_url(), self.groupInfo.name)
          
    def handle_change_action_failure(self, action, data, errors):
        if len(errors) == 1:
            self.status = u'<p>There is an error:</p>'
        else:
            self.status = u'<p>There are errors:</p>'

