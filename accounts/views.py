from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,ProfileUpdateForm,MedicalHistoryForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,PatientBio,DoctorBio, Appointment
from django.contrib.auth.decorators import login_required
from .models import MedicalHistory
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView
from django.core.exceptions import ValidationError

def register(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            user = User.objects.get(username=u_form.cleaned_data.get('username'))
            profile = Profile.objects.create(user= user,type=p_form.cleaned_data.get('type'))
            user.profile.save()
            if profile.type in ['PATIENT','patient']:
                patient = PatientBio.objects.create(patient =user)
                patient.save()
            else:
                doctor  = DoctorBio.objects.create(doctor = user)
                doctor.save()
            messages.success(request,'successfully registered!')
            return redirect('home')
    else :
        u_form = UserRegistrationForm()
        p_form = ProfileUpdateForm()
    context ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'accounts/register.html',context)

@login_required
def index(request):
    return render(request,'accounts/base.html')

@login_required
def appointments(request,type):
    if type == 'patient':
        data = Appointment.objects.filter(patient_name = request.user).order_by('-date','-time')
    else :
        data = Appointment.objects.filter(consulting_doctor = request.user).order_by('-date','-time')
    return render(request,'accounts/appointments.html',{'appointments':data,'type':type})

@login_required
def medical_history(request,type):
    if type== "patient":
        data =MedicalHistory.objects.filter(patient_name=request.user).order_by('-date','-id')
    else:
        data=MedicalHistory.objects.filter(doctor_name=request.user).order_by('-date','-id')
    return render(request,'accounts/medical_history.html',{'data':data,'type':type})





def prescription_create(request):
    if request.method == 'POST':
        form = MedicalHistoryForm(request.POST)
        if form.is_valid():
            patient = User.objects.get(username=form.cleaned_data['patient_name'])
            prescription = MedicalHistory.objects.create(
                doctor_name = request.user,
                 patient_name = patient,
                 symptoms = form.cleaned_data['symptoms'],
                 prescription = form.cleaned_data['prescription'] )
            prescription.save()
            messages.success(request,'successfully added prescription')
        return redirect('/accounts/med-history/doctor/')
    else:
        form = MedicalHistoryForm()
    return render(request,'accounts/prescription_create.html',{'form':form})





