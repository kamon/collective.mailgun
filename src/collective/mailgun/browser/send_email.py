# -*- coding: utf-8 -*-

#import requests

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from mailgun import MailgunAPI
from mailgun.mailinglist import MailingList

from collective.mailgun.interfaces import IMailingSettings


# Utility function

def email_message(api_key, domain, address, from_email, subject, text):
    mapi = MailgunAPI(api_key, domain)
    mailinglist = MailingList(mapi, address)  
        
    mailinglist.email(subject=subject, 
                      body=text, 
                      from_email=from_email)



TEXT_TEMPLATE = """<h1>Message from the site</h1>

<p>
%s
</p>

<p>Footer text</p>
"""

            
class SendEmailView(BrowserView):

    #index = ViewPageTemplateFile('templates/xxxxx.pt')

    def __call__(self):
        """"""
        context = self.context
        request = self.request

        # Get settings values via portal_registry
        registry = getUtility(IRegistry)
        settings = registry.forInterface(IMailingSettings)
        api_key = settings.mailing_api_key
        domain = settings.mailing_domain
        address = settings.mailing_address
        from_email = settings.mailing_from_email
        
        subject = context.Title()
        text = self.prepareText()

        if request.has_key('preview'):
            return text
        
        email_message(api_key, domain, address, from_email, subject, text)
        
        #return self.index()
        return 1


    def prepareText(self):
        """"""
        context = self.context
        request = self.request

        # TODO: Adapt content type and extract the text... (using plone.api ?)
        #       Start with documents...
        text = TEXT_TEMPLATE % context.Title()
        return text
        