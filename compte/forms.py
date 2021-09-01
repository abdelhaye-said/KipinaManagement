from django import forms
from django.db.models import fields
from django.forms.models import ModelForm
from .models import *

class create_profil(ModelForm):
    class Meta :
        model=Enfant
        fields=('__all__')

class create_cantine(ModelForm):
    class Meta :
        model=Cantine
        fields=('__all__')

class create_assurance(ModelForm):
    class Meta :
        model=Assurance
        fields=('__all__')

class create_forfait(ModelForm):
    class Meta :
        model=Forfait
        fields=('__all__')

class create_transport(ModelForm):
    class Meta :
        model=Transport
        fields=('__all__')
class create_garde(ModelForm):
    class Meta :
        model=Service_Garde
        fields=('__all__')
