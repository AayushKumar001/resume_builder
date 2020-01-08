from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView
from . import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from personal_info.models import ContactInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
from extra_views import CreateWithInlinesView as InlineFormSet
from django.utils.text import slugify



class PersonalContactInfoView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    form_class = forms.PersonalContactInfoForm
    model = ContactInfo
    
    def form_valid(self, form):
    
        if self.request.method == 'POST':
            
            if 'save' in self.request.POST:
                self.object = form.save(commit=False)
                self.object.slug = slugify(self.object.first_name)
                if 'profile_pic' in self.request.FILES:
                    print('Profile pic is getting inserted')
                    self.object.profile_pic = self.request.FILES['profile_pic']
                    
                first_name = self.object.first_name
                self.request.session['fname'] = first_name


                #session_value = self.request.session.get('fname','')
                self.object.save()

            elif 'cancel' in self.request.POST:
                return render(self.request,'thanks.html')
                
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print(form.errors)    
        return response