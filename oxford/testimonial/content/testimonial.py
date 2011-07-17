from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.newsitem import ATNewsItem

from oxford.testimonial.config import PROJECTNAME
from oxford.testimonial.interfaces.testimonial import ITestimonial

from schemata import TestimonialSchema

class Testimonial(ATNewsItem):
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
