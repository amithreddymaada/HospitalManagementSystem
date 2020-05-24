from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,PatientBio,DoctorBio
from django.contrib.auth.decorators import login_required


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


