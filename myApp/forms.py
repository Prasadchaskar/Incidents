from django import forms
from . models import Incident
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.conf import settings
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.TimeInput):
    input_type = 'time'   
class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class IncidentsForm(forms.ModelForm):
    incident_choices =(
        ('Environmental_Incident','Environmental_Incident'),
        ('Injurry//Illness','Injurry//Illness'),
        ('Property_Damage','Property_Damage'),
        ('Vehicle','Vehicle')
    )
    Date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    Time = forms.TimeField(
    widget=forms.TextInput(     
        attrs={'type': 'time'} 
    )
)    
    Sub_Incident_Type = forms.MultipleChoiceField(choices=incident_choices, widget=forms.CheckboxSelectMultiple())
    class Meta:
        model = Incident 
        fields = ['location','Incident_Department','Date','Time','Incident_location','Initial_Severity','suspected_Cause','immediate_Ation_Taken','Sub_Incident_Type','Reportes_By']
       