from django.shortcuts import render, redirect
from .forms import UserRegistrationForm,ProfileUpdateForm,MedicalHistoryForm, AppointmentForm,UserUpdateForm,PatientUpdateForm,DoctorUpdateForm
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile,PatientBio,DoctorBio, Appointment
from django.contrib.auth.decorators import login_required
from .models import MedicalHistory, Payments
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,UpdateView
from django.core.exceptions import ValidationError
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import UpdateView,DetailView

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
            pay = Payments.objects.create(medical_report = prescription)
            prescription.payments.save()

            messages.success(request,'successfully added prescription')
        return redirect('/accounts/med-history/doctor/')
    else:
        form = MedicalHistoryForm()
    return render(request,'accounts/prescription_create.html',{'form':form})

@login_required
def receptionist_appointments_list(request):
    appointments = Appointment.objects.all().order_by('-date','-time', '-id')
    return render(request,'accounts/reception_appointments.html',{'appointments':appointments})

class AppointmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Appointment
    fields = ['status']
    template_name='accounts/receptionist_appointment_form.html'
    success_url = '/accounts/receptionist/appointments/'

def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            patient = User.objects.get(username=form.cleaned_data['patient_name'])
            doctor = User.objects.get(username=form.cleaned_data['consulting_doctor'])
            appointment = Appointment.objects.create(
                 patient_name = patient,
                 consulting_doctor = doctor,
                 status = form.cleaned_data['status'],
                 date = form.cleaned_data['date'],
                 time = form.cleaned_data['time']
                 )
            appointment.save()
            messages.success(request,'appointment added')
        return redirect('/accounts/receptionist/appointments/')
    else:
        form = AppointmentForm()
    return render(request,'accounts/receptionist_appointment_form.html',{'form':form})



@login_required
def patient_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = PatientUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.patientbio)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('p-update')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = PatientUpdateForm(instance=request.user.patientbio)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/update.html', context)



@login_required
def doctor_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = DoctorUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.doctorbio)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('d-update')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = DoctorUpdateForm(instance=request.user.doctorbio)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'accounts/update.html', context)

@login_required
def accounts_list(request):
    users = Profile.objects.filter(type='patient')
    patients = list()
    for user in users:
        patients.append(user.user)
    users = Profile.objects.filter(type='doctor')
    doctors = list()
    for user in users:
        doctors.append(user.user)
    

    return render(request,'accounts/receptionist_list.html',{'patients':patients,'doctors':doctors})

@login_required
def pending_payments(request):
    payments = list()
    for payment in Payments.objects.all():
        if payment.medical_report.billed == "no":
            payments.append(payment)
    return render(request, 'accounts/pending_payments.html',{'payments':payments})

class PaymentsUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Payments
    fields = ['total_amount']
    template_name = 'accounts/payments_update.html'
    success_url = '/accounts/receptionist/pending-payments/'

    def form_valid(self,form):
        pay = Payments.objects.get(id=form.instance.id)
        pay.medical_report.billed = "yes"
        pay.medical_report.save()
        print(pay.medical_report.billed)
        print(pay.medical_report.patient_name)
        return super().form_valid(form)
    def test_func(self):
        if self.request.user.profile.type == "receptionist":
            return True
        return False

@login_required
def patient_payments(request,username):
    patient = User.objects.get(username=username)
    payments = list()
    for payment in Payments.objects.all():
        if payment.medical_report.billed == "yes" and payment.medical_report.patient_name == patient:
            payments.append(payment)
    return render(request,'accounts/patient_payments.html',{'payments':payments})

class PatientPaymentsUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Payments
    fields = ['amount_paid']
    template_name = 'accounts/payments_update.html'

    
    def test_func(self):
        payment = self.get_object()
        if payment.medical_report.patient_name == self.request.user:
            return True
        return False

class MedicalHistoryDetailView(LoginRequiredMixin,UserPassesTestMixin,DetailView):
    model = MedicalHistory

    def test_func(self):
        obj = self.get_object()
        if obj.patient_name == self.request.user:
            return True
        return False

@login_required
def hr_dashboard(request):
    users = Profile.objects.filter(type='patient')
    patients = list()
    for user in users:
        patients.append(user.user)
    users = Profile.objects.filter(type='doctor')
    doctors = list()
    on_duty_doctors = list()
    for user in users:
        doctors.append(user.user)
        if user.user.doctorbio.status == "active":
            on_duty_doctors.append(user.user)
    payments_list = Payments.objects.all()
    total_amount_billed = 0
    amount_paid = 0
    for payments in payments_list:
        if payments.total_amount:
            total_amount_billed += payments.total_amount
        if payments.amount_paid:
            amount_paid += payments.amount_paid
    context = {
        'patients':patients,
        'doctors':doctors,
        'on_duty_doctors': on_duty_doctors,
        'total_amount':total_amount_billed,
        'amount_paid':amount_paid,
        'num_doctors':len(doctors),
        'num_patients':len(patients),
        'num_onduty':len(on_duty_doctors)
    }
    return render(request,'accounts/hr_dashboard.html',context)






