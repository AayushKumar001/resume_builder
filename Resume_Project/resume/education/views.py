from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,UpdateView,ListView,DeleteView
from education.models import EducationInfo
from education.forms import EducationForm
from personal_info.models import ContactInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.timezone import localdate
from datetime import datetime
from django.utils.text import slugify
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy,reverse
# Create your views here.

class EducationCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = EducationInfo
    form_class = EducationForm

    def form_valid(self,form):
    
        if self.request.method == 'POST':          
            
            if 'save' in self.request.POST:
                
                self.object = form.save(commit=False)
                self.object.slug = slugify(self.object.school_name)
                
                if self.object.present_check == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.graduation_date = date_obj

                if 'fname' in self.request.session:

                    fname =self.request.session.get('fname','')
                    
                
                queryset = ContactInfo.objects.get(first_name__exact=fname)
                self.object.user = queryset
                self.object.save()

            elif 'back' in self.request.POST:
                print('Coming inside cancel')
                return HttpResponseRedirect(reverse('experience:list'))
                #return reverse('experience:experience_index',kwargs={'slug':self.slug})

        return HttpResponseRedirect(self.get_success_url())  

    def form_invalid(self, form):
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response

class EducationListView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    model = EducationInfo
    template_name = 'education/educationinfo_list.html'
    fields =('school_name','city','state','degree','specialization','graduation_date','present_check')
    form_class = EducationForm
    #educationinfo_list will be returned as a default context object name

    def get_context_data(self,*args,**kwargs):
        context = super(EducationListView,self,).get_context_data(*args,**kwargs)

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')
        
        #retrieving the id or pk value
        #id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True)
        id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
        #select id from ContactInfo where first_name=fname

        context['educationinfo_list']= EducationInfo.objects.filter(user_id=id)
        context['form'] = EducationForm
        return context


    def post(self,request,*args,**kwargs):
    
        
        form = self.form_class(request.POST)
        print('******')
        print(form)
        if form.is_valid():        
            if 'save' in self.request.POST:
                
                self.object = form.save(commit=False)
                self.object.slug = slugify(self.object.school_name)
                
                if self.object.present_check == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.graduation_date = date_obj

                if 'fname' in self.request.session:

                    fname =self.request.session.get('fname','')
                    
                
                    queryset = ContactInfo.objects.get(first_name__exact=fname)
                    self.object.user = queryset
                    self.object.save()
                id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
                #pk = EducationInfo.objects.filter(user_id=id).values_list('id',flat=True).get()
                
                return HttpResponseRedirect(self.request.path_info)
            
            

        return HttpResponseRedirect(self.get_success_url())  

    


    def form_invalid(self, form):
        
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response    

class EducationUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model=EducationInfo
    fields = ('city','state','degree','specialization','field','graduation_date','present_check')
    template_name = 'education/edit_educationinfo.html'
    redirect_field_name='education/educationinfo_list.html'
    context_object_name = 'edu'

    def dispatch(self,*args,**kwargs):
        
        self.educationinfo_id = kwargs['pk']

        print('*******'+str(self.educationinfo_id))

        return super(EducationUpdateView,self).dispatch(*args,**kwargs)

    def form_valid(self, form):

        if self.request.method == 'POST':
            print('Inside post')
            if 'save' in self.request.POST:
                print('Inside save')

                self.object = form.save(commit=False)
                
                if self.object.present_check == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.graduation_date =  date_obj

                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('education:list'))

        return HttpResponseRedirect(self.get_success_url())



class EducationDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = EducationInfo
    success_url=reverse_lazy('education:list')    