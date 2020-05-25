from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

ACCOUNT_TYPES = (
    ('person', 'PERSON'),
    ('doctor', 'DOCTOR'),
    ('receptionist', 'RECEPTIONIST'),
    ('hr', 'HR'),
)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'profile')
    type = models.CharField(max_length=15, choices=ACCOUNT_TYPES)

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
    

    def __str__(self):
        return f'{self.patient.username} patient'

STATUS = (
    ('active', 'ACTIVE'),
    ('inactive', 'INACTIVE'),
)

class DoctorBio(models.Model):
    doctor = models.OneToOneField(User,on_delete = models.CASCADE, default = 1)
    gender = models.CharField(max_length = 8,choices = GENDER,null=True)
    age = models.IntegerField(null=True)
    status = models.CharField(max_length = 9,choices = STATUS,default="active")
    department = models.CharField(max_length=20,null=True)
    attendence = models.FloatField(null=True)
    salary = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.doctor.username} doctor'

STATUS = (
    ('pending', 'PENDING'),
    ('completed', 'COMPLETED')
)
class Appointment(models.Model):
    patient_name = models.ForeignKey(User, related_name='patient_name',on_delete = models.CASCADE)
    consulting_doctor = models.ForeignKey(User,related_name='consulting_doctor',on_delete = models.CASCADE)
    status = models.CharField(max_length=15,choices = STATUS)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f'appointement patient-{self.patient_name} doctor-{self.consulting_doctor}'



BILLED = (
    ('yes','YES'),
    ('no','NO')
)

class MedicalHistory(models.Model):
    date =models.DateField(auto_now_add = True)
    symptoms= models.TextField()
    doctor_name= models.ForeignKey(User ,related_name='medical_doctor',on_delete=models.CASCADE)
    patient_name=models.ForeignKey(User,related_name='medical_patient',on_delete=models.CASCADE)
    prescription=models.TextField(max_length=1000)
    billed = models.CharField(max_length=10, choices=BILLED,default = 'no')

    def __str__(self):
        return 'medical-history-patient'+self.patient_name.username+':doctor'+self.doctor_name.username

class Payments(models.Model):
    medical_report = models.OneToOneField(MedicalHistory,on_delete = models.CASCADE)
    total_amount = models.IntegerField(null=True)
    amount_paid = models.IntegerField(default=0)
    date = models.DateField(auto_now_add = True)


    def __str__(self):
        return f'{self.medical_report.patient_name} payment info'
    
    def get_absolute_url(self):
        return reverse('patient-payments', kwargs={'username':self.medical_report.patient_name.username})



