from Acquisition import aq_inner
import unittest2 as unittest
from zope.component import getMultiAdapter

from plone.app.customerize import registration
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from oxford.testimonial.interfaces.testimonialfolder import ITestimonialFolder

from base import OXFORD_TESTIMONIAL_INTEGRATION_TESTING

class TestContentType(unittest.TestCase):
    """Ensure product is properly installed"""
    layer =  OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testAddType(self):
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('TestimonialFolder', 'tf1')
        tf1 = getattr(self.portal, 'tf1')
        assert 'tf1' in self.portal.objectIds()

class TestView(unittest.TestCase):
    """Test the view for testimonial content type"""
    layer = OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('TestimonialFolder', 'tf1')
        self.tf1 = getattr(self.portal, 'tf1')

    def testView(self):
        """Basic test for the view
        """
        tf1 = self.tf1
        tf1.invokeFactory('Testimonial', 't1')
        t1 = getattr(tf1, 't1')
        view = getMultiAdapter((aq_inner(t1), self.portal.REQUEST), name='testimonial_view')
        view = view.__of__(t1)
