from django  import forms
from . models import PaymentCheck

class CheckForm(forms.ModelForm):
    class Meta:
        model = PaymentCheck
        fields = ['shop','total_amount' , 'photo' ]

