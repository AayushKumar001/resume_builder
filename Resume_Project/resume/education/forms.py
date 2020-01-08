from django import forms
from education.models import EducationInfo
from personal_info.models import ContactInfo

class EducationForm(forms.ModelForm):

    degrees = (
        (None,'Select your Degree'),
        ('Bachelor of Architecture','B.Arch.'),
        ('Bachelor of Arts','B.A.'),
        ('Bachelor of Ayurvedic Medicine & Surgery','B.A.M.S.'),
        ('Bachelor of Business Administration','B.B.A.'),
        ('Bachelor of Commerce','B.Com'),
        ('Bachelor of Computer Applications','B.C.A.'),
        ('Bachelor of Technology','B.Tech.'),
    )

    specializations = (
        (None,'Select your Specialization'),
        ('AGRICULTURE','Agriculture'),
        ('AUTOMOBILE','Automobile'),
        ('COMPUTERS','Computers'),
        ('CHEMICAL','Chemical'),
        ('CIVIL','Civil'),
        ('MECHANICAL','Mechanical'),
        ('ELECTRICAL','Electrical'),
    )

    graduation_date = forms.DateField(
        widget=forms.DateInput(format='%d-%b-%Y',attrs={'class':'textinputclass1','placeholder':' 20-JAN-1992'}),
        input_formats=('%d-%b-%Y', )
        )
    degree=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'textinputclass1'}),
        choices=degrees
    )
    specialization=forms.ChoiceField(
        widget=forms.Select(attrs={'class':'textinputclass1'}),
        choices=specializations)

    class Meta():
        model = EducationInfo
        exclude = ['user','slug']
        widgets = {'school_name':forms.TextInput(attrs={'placeholder':"eg. St Karen's High School",
                                'class':'textinputclass1'
                                }),
                                'city':forms.TextInput(attrs={'placeholder':'eg. Patna',
                                'class':'textinputclass1'
                                }),
                                'state':forms.TextInput(attrs={'placeholder':'eg. Bihar',
                                'class':'textinputclass1'
                                }),
                                'field':forms.TextInput(attrs={'placeholder':'eg. Engineering',
                                'class':'textinputclass1'
                                }),
                                'present_check':forms.CheckboxInput(),
                                }

    def __init__(self,*args,**kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['graduation_date'].required=False
        self.fields['degree'].required=False
        self.fields['specialization'].required=False
        self.fields['field'].required=False
