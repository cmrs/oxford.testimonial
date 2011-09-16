from AccessControl import ClassSecurityInfo
from zope.interface import implements

from plone.app.folder.folder import ATFolder

from Products.Archetypes.atapi import registerType

from oxford.testimonial.config import PROJECTNAME
from oxford.testimonial.interfaces.testimonialfolder import ITestimonialFolder

from schemata import TestimonialFolderSchema

class TestimonialFolder(ATFolder):
    """Testimonial Folder"""

    security = ClassSecurityInfo()

    implements(ITestimonialFolder)

    meta_type = 'TestimonialFolder'
    _at_rename_after_creation = True

    schema = TestimonialFolderSchema

    security.declarePublic('canSetConstrainTypes')
    def canSetConstrainTypes(self):
        return False

    security.declarePublic('getSectionFolder')
    def getSectionFolder(self):
        return self

registerType(TestimonialFolder, PROJECTNAME)
