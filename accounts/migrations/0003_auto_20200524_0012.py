# Generated by Django 3.0.6 on 2020-05-23 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_doctorbio_patientbio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorbio',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorbio',
            name='attendence',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorbio',
            name='department',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='doctorbio',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='doctorbio',
            name='salary',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='doctorbio',
            name='status',
            field=models.CharField(choices=[('active', 'ACTIVE'), ('inactive', 'INACTIVE')], max_length=9, null=True),
        ),
        migrations.AlterField(
            model_name='patientbio',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='patientbio',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patientbio',
            name='blood_group',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='patientbio',
            name='gender',
            field=models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='patientbio',
            name='medical_reports',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
