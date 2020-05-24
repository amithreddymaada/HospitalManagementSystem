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
<<<<<<< HEAD
    path('patientbio/<int:pk>', user_views.PatientBioUpdateView.as_view(), name='p-update'),
=======
    path('receptionist/appointments/',user_views.receptionist_appointments_list,name='receptionist-appointments'),
    path('receptionist/appointments/create/',user_views.appointment_create,name='receptionist-appointments-create'),
    path('receptionist/appointments/<int:pk>/update/',
        user_views.AppointmentUpdateView.as_view(),
        name='receptionist-appointments-update'),
>>>>>>> 0094bba5cbb85712ba254d411c9dceb565d432d7

]