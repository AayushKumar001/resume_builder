from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,CreateView
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from contacts.models import Contact
# Create your views here.


def register(request):

    if request.method == 'POST':
        #Get Form Values
        print('Inside post')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        #check password match
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username is taken")
                
                return render(request,'accounts/register.html')
            else:
                #check email
                if User.objects.filter(email=email).exists():
                    messages.error(request,"That Email is used")
                    return render(request,'accounts/register.html')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
                    #Login after register
                    user.save()
                    messages.success(request,"You are now logged in:")
                    return render(request,'accounts/login.html')
        else:
            messages.error(request,"Passwords do not match")
    else:
        print('Form is invalid')
        return render(request,'accounts/register.html')
        
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in!!!')
            return redirect('accounts:dashboard')

        else:
            messages.error(request,'Invalid credentials')
            return redirect('accounts:login')    
    else:
        return render(request,'accounts/login.html')


class DashboardView(TemplateView):
    model = Contact
    template_name = 'accounts/dashboard.html'

    def get_context_data(self,*args,**kwargs):
        context = super(DashboardView,self).get_context_data(*args,**kwargs)
        
        context['user_contact'] = Contact.objects.order_by('-contact_date').filter(user_id=self.request.user.id)
        return context


def logout(request):
    if request.method =='POST':
        auth.logout(request)
        messages.success(request,"You are now logged out")
        return redirect('index')
        