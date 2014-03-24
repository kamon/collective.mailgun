# -*- coding: utf-8 -*-

#import requests

from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName

from mailgun import MailgunAPI
from mailgun.mailinglist import MailingList

# TODO: Conditional import so we can use the richtext behavior from Plone 5
#from plone.app.contenttypes.behaviors.richtext import IRichText

from collective.mailgun.interfaces import IMailingSettings


# Utility function

def email_message(api_key, domain, address, from_email, subject, text):
    mapi = MailgunAPI(api_key, domain)
    mailinglist = MailingList(mapi, address)  
        
    mailinglist.email(subject=subject, 
                      body=text, 
                      from_email=from_email)



## Default implementation of a "Send content to a mailing list" view 

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

        header = settings.mailing_message_header
        footer = settings.mailing_message_footer
        
        subject = context.Title()
        text = self.prepareText()
        if header:
            text = header + text
        if footer:
            text = text + footer

        if request.has_key('preview'):
            return text
        
        email_message(api_key, domain, address, from_email, subject, text)
        
        #return self.index()
        return 1


    def prepareText(self):
        """"""
        context = self.context
        request = self.request

        # Get the text from the content object if Dexterity Document.
        text = '<h1>%s</h1>' % context.Title()
        #if IRichText.providedBy(context):
        #    text = text + context.text.output
        text = text + context.text.output  # Should only work with Documents for now.
        
        return text
        