from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile,MedicalHistory,PatientBio,DoctorBio


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name',
                  'last_name', 'password1', 'password2']


ACCOUNT_TYPES = (
    ('patient', 'PATIENT'),
    ('doctor', 'DOCTOR')
)

class ProfileUpdateForm(forms.Form):
    type = forms.ChoiceField(choices = ACCOUNT_TYPES)

data = Profile.objects.filter(type='patient')
PATIENTS = list()

for user in data:
    PATIENTS.append((user.user.username,user.user.username.upper()))

class MedicalHistoryForm(forms.Form):
    patient_name = forms.ChoiceField(choices = PATIENTS)
    symptoms = forms.CharField()
    prescription = forms.CharField(widget=forms.Textarea)

DOCTORS = list()
data = Profile.objects.filter(type='doctor')

for user in data:
    DOCTORS.append((user.user.username,user.user.username.upper()))

STATUS = (
    ('pending', 'PENDING'),
    ('completed', 'COMPLETED')
)
class AppointmentForm(forms.Form):
    patient_name = forms.ChoiceField(choices = PATIENTS)
    consulting_doctor = forms.ChoiceField(choices = DOCTORS)
    status = forms.ChoiceField(choices = STATUS)
    date = forms.DateField()
    time = forms.TimeField()
    

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email']


class PatientUpdateForm(forms.ModelForm):
    
    class Meta:
        model = PatientBio
        fields = [ 'gender','age','address','blood_group']


class DoctorUpdateForm(forms.ModelForm):
    
    class Meta:
        model = DoctorBio
        fields = [ 'gender','age','status','department','attendence','salary']



