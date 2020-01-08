from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from project.forms import ProjectForm,CertificationForm
from django.utils.timezone import localdate,datetime
from personal_info.models import ContactInfo
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect
import misaka
from .models import Project,Certification

def get_session_value(self):

        if 'fname' in self.request.session:
            fname =self.request.session.get('fname','')

        return fname


def get_current_date(self):

        x = localdate().strftime('%d-%b-%Y')
        date_obj = datetime.strptime(x,'%d-%b-%Y').date()

        return date_obj


class ProjectIndexView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name='project/project_index.html'

class ProjectCreateView(LoginRequiredMixin,TemplateView):
    login_url = '/login/'
    template_name = 'project/project_certification_form.html'

    def get_context_data(self, **kwargs):
        context = super(ProjectCreateView,self).get_context_data(**kwargs)
        context['p_form'] = ProjectForm(prefix='p_form',data=self.request.POST or None)
        context['c_form'] = CertificationForm(prefix='c_form',data=self.request.POST or None)
        return context


    def post(self,request,*args,**kwargs):
        
        context = self.get_context_data(**kwargs)
        
        if 'save' in self.request.POST:
            if context['p_form'].is_valid() and context['c_form'].is_valid():
                instance=context['p_form'].save(commit=False)
                instance.last_update_date=get_current_date(self)
                fname = get_session_value(self)

                queryset = ContactInfo.objects.get(first_name__exact=fname)
                instance.user = queryset
                instance.github_link = misaka.html(instance.link_html)
                instance.save()

                #Prepare the tech skill model but don't commit it
                c_form = context['c_form'].save(commit=False)
                c_form.last_update_date = get_current_date(self)
                c_form.user = queryset
                c_form.save()

            else:
                self.form_invalid(context['c_form'])
                self.form_invalid(context['p_form'])

        elif 'back' in self.request.POST:
            return HttpResponseRedirect(reverse_lazy('project:index'))

        return HttpResponseRedirect(reverse('project:list'))
        
    def form_invalid(self, form):
        self.form = form
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response                              


class ProjectListView(LoginRequiredMixin,TemplateView):
    login_url ='/login/'
    template_name = 'project/project_list.html'


    def get_context_data(self,*args,**kwargs):
        context = super(ProjectListView,self,).get_context_data(*args,**kwargs)

        #retrieving the id or pk value
        id = ContactInfo.objects.filter(first_name=get_session_value(self)).values_list('id',flat=True).get()
        #select id from ContactInfo where first_name=fname


        context['projects'] = Project.objects.filter(user_id=id)
        context['certifications'] = Certification.objects.filter(user_id=id)
        context['p_form'] = ProjectForm(prefix='p_form',data=self.request.POST or None)
        context['c_form'] = CertificationForm(prefix='c_form',data=self.request.POST or None)
        return context
    
    def post(self,request,*args,**kwargs):
    
        context = self.get_context_data(**kwargs)
        
        if 'save' in self.request.POST:
            if context['p_form'].is_valid() and context['c_form'].is_valid():
                instance=context['p_form'].save(commit=False)
                fname = get_session_value(self)

                queryset = ContactInfo.objects.get(first_name__exact=fname)

                if(instance.title == '' and instance.description == '' and instance.technology == '' and instance.link_html == ''):
                    pass
                else:
                    print('Value is:'+instance.title)            
                    instance.last_update_date=get_current_date(self)
                    instance.user = queryset
                    instance.github_link = misaka.html(instance.link_html)
                    instance.save()

                #Prepare the tech skill model but don't commit it
                c_form = context['c_form'].save(commit=False)
                c_form.last_update_date = get_current_date(self)
                c_form.user = queryset
                c_form.save()
                return HttpResponseRedirect(self.request.path_info)
            
            else:
                self.form_invalid(context['c_form'])
                self.form_invalid(context['p_form'])

        # elif 'cancel' in self.request.POST:
        #         return reverse('project:list')

        return HttpResponseRedirect(reverse('project:list'))

    def form_invalid(self, form):
        
        response = super().form_invalid(form)
        print('Errors are: ')
        print(form.errors)    
        return response


class ProjectDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Project
    success_url = reverse_lazy('project:list')

class CertificationDeleteView(LoginRequiredMixin,DeleteView):
    login_url = '/login/'
    model = Certification
    success_url = reverse_lazy('project:list')

class ProjectUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    model = Project
    fields = ('description','technology','link_html')
    template_name = 'project/edit_project.html'
    redirect_field_name = 'project/project_list.html'

    def dispatch(self,*args,**kwargs):
        
        self.project_id = kwargs['pk']

        

        return super(ProjectUpdateView,self).dispatch(*args,**kwargs)

    def form_valid(self, form):

        if self.request.method == 'POST':
            print('Inside post')
            if 'save' in self.request.POST:
                print('Inside save')

                self.object = form.save(commit=False)
                self.object.last_update_date = get_current_date(self)
                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('project:list'))

        return HttpResponseRedirect(self.get_success_url())


class CertUpdateView(LoginRequiredMixin,UpdateView):
    model = Certification
    fields = ('certification_body','year')
    template_name = 'project/edit_certification.html'
    redirect_field_name = 'project/project_list.html'
    context_object_name = 'cert'

    def dispatch(self,*args,**kwargs):
        
        self.certification_id = kwargs['pk']

        print('*******'+str(self.certification_id))

        return super(CertUpdateView,self).dispatch(*args,**kwargs)

    def form_valid(self, form):

        if self.request.method == 'POST':
            print('Inside post')
            if 'save' in self.request.POST:
                print('Inside save')

                self.object = form.save(commit=False)
                self.object.last_update_date = get_current_date(self)
                self.object.save()

            elif 'cancel' in self.request.POST:
                return HttpResponseRedirect(reverse('project:list'))

        return HttpResponseRedirect(self.get_success_url())    