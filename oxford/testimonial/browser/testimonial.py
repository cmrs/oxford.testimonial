from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class TestimonialView(BrowserView):  

    template = ViewPageTemplateFile('templates/testimonial_view.pt')

    def __call__(self):
        return self.template() 
