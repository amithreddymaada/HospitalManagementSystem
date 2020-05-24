from django.db import models
from django.contrib.auth.models import User

ACCOUNT_TYPES = (
    ('person', 'PERSON'),
    ('doctor', 'DOCTOR')
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    type = models.CharField(max_length=6, choices=ACCOUNT_TYPES)

    def __str__(self):
        return f'{self.user.username} '+self.type


GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE'),
    ('other','OTHER')
)

class PatientBio(models.Model):
    patient = models.OneToOneField(User,on_delete = models.CASCADE, default = 1)
    gender = models.CharField(max_length = 8,choices = GENDER ,null=True)
    age = models.IntegerField(null=True)
    address = models.TextField(null=True)
    blood_group = models.CharField(max_length = 4,null=True)
    medical_reports = models.FileField(null=True)

STATUS = (
    ('active', 'ACTIVE'),
    ('inactive', 'INACTIVE'),
)

class DoctorBio(models.Model):
    doctor = models.OneToOneField(User,on_delete = models.CASCADE, default = 1)
    gender = models.CharField(max_length = 8,choices = GENDER,null=True)
    age = models.IntegerField(null=True)
    status = models.CharField(max_length = 9,choices = STATUS,null=True)
    department = models.CharField(max_length=20,null=True)
    attendence = models.FloatField(null=True)
    salary = models.IntegerField(null=True)
