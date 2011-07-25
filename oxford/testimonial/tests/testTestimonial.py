from Acquisition import aq_inner
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.customerize import registration
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from oxford.testimonial.interfaces.testimonial import ITestimonial

from base import OXFORD_TESTIMONIAL_INTEGRATION_TESTING
from utils import HAMLET_SPEECH

class TestContentType(unittest.TestCase):
    """Ensure product is properly installed"""
    layer =  OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('TestimonialFolder', 'tf1')
        tf1 = getattr(self.portal, 'tf1')
        tf1.invokeFactory('Testimonial', 't1')
        assert 't1' in tf1.objectIds()

    def testDescriptionField(self):
        self.testAddType()
        tf1 = getattr(self.portal, 'tf1')
        t1 = getattr(tf1, 't1')
        t1.setText('Some sample text')
        assert t1.Description() == 'Some sample text', t1.Description()

class TestView(unittest.TestCase):
    """Test the view for testimonial content type"""
    layer = OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('TestimonialFolder', 'tf1')
        self.tf1 = getattr(self.portal, 'tf1')

    def testGetAcademicsReturnsNone(self):
        """Should return empty list if no academics
        """
        tf1 = self.tf1
        view = getMultiAdapter((aq_inner(tf1), self.portal.REQUEST), name='testimonial_list')
        view = view.__of__(tf1)
        assert view.getTestimonials() == []

    def testGetAcademicsReturnNone(self):
        """Should return list of one item
        """
        tf1 = self.tf1
        tf1.invokeFactory('Testimonial', 't1')
        view = getMultiAdapter((aq_inner(tf1), self.portal.REQUEST), name='testimonial_list')
        view = view.__of__(tf1)
        testimonials = view.getTestimonials()
        assert len(testimonials) == 1

class TestView(unittest.TestCase):
    """Test the view for testimonial content type"""
    layer = OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('TestimonialFolder', 'tf1')
        self.tf1 = getattr(self.portal, 'tf1')
        self.tf1.invokeFactory('Testimonial', 't1')
        self.t1 = getattr(self.tf1, 't1')

    def testShortenText(self):
        """Text should split on a space after 350 chars
        """
        t1 = self.t1
        t1.setText(HAMLET_SPEECH)
        # the rich field inserts html
        start_text = "<p>To be, or not to be: that is the question:<br />"
        end_text = "<br />That flesh is"
        assert t1.getTestimonial()[:51] == start_text
        assert t1.getTestimonial()[-19:] == end_text
