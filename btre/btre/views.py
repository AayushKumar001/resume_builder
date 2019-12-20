from django.shortcuts import render
from django.views.generic import TemplateView
from listings.models import Listing
from realtors.models import Realtor
from .choices import bedroom_choices,state_choices,price_choices

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,*args, **kwargs):
        context = super(IndexView,self).get_context_data(*args,**kwargs)
        context['listings'] = Listing.objects.order_by('-list_date').filter(is_publish=True)[:3]
        context['state_choices'] = state_choices
        context['bedroom_choices'] = bedroom_choices
        context['price_choices'] = price_choices    
        return context

class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self,*args,**kwargs):
        context = super(AboutView,self).get_context_data(*args,**kwargs)
        #Get all realtors
        context['realtors'] = Realtor.objects.order_by('-hire_date')

        #Get mvp
        context['mvp_realtors'] = Realtor.objects.all().filter(is_mvp=True)
        
        return context
