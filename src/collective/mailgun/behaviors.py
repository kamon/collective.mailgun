# -*- coding: utf-8 -*-
from zope.interface import alsoProvides, implements
from zope.component import adapts
from zope import schema
from plone.supermodel import model
from plone.dexterity.interfaces import IDexterityContent
from plone.autoform.interfaces import IFormFieldProvider
from plone.app.textfield import RichText as RichTextField

from zope.component import adapts, getMultiAdapter, getUtility

from collective.mailgun import MessageFactory as _



class IMailMessageText(model.Schema):

    text = RichTextField(
        title=_(u'Mail Message Text', default=u'Mail Message Text'),
        description=u"Mail Message Text for edition before sending",
        required=False,
    )

alsoProvides(IMailMessageText, IFormFieldProvider)


class MailMessageText(object):
    implements(IMailMessageText)
    adapts(IDexterityContent)

    def __init__(self, context):
        self.context = context


