from django import forms
from project.models import Project,Certification

class ProjectForm(forms.ModelForm):
    
    class Meta():
        model = Project
        exclude = ('user','last_update_date','github_link')

        widgets = {'title':forms.TextInput(attrs={'placeholder':' eg. Geeta ',
                                'class':'textinputclass1'
                    }),
                    'description':forms.Textarea(attrs={'placeholder':'eg. Describe your project',
                                'class':'form-control z-depth-1 description','rows':3
                    }),
                    'technology':forms.Textarea(attrs={'placeholder':'eg. Javscript,Java',
                    'class':'form-control z-depth-1 description','rows':3
                    }),
                    'link_html':forms.TextInput(attrs={'class':'textinputclass1'
                    })
            }

    def __init__(self,*args,**kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)
        self.fields['link_html'].label='(Github/Project)Link'
        self.fields['link_html'].required=False
        self.fields['description'].required=False
        self.fields['title'].required=False
        self.fields['technology'].required=False


############################################################################################
#Certification Form

class CertificationForm(forms.ModelForm):


    y = [ i for i in range(2019,0,-1) if i >= 1980 ]
    years = [(val,str(val)) for val in y ]

    year = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'last-used'}),
        choices=years)


    class Meta():
        model = Certification
        exclude = ('user','last_update_date')

        widgets = {'certification':forms.TextInput(attrs={'placeholder':' eg. Python Certification',
                                'class':'textinputclass1'
                    }),
                    'certification_body':forms.TextInput(attrs={'placeholder':'eg. Coursera',
                                'class':'textinputclass1'
                    })
        }

    def __init__(self,*args,**kwargs):
        super(CertificationForm, self).__init__(*args, **kwargs)
        self.fields['year'].required=False