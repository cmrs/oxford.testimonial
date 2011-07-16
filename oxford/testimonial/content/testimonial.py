from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.content.item import Item

from Products.Archetypes.atapi import registerType

from oxford.testimonial.config import PROJECTNAME
from oxford.testimonial.interfaces.testimonial import ITestimonial

from schemata import TestimonialSchema

class Testimonial(Item):
    """Testimonial"""

    security = ClassSecurityInfo()

    implements(ITestimonial)

    meta_type = 'Testimonial'
    _at_rename_after_creation = True

    schema = TestimonialSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

registerType(Testimonial, PROJECTNAME)
