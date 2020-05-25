from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('med-history/<str:type>/',user_views.medical_history,name='medical'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('appointments/<str:type>/',user_views.appointments,name='appointments'),
    path('prescriptions/create/',
            user_views.prescription_create,
            name='prescription-create'),

    path('patientbio/', user_views.patient_profile, name='p-update'),
    path('doctorbio/', user_views.doctor_profile, name='d-update'),
    path('receptionist/appointments/',user_views.receptionist_appointments_list,name='receptionist-appointments'),
    path('receptionist/appointments/create/',user_views.appointment_create,name='receptionist-appointments-create'),
    path('receptionist/appointments/<int:pk>/update/',
        user_views.AppointmentUpdateView.as_view(),
        name='receptionist-appointments-update'),
    path('receptionist/accounts/list/',user_views.accounts_list,name='list'),
    path('receptionist/pending-payments/',user_views.pending_payments,name='pending-payments'),
    path('receptionist/pending-payments/<int:pk>/update/',user_views.PaymentsUpdateView.as_view(),name='pending-payments-update'),
    path('patient/<str:username>/payments/',user_views.patient_payments,name='patient-payments'),
    path('patient/payments/<int:pk>/update/',user_views.PatientPaymentsUpdateView.as_view(),name='patient-payments-update'),
    path('patient/prescription/<int:pk>/detail/',user_views.MedicalHistoryDetailView.as_view(),name='patient-prescription-detail'),
    path('hr/dashboard/',user_views.hr_dashboard,name='hr-dashboard'),

]