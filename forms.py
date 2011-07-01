from django.forms import ModelForm
from django import forms
from models import *


class JobForm(ModelForm):
    UNIT_CHOICES = (
            ('--No Unit Selected--','--No Unit Selected--'),
            ('Facilities', 'Facilities'),
            ('Residence Life', 'Residence Life'),
            ('Business', 'Business'),
            ('ResTek', 'ResTek'),
            ('Assignments', 'Assignments'),
            ('Director', 'Director'),
    )
    
    unit = forms.ChoiceField(choices=UNIT_CHOICES)
    
    class Meta:
        model = Job
    
    def clean_unit(self):
        unit = self.cleaned_data['unit']
        if (unit == "--No Unit Selected--"):
            raise forms.ValidationError("Please Select A Unit")
        return unit


class LocationForm(ModelForm):
    class Meta:
        model = Location


class PersonForm(ModelForm):
    class Meta:
        model = Person


class PurchaseForm(ModelForm):
    class Meta:
        model = Purchase


class StatusForm(ModelForm):
    class Meta:
        model = Status


class EsignForm(ModelForm):
    class Meta:
        model = Esign


class Esign_SysForm(ModelForm):
    class Meta:
        model = Esign_Sys
        exclude = ('esign_ID',)
        

class DeviceForm(ModelForm):
    class Meta:
        model = Device
        exclude = ('last_update',)
