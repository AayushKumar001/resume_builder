from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from experience.models import Experience
from experience.forms import ExperienceForm,ExperienceFormSet
from personal_info.models import ContactInfo
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.utils.timezone import localdate
from datetime import datetime
from django.shortcuts import get_object_or_404
# Create your views here.



class ExperienceIndexView(LoginRequiredMixin,TemplateView):
    template_name = 'experience/experience_index.html'
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'Testing Script!!!'
        return context

class ExperienceDetailView(LoginRequiredMixin,DetailView):
    login_url = '/login/'
    model = Experience
    template_name = 'experience/experience_detail.html'
    context_object_name = 'experience_detail'
    
        
class ExperienceListView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    model = Experience
    template_name = 'experience/experience_list.html'
    exclude = ('users','career_field','career_subfield')
    form_class = ExperienceForm
    
    
    
    def get_context_data(self,*args,**kwargs):
        context = super(ExperienceListView,self,).get_context_data(*args,**kwargs)

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')
        
        id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
        
        context['experience_detail']= Experience.objects.filter(user_id=id)
        
        context['form'] = ExperienceForm
        return context

    def post(self,request,*args,**kwargs):
    
        print('Getting called')
        form = self.form_class(request.POST)
        print(form)
        if form.is_valid():        
            if 'save' in self.request.POST:
                
                self.object = form.save(commit=False)
                
                if self.object.currently_work == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.end_date = date_obj

                if 'fname' in self.request.session:

                    fname =self.request.session.get('fname','')
                    
                    id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
                    queryset = ContactInfo.objects.get(first_name__exact=fname)
                    self.object.user = queryset
                    self.object.save()

                
                return HttpResponseRedirect(self.request.path_info)
            
            elif 'cancel' in self.request.POST:
                return reverse('experience:experience_index',kwargs={'slug':self.slug})
        else:
            print('Form is invalid')
            self.form_invalid(ExperienceForm)

        #return HttpResponseRedirect(reverse('experience:list',kwargs={'pk':self.kwargs.get('pk')}))
        return HttpResponseRedirect(reverse('experience:list'))
        #return  HttpResponseRedirect(self.get_success_url())
        


    def form_invalid(self, form):
        print('Errors are: ')
        print(form.errors)    
        return None

class ExperienceCreateView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    model = Experience
    form_class = ExperienceForm       
             
    def form_valid(self, form):       
        
        if self.request.method == 'POST':
                
            if 'save' in self.request.POST:
                self.object = form.save(commit=False)
                if self.object.currently_work == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.end_date =  date_obj

                if 'fname' in self.request.session:

                    fname =self.request.session.get('fname','')
                    
                
                queryset = ContactInfo.objects.get(first_name__exact=fname)
                
                self.object.user = queryset
                print('*******'+str(self.object.end_date))
                self.object.save()

            elif 'cancel' in self.request.POST:
                return reverse('experience:experience_index')

        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("*******"+form.errors)    
        return response    


class ExperienceUpdateView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    model = Experience
    redirect_field_name = 'experience/experience_list.html'
    template_name = 'experience/edit_experience.html'
    fields = ('job_title','end_date','currently_work','description',)
    context_object_name = 'exp'
    #by default form keyword can be used to create the form and Experience or exp will be used to extract data

    def dispatch(self,*args,**kwargs):
        
        self.experience_id = kwargs['pk']

        print('*******'+str(self.experience_id))

        return super(ExperienceUpdateView,self).dispatch(*args,**kwargs)

    def form_valid(self, form):

        if self.request.method == 'POST':
            print('Inside post')
            if 'save' in self.request.POST:
                print('Inside save')

                self.object = form.save(commit=False)
                
                if self.object.currently_work == True:
                    
                    x = localdate().strftime('%d-%b-%Y')
                    date_obj = datetime.strptime(x,'%d-%b-%Y').date()
                    self.object.end_date =  date_obj

                """ if 'fname' in self.request.session:

                    fname =self.request.session.get('fname','')
                    
                
                queryset = ContactInfo.objects.get(first_name__exact=fname)
                
                self.object.user = queryset """
                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('experience:list'))

        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        response = super().form_invalid(form)
        print("*******"+str(form.errors))    
        return response

class ExperienceDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Experience
    success_url = reverse_lazy('experience:list')            