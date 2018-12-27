from django  import forms
from . models import Check

class CheckForm(forms.ModelForm):
    class Meta:
        model = Check
        fields = ['shop','total_amount' , 'photo' ]

