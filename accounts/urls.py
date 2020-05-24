from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('med-history/<str:type>/',user_views.medical_history,name='medical'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('appointments/<str:type>/',user_views.appointments,name='appointments')
]