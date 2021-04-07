from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Incident(models.Model):
    Corporate_Headoffice = 1
    Operations_Department= 2
    Work_Station         = 3
    Marketing_Division   = 4

    TYPE_CHOICES = (
        (Corporate_Headoffice,'Corporate Headoffice'),
        (Operations_Department,'Operations Department'),
        (Work_Station,'Work Station'),
        (Marketing_Division,'Marketing Division'),
    )
    Mild = 1
    Modarate = 2
    Severe = 3
    Fatal = 4
    severity_choices =(
        (Mild,'Mild'),
        (Modarate,'Modarate'),
        (Severe,'Severe'),
        (Fatal,'Fatal')
    )
    Environmental_Incident = 1
    Injurry_Illness=2
    Property_Damage  = 3
    Vehicle = 4
    incident_choices =(
        ('1','Environmental_Incident'),
        ('2','Injurry//Illness'),
        ('3','Property_Damage'),
        ('4','Vehicle')
    )
    location = models.SmallIntegerField(choices=TYPE_CHOICES,default='1')
    Incident_Department = models.TextField()
    Date = models.DateField()
    Time = models.TimeField()
    Incident_location = models.TextField()
    Initial_Severity = models.SmallIntegerField(choices=severity_choices)
    suspected_Cause = models.TextField()
    immediate_Ation_Taken = models.TextField()
    Sub_Incident_Type = models.TextField()
    Reportes_By = models.ForeignKey(User, on_delete=models.CASCADE)

