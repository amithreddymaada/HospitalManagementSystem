from django.contrib import admin
from .models import Profile,PatientBio,DoctorBio, Appointment

admin.site.register(Profile)
admin.site.register(PatientBio)
admin.site.register(DoctorBio)
admin.site.register(Appointment)
