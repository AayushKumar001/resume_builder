from django import forms
from experience.models import Experience
from django.forms.models import inlineformset_factory,formset_factory
from personal_info.models import ContactInfo


class ExperienceForm(forms.ModelForm):

    start_date = forms.DateField(
        widget=forms.DateInput(format='%d-%b-%Y',attrs={'class':'textinputclass1','placeholder':' 20-JAN-1992'}),
        input_formats=('%d-%b-%Y', )
        )
    end_date = forms.DateField(
        widget=forms.DateInput(format='%d-%b-%Y',attrs={'class':'textinputclass1','placeholder':' 20-JAN-1992'}),
        input_formats=('%d-%b-%Y',)
    )

    class Meta():
        model = Experience
        fields = ('employer','job_title','city','state','start_date','end_date','currently_work','description')
        

        widgets = {
            'employer':forms.TextInput(attrs={'placeholder':' eg. Tata Consultancy Service',
                'class':'textinputclass1'
            }),
            'job_title':forms.TextInput(attrs={'placeholder':' eg. System Engineer',
                'class':'textinputclass1'
            }),
            'city':forms.TextInput(attrs={'placeholder':' Patna',
                'class':'textinputclass1'
            }),
            'state':forms.TextInput(attrs={'placeholder':' Bihar',
                'class':'textinputclass1'
            }),            
            'currently_work':forms.CheckboxInput(),
            'description':forms.Textarea(attrs={'placeholder':'Write Something here....',
                'class':'form-control z-depth-1 description'
            }),
        }


    
    def __init__(self, *args, **kwargs):

        kwargs.setdefault('label_suffix', '')       
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['currently_work'].label = 'I currently work here'
        self.fields['description'].label = "Job Description"
        self.fields['end_date'].required = False
        self.fields['employer'].required = False        
        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'The field {fieldname} is required'.format(
                fieldname=field.label),
                'invalid':"That's not a number Sir"}

ExperienceFormSet = inlineformset_factory(ContactInfo,Experience,form=ExperienceForm,extra=1,can_delete=True)