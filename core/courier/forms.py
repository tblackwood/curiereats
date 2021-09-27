from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from core.models import Courier

class PayoutForm(forms.ModelForm):
    class Meta:
        model = Courier
        fields = ('paypal_email',)
        

