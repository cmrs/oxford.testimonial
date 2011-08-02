import time
import unittest2 as unittest
from zExceptions import BadRequest

from zope.component import getSiteManager

from plone.app.testing import PLONE_INTEGRATION_TESTING
from plone.app.testing import ploneSite
from plone.app.testing import applyProfile
from plone.browserlayer.utils import registered_layers

from Products.CMFCore.utils import getToolByName

from base import OXFORD_TESTIMONIAL_INTEGRATION_TESTING

class TestInstallation(unittest.TestCase):
    """Ensure product is properly installed"""
    layer =  OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testTypesInstalled(self):
        portal_types = getToolByName(self.portal, 'portal_types')
        assert 'TestimonialFolder' in portal_types.objectIds(), portal_types.objectIds()
        assert 'Testimonial' in portal_types.objectIds(), portal_types.objectIds()

    def testPortalFactorySetup(self):
        assert 'Testimonial' in self.portal.portal_factory.getFactoryTypes()
        assert 'TestimonialFolder' in self.portal.portal_factory.getFactoryTypes()

class TestReinstall(unittest.TestCase):
    """Ensure product can be reinstalled safely"""
    layer = OXFORD_TESTIMONIAL_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def testReinstall(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')
        try:
            portal_setup.runAllImportStepsFromProfile('profile-oxford.testimonial:default')
        except BadRequest:
            # if tests run too fast, duplicate profile import id makes test fail
            time.sleep(0.5)
            portal_setup.runAllImportStepsFromProfile('profile-oxford.testimonial:default')
