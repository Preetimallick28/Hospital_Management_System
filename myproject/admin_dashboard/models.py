from django.contrib.auth.models import User
from django.db import models
from doctor_dashboard.models import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'is_staff': False}) 
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=200)
    
