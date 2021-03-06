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

    security.declareProtected(permissions.View, 'tag')
    def tag(self, **kwargs):
        """Generate image tag using the api of the ImageField
        """
        if 'title' not in kwargs:
            kwargs['title'] = self.getStudentName()
        if 'scale' not in kwargs:
            kwargs['scale'] = 'thumb'
        return self.getField('testimionialImage').tag(self, **kwargs)

    security.declareProtected(permissions.View, 'getTestimonial')
    def getTestimonial(self, **kwargs):
        """Shorten the text if too long
        """
        # not used because spaces can be in html tags
        # there also would not a be a close p tag
        # method needs to be made html aware which is not easy
        text = self.getText()
        if len(text) < 350:
            return text
        position = 0
        for char in text:
            if char == ' ':
                if position > 350:
                    return text[:position]
            position += 1

registerType(Testimonial, PROJECTNAME)
