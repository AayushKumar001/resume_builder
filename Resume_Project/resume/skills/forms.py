from django import forms
from skills.models import KeySkill,TechSkill
from betterforms.multiform import MultiModelForm


class KeySkillForm(forms.ModelForm):
    
    class Meta():
        model = KeySkill
        exclude = ['user','last_update_date']
        widgets = {'key_skill':forms.Textarea(attrs={'placeholder':"eg. Project Management",
                                'class':'form-control z-depth-1 description key-skill','rows':1
                    })}
    def __init__(self,*args,**kwargs):
        super(KeySkillForm, self).__init__(*args, **kwargs)
        self.fields['key_skill'].label='Key Skill'


class TechSkillForm(forms.ModelForm):

    y = [ i for i in range(2019,0,-1) if i >= 1980 ]
    years = [(val,str(val)) for val in y ]

    last_used = forms.ChoiceField(
        widget=forms.Select(attrs={'class':'last-used'}),
        choices=years)

    class Meta():
        model=TechSkill
        exclude = ['user','last_update_date','rating']
        widgets = {'tech_skill':forms.TextInput(attrs={'placeholder':' eg. Java',
                                'class':'textinputclass1'
                    }),
                    'tech_skill_description':forms.Textarea(attrs={'placeholder':'eg. Use only keywords to describe your skill',
                                'class':'form-control z-depth-1 description','rows':3
                    }),
                    'version':forms.TextInput(attrs={'class':'textinputclass1'
                    }),
                    'experience':forms.TextInput(attrs={'class':'textinputclass1'
                    })
            }

    def __init__(self,*args,**kwargs):
        super(TechSkillForm, self).__init__(*args, **kwargs)
        self.fields['tech_skill'].label='Skill'
        self.fields['tech_skill_description'].label='Description'
        self.fields['version'].required=False
        self.fields['last_used'].required=False
        self.fields['experience'].required=False