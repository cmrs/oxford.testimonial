from zope.schema import Int

from plone.portlets.interfaces import IPortletDataProvider

from Products.CMFPlone import PloneMessageFactory as _

class ITestimonialPortlet(IPortletDataProvider):

    interval = Int(title=_(u'Change Interval'),
                       description=_(u'Number of seconds between testimonial changes.'),
                       required=True,
                       default=10)
