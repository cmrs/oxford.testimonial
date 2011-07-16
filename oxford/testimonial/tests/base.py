from plone.app.testing import PloneSandboxLayer
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting

from plone.testing import z2

class TestCase(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import oxford.testimonial
        self.loadZCML(package=oxford.testimonial)

        # Install product and call its initialize() function
        z2.installProduct(app, 'oxford.testimonial')

        # Note: you can skip this if my.product is not a Zope 2-style
        # product, i.e. it is not in the Products.* namespace and it
        # does not have a <five:registerPackage /> directive in its
        # configure.zcml.

    def setUpPloneSite(self, portal):
        # Install into Plone site using portal_setup
        self.applyProfile(portal, 'oxford.testimonial:default')

    def tearDownZope(self, app):
        # Uninstall product
        z2.uninstallProduct(app, 'oxford.testimonial')

        # Note: Again, you can skip this if my.product is not a Zope 2-
        # style product

OXFORD_TESTIMONIAL_FIXTURE = TestCase()
OXFORD_TESTIMONIAL_INTEGRATION_TESTING = IntegrationTesting(bases=(OXFORD_TESTIMONIAL_FIXTURE,), name="OxfordTestimonial:Integration")
