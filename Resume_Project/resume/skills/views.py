from django.shortcuts import render
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,UpdateView
from django.views.generic.base import ContextMixin
from skills.models import TechSkill,KeySkill
from skills.forms import KeySkillForm,TechSkillForm
from django.utils.timezone import localdate,datetime
from personal_info.models import ContactInfo
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from .languages import *
from skills.multiforms import MultiFormsView
# Create your views here.

def get_rating(self,description,value):
    description_list = description.split(',')
    value_length = len(value)
    print(value_length)
    count = 0
    for word in description_list:
        for words in value:
            if (word == words or word == words[:-1] or word == words[:-2]):
                count = count+1
    print(count)
    return (count/value_length)*100

def get_session_value(self):

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')

        return fname

def get_current_date(self):

        x = localdate().strftime('%d-%b-%Y')
        date_obj = datetime.strptime(x,'%d-%b-%Y').date()

        return date_obj

class SkillsIndexView(TemplateView):
    login_url = "/login/"
    template_name = 'skills/skills_index.html'

class SkillsCreateView(LoginRequiredMixin,TemplateView):
    login_url="/login/"
    template_name='skills/skill_form.html'    

    def get_context_data(self, **kwargs):
        context = super(SkillsCreateView,self).get_context_data(**kwargs)
        context['k_skill'] = KeySkillForm(prefix='k_skill',data=self.request.POST or None)
        context['t_skill'] = TechSkillForm(prefix='t_skill',data=self.request.POST or None)
        return context         
                      

    def post(self,request,*args,**kwargs):
        
        context = self.get_context_data(**kwargs)
        
        if 'save' in self.request.POST:
            if context['k_skill'].is_valid() and context['t_skill'].is_valid():
                instance=context['k_skill'].save(commit=False)
                instance.last_update_date=get_current_date(self)
                fname = get_session_value(self)

                queryset = ContactInfo.objects.get(first_name__exact=fname)
                instance.user = queryset
                instance.save()

                #Prepare the tech skill model but don't commit it
                tech_skills = context['t_skill'].save(commit=False)
                
                skill = context['t_skill'].cleaned_data.get('tech_skill')
                description = context['t_skill'].cleaned_data.get('tech_skill_description')
                
                for key in dict1:
                    if key == 'java':
                        if skill.casefold() == key.casefold():
                            
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'python':
                        if skill.casefold() == key.casefold():
                            print('Inside python block')
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'django':
                        print('key is django')
                        if skill.casefold() == key.casefold():
                            print('Inside django block')
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'html5':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'css':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])                            
                    elif key == 'javascript':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'bootstrap':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])
                    
                print('Percentage Match',rate)
                if rate <=20.0:
                    rate = 1.0
                elif rate >20.0 and rate <=40.0:
                    rate = 2.0
                elif rate >40.0 and rate <=60.0:
                    rate = 3.0
                elif rate >60.0 and rate <=80.0:
                    rate = 4.0
                elif rate >80.0 and rate <=100.0:
                    rate = 5.0
                tech_skills.last_update_date = get_current_date(self)
                tech_skills.rating = rate
                tech_skills.user = queryset
                tech_skills.save()

            else:
                self.form_invalid(context['k_skill'])
                self.form_invalid(context['t_skill'])
        elif 'back' in self.request.POST:
            return HttpResponseRedirect(reverse_lazy('skills:index'))

        return HttpResponseRedirect(reverse('skills:list'))
        
    def form_invalid(self, form):
        self.form = form
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response


class SkillListView(LoginRequiredMixin,TemplateView):
    
    login_url="/login/"
    template_name="skills/skill_list.html"
    form_class = TechSkillForm
    
    def get_context_data(self,*args,**kwargs):
        context = super(SkillListView,self,).get_context_data(*args,**kwargs)

        #retrieving the id or pk value
        id = ContactInfo.objects.filter(first_name=get_session_value(self)).values_list('id',flat=True).get()
        #select id from ContactInfo where first_name=fname

        context['t_skill']= TechSkill.objects.filter(user_id=id)
        context['t_form'] = TechSkillForm
        return context


    def post(self,request,*args,**kwargs):
    
        
        form = self.form_class(request.POST)
        
        if form.is_valid():        
            
            if 'save' in self.request.POST:
                
                self.object = form.save(commit=False)
                skill = form.cleaned_data.get('tech_skill')
                description = form.cleaned_data.get('tech_skill_description')
                for key in dict1:
                    if key == 'java':
                        if skill.casefold() == key.casefold():
                            
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'python':
                        if skill.casefold() == key.casefold():
                            print('Inside python block')
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'django':
                        print('key is django')
                        if skill.casefold() == key.casefold():
                            print('Inside django block')
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'html5':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'css':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])                            
                    elif key == 'javascript':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])
                    elif key == 'bootstrap':
                        if skill.casefold() == key.casefold():
                            rate = get_rating(self,description,dict1[key])

                print('Percentage Match',rate)
                if rate <=20.0:
                    rate = 1.0
                elif rate >20.0 and rate <=30.0:
                    rate = 1.5
                elif rate >30.0 and rate <=40.0:
                    rate = 2.0
                elif rate >40.0 and rate <=50.0:
                    rate = 2.5
                elif rate >50.0 and rate <=60.0:
                    rate = 3.0
                elif rate >60.0 and rate <=70.0:
                    rate = 3.5
                elif rate >70.0 and rate <=80.0:
                    rate = 4.0
                elif rate >80.0 and rate <=90.0:
                    rate = 4.5
                else:
                    rate = 5.0

                
                self.object.rating = rate
                self.object.last_update_date = get_current_date(self)
                queryset = ContactInfo.objects.get(first_name__exact=get_session_value(self))
                self.object.user = queryset
                self.object.save()
                fname = get_session_value(self)
                id = ContactInfo.objects.filter(first_name=fname).values_list('id',flat=True).get()
                
                return HttpResponseRedirect(self.request.path_info)
            
            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('skills:list'))

        return HttpResponseRedirect(reverse('skills:list'))

    def form_invalid(self, form):
        
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response   


class SkillDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = TechSkill
    success_url = reverse_lazy('skills:list')

class SkillUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = TechSkill
    fields = ('tech_skill_description','version','last_used','experience','last_update_date')
    template_name = 'skills/edit_skill.html'
    redirect_field_name = 'skills/skill_list.html'
    context_object_name = 't_skill'


    def dispatch(self,*args,**kwargs):
        
        self.techskill_id = kwargs['pk']

        print('*******'+str(self.techskill_id))

        return super(SkillUpdateView,self).dispatch(*args,**kwargs)

    def form_valid(self, form):

        if self.request.method == 'POST':
            print('Inside post')
            if 'save' in self.request.POST:
                print('Inside save')

                self.object = form.save(commit=False)
                self.object.last_update_date = get_current_date(self)
                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('skills:list'))

        return HttpResponseRedirect(self.get_success_url())    

    def form_invalid(self, form):
        
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response        