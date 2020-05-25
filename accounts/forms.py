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

def get_patients():
        data = Profile.objects.filter(type='patient')
        PATIENTS = list()
        for user in data:
            PATIENTS.append((user.user.username,user.user.username.upper()))
        return PATIENTS

class MedicalHistoryForm(forms.Form):
    patient_name = forms.ChoiceField(choices = get_patients())
    symptoms = forms.CharField()
    prescription = forms.CharField(widget=forms.Textarea)

    
STATUS = (
    ('pending', 'PENDING'),
    ('completed', 'COMPLETED')
)

def get_doctors():
        DOCTORS = list()
        data = Profile.objects.filter(type='doctor')
        for user in data:
            DOCTORS.append((user.user.username,user.user.username.upper()))
        return DOCTORS

class AppointmentForm(forms.Form):
    patient_name = forms.ChoiceField(choices = get_patients())
    consulting_doctor = forms.ChoiceField(choices = get_doctors())
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



