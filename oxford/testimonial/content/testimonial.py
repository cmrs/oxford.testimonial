from AccessControl import ClassSecurityInfo
from zope.interface import implements

from Products.Archetypes.atapi import registerType
from Products.ATContentTypes.content.newsitem import ATNewsItem
from Products.CMFCore import permissions
from Products.CMFCore.utils import getToolByName

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

    security.declareProtected(permissions.View, 'Description')
    def Description(self):
        """Return description based on the testimonial text"""
        description = self.getText()
        if not description:
            return ''
        tansform_tool = getToolByName(self, 'portal_transforms')
        description = tansform_tool.convert('html_to_text', description).getData()
        description = description.strip()
        if len(description) > 150:
            description = description[:150] + '...'
        return description

registerType(Testimonial, PROJECTNAME)
