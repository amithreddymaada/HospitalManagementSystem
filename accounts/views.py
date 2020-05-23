from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile

def register(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        p_form = ProfileUpdateForm(request.POST)

        if u_form.is_valid() and p_form.is_valid() :
            u_form.save()
            profile = Profile.objects.create(user=User.objects.get(username=u_form.cleaned_data.get('username')))
            profile.type = p_form.cleaned_data.get('type')
            profile.save()
            messages.success(request,'successfully created profile!')
            return redirect('home')
    else :
        u_form = UserRegistrationForm()
        p_form = ProfileUpdateForm()
    context ={
        'u_form':u_form,
        'p_form':p_form,
    }
    return render(request,'accounts/register.html',context)
