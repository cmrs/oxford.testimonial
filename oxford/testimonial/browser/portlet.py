from Acquisition import aq_inner
from random import choice
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.memoize.instance import memoize
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone import PloneMessageFactory as _

from oxford.testimonial.interfaces import ITestimonialPortlet

class Assignment(base.Assignment):
    implements(ITestimonialPortlet)

    def __init__(self, interval=10):
        self.interval = interval

    @property
    def title(self):
        return _(u"Testimonial Carousel")

class AddForm(base.AddForm):
    form_fields = form.Fields(ITestimonialPortlet)
    label = _(u"Add Testimonial Carousel Portlet")
    description = _(u"This portlet displays testimonials in a carousel.")

    def create(self, data):
        return Assignment(interval=data.get('interval', 5))

class EditForm(base.EditForm):
    form_fields = form.Fields(ITestimonialPortlet)
    label = _(u"Add Testimonial Carousel Portlet")
    description = _(u"This portlet displays testimonials in a carousel.")

class Renderer(base.Renderer):
    _template = ViewPageTemplateFile('portlet.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

        context = aq_inner(self.context)
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        self.anonymous = portal_state.anonymous()  # whether or not the current user is Anonymous
        self.portal_url = portal_state.portal_url()  # the URL of the portal object
        
        # a list of portal types considered "end user" types
        self.typesToShow = portal_state.friendly_types()  

        plone_tools = getMultiAdapter((context, self.request), name=u'plone_tools')
        self.catalog = plone_tools.catalog()

    def render(self):
        return self._template()

    def getRandomTestimonial(self):
        """Returns a random testimonial object"""
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        folder = portal_catalog(portal_type='TestimonialFolder')
        if not folder:
            return
        folder = folder[0].getObject()
        testimonials = folder.getFolderContents({'portal_type':'Testimonial',})
        if not testimonials:
            return
        random_testimonial = choice(testimonials).getObject()
        return random_testimonial
