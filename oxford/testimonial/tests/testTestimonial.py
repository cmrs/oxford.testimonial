import unittest2 as unittest

from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

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
        tf1.invokeFactory('Testimonial', 't1')
        assert 't1' in tf1.objectIds()
