# -*- coding: utf-8 -*-
from zope.interface import Interface
from zope import schema
from collective.mailgun import MessageFactory as _


class ICollectiveMailgunLayer(Interface):
    """Marker interface that defines a ZTK browser layer. We can reference
    this in the 'layer' attribute of ZCML <browser:* /> directives to ensure
    the relevant registration only takes effect when this theme is installed.

    The browser layer is installed via the browserlayer.xml GenericSetup
    import step.
    """


# Mailing settings interface
class IMailingSettings(Interface):
    """Mailing settings"""

    # Done while testing MailGun
    
    mailing_api_key = schema.Text(
        title=_(u"mailing_api_key"),
        default=u'',
        )

    mailing_domain = schema.Text(
        title=_(u"mailing_domain"),
        default=u'example.com',
        )

    mailing_address = schema.Text(
        title=_(u"mailing_address"),
        default=u'',
        )

    mailing_from_email = schema.Text(
        title=_(u"mailing_from_email"),
        default=u'',
        )

    mailing_message_header = schema.Text(
        title=_(u"mailing_message_header"),
        default=u'',
        )

    mailing_message_footer = schema.Text(
        title=_(u"mailing_message_footer"),
        default=u'',
        )
