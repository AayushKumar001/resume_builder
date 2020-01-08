from django import forms
from .models import Summary

class SummaryForm(forms.ModelForm):

    class Meta():
        model = Summary
        exclude = ('user','last_update_date')

        widgets = {'summary':forms.Textarea(attrs={'placeholder':' Write a short summary about yourself,your experience,your skills and achievements.',
                                'class':'form-control z-depth-1 summary','rows':5
                                
                    }),
                    'history':forms.Textarea(attrs={'placeholder':' Describe in brief about your variuos employment history.',
                    'class':'form-control z-depth-1 history','rows':5,
                    'id':'rich_with_insert_html_object',
                    })
        }

     
        