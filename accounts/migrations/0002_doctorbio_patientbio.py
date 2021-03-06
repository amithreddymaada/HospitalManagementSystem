# Generated by Django 3.0.6 on 2020-05-23 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=8)),
                ('age', models.IntegerField()),
                ('address', models.TextField()),
                ('blood_group', models.CharField(max_length=4)),
                ('medical_reports', models.FileField(upload_to='')),
                ('patient', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DoctorBio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=8)),
                ('age', models.IntegerField()),
                ('status', models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], max_length=9)),
                ('department', models.CharField(max_length=20)),
                ('attendence', models.FloatField()),
                ('salary', models.IntegerField()),
                ('doctor', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
