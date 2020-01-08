from django.shortcuts import render
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localdate,datetime
from .models import Summary
from .forms import SummaryForm
from personal_info.models import ContactInfo
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def get_session_value(self):

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')

        return fname

def get_current_date(self):

        x = localdate().strftime('%d-%b-%Y')
        date_obj = datetime.strptime(x,'%d-%b-%Y').date()

        return date_obj

class SummaryIndexView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'summary/summary_index.html'

class SummaryCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Summary
    form_class = SummaryForm

    def form_valid(self,form):
    
        if self.request.method == 'POST':          
            
            if 'save' in self.request.POST:
                
                self.object = form.save(commit=False)
                self.last_update_date=get_current_date(self)
                fname = get_session_value(self)
                
                queryset = ContactInfo.objects.get(first_name__exact=fname)
                self.object.user = queryset
                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('summary:index'))

        return HttpResponseRedirect(self.get_success_url())  

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response    