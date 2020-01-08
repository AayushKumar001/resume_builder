from django import forms
from personal_info.models import ContactInfo
from django.contrib.auth.models import User
from betterforms.multiform import MultiModelForm

class PersonalContactInfoForm(forms.ModelForm):
    class Meta():
        model = ContactInfo
        fields = ('first_name','last_name','address','city','state','zip_code','country','email','phone','profile_pic')

        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder':'First Name',
                'class':'form-control col-xs-6'
            }),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Last Name',
                'class':'form-control col-xs-6'
            }),
            'address':forms.TextInput(attrs={
                'placeholder':'Address',
                'class':'form-control col-xs-6'
            }),
            'city':forms.TextInput(attrs={
                'placeholder':'City',
                'class':'form-control col-xs-6'
            }),
            'state':forms.TextInput(attrs={
                'placeholder':'State',
                'class':'form-control col-xs-6'
            }),
            'zip_code':forms.TextInput(attrs={
                'placeholder':'Zip Code',
                'class':'form-control col-xs-6'
            }),
            'country':forms.TextInput(attrs={
                'placeholder':'Country',
                'class':'form-control col-xs-6'
            }),
            'email':forms.TextInput(attrs={
                'placeholder':'Email',
                'class':'form-control col-xs-6'
            }),
            'phone':forms.TextInput(attrs={
                'placeholder':'Phone',
                'class':'form-control col-xs-6'
            })
        }
    def __init__(self,*args,**kwargs):
        kwargs.setdefault('label_suffix', '')       
        super(PersonalContactInfoForm, self).__init__(*args, **kwargs)        
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['address'].label = "Address"
        self.fields['city'].label = "City"
        self.fields['state'].label = "State"
        self.fields['zip_code'].label = "Zip Code"
        self.fields['country'].label = "Country"
        self.fields['email'].label = "Email Address"
        self.fields['phone'].label = "Phone" 