from django.views.generic import TemplateView,ListView
from personal_info.models import ContactInfo
from education.models import EducationInfo
from experience.models import Experience
from project.models import Project,Certification
from skills.models import TechSkill
from summary.models import Summary
from django.shortcuts import get_object_or_404
from itertools import chain
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

class ReportList(TemplateView):
    template_name = 'detail_list.html'
    
    
    