
from .models import *
from django.forms import ModelForm


class massage_Form(ModelForm):
    class Meta:
        model = MASSAGE
        fields = ['user', 'receiver', 'subject', 'massage']




