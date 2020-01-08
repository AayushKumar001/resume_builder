from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'resume_index.html'


class ThanksPageView(TemplateView):
    template_name = 'thanks.html'


class TestView(TemplateView):
    template_name = 'test.html'

class AboutView(TemplateView):
    template_name = 'resume_about.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Resume Builder application can be used to build Resumes'
        return context