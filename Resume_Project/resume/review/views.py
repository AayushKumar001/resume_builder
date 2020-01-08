from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,View
from personal_info.models import ContactInfo
from education.models import EducationInfo
from experience.models import Experience
from project.models import Project,Certification
from skills.models import TechSkill
from summary.models import Summary
import json
from django.forms import model_to_dict
from django.http import HttpResponse
from django.template.loader import get_template,render_to_string
from .utils import render_to_pdf
from weasyprint import HTML,CSS,default_url_fetcher
from django.conf import settings
import tempfile
import logging
import pdfcrowd
import sys
# Create your views here.



def get_session_value(self):

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')

        return fname

class ReviewList(LoginRequiredMixin,TemplateView):
    template_name = 'review/review_index.html'
    #template_name = 'review/resume_index1.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ReviewList,self,).get_context_data(*args,**kwargs)
        fname = get_session_value(self)
        id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
        context['contact']= ContactInfo.objects.filter(first_name=fname).values()
        context['education'] = EducationInfo.objects.filter(user_id=id)
        context['experience'] = Experience.objects.filter(user_id=id)
        context['project'] = Project.objects.filter(user_id=id)
        context['certification'] = Certification.objects.filter(user_id=id)
        context['t_skill'] = TechSkill.objects.filter(user_id=id)
        context['summary'] = Summary.objects.filter(user_id=id)
        return context

class GeneratePdf(View):

    def get(self,request,*args,**kwargs):
        logger = logging.getLogger('weasyprint')

        template = get_template('review/resume.html')
        fname = get_session_value(self)
        id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
        contact= ContactInfo.objects.filter(first_name=fname).values()
        education = EducationInfo.objects.filter(user_id=id)
        experience = Experience.objects.filter(user_id=id)
        project = Project.objects.filter(user_id=id)
        certification = Certification.objects.filter(user_id=id)
        t_skill = TechSkill.objects.filter(user_id=id)
        summary = Summary.objects.filter(user_id=id)
        context = {
            'contact':contact,
            'education':education,
            'experience':experience,
            'project':project,
            'certification':certification,
            't_skill':t_skill,
            'summary':summary
        }
        # html = template.render(context)

        # #Rendered
        
        # creating http response        
        response = HttpResponse(content_type='application/pdf;')
        response['Content-Disposition'] = 'inline;filename=resume_aayush.pdf'
        html_string = render_to_string('review/resume.html',context)
        html = HTML(string=html_string,base_url=request.build_absolute_uri())
        result = html.write_pdf(response,
        stylesheets=[settings.STATIC_DIR+'\\css\\bootstrap.css',
        settings.STATIC_DIR+'\\fonts\\glyphicons-halflings-regular.ttf',
        settings.STATIC_DIR+'\\fonts\\glyphicons-halflings-regular.svg',
        settings.STATIC_DIR+'\\fonts\\glyphicons-halflings-regular.woff',
        settings.STATIC_DIR+'\\fonts\\glyphicons-halflings-regular.woff2',
        CSS(settings.STATIC_DIR+'\\css\\master\\style_pdf.css'),]
        )
        logger.addHandler(logging.FileHandler(settings.BASE_DIR+"\\weasyprint.log"))

        return response

def index(request):
    try:
        # enter your Pdfcrowd credentials to the converter's constructor
        client = pdfcrowd.HtmlToPdfClient('demo', 'ce544b6ea52a5621fb9d55f8b542d14d')
        print('Inside Try block')
        
        
        # convert a web page and store the generated PDF to a variable
        #logger.info('running Pdfcrowd HTML to PDF conversion')

        # set HTTP response headers
        response = HttpResponse(content_type='application/pdf')
        response['Cache-Control'] = 'max-age=0'
        response['Accept-Ranges'] = 'none'
        content_disp = 'attachment' if 'asAttachment' in request.POST else 'inline'
        response['Content-Disposition'] = content_disp + '; filename=demo_django.pdf'

        html = render_to_string(
            'review/review_index.html')
        client.convertStringToStream(html, response)

        # send the generated PDF
        return response
    except pdfcrowd.Error as why:
        #logger.error('Pdfcrowd Error: %s', why)
        return HttpResponse(why)