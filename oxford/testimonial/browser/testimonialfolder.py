from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class TestimonialFolderView(BrowserView):  

    template = ViewPageTemplateFile('templates/testimonial_list.pt')

    def __call__(self):
        return self.template() 

    def getTestimonials(self):
        """Return the testimonials as objects
        """
        academics = self.context.getFolderContents(contentFilter={'portal_type':'Testimonial',},
                                                   full_objects=True)
        return academics
