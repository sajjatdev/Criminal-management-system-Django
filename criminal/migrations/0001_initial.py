# Generated by Django 4.1.7 on 2023-04-02 15:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('settings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CasesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('descriptions', models.TextField(max_length=500)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('In_Process', 'In Process'), ('open', 'Open'), ('running', 'Running'), ('done', 'Done')], default='pending', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Case List',
            },
        ),
        migrations.CreateModel(
            name='VictimModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('documentType', models.CharField(choices=[('nid', 'National ID card'), ('passport', 'Passport'), ('driving licence', 'Driving Licence')], default='None', max_length=255)),
                ('document', models.ImageField(upload_to='criminal/victim/')),
                ('cases', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminal.casesmodel')),
            ],
            options={
                'verbose_name': 'Victim',
                'verbose_name_plural': 'Victim List',
            },
        ),
        migrations.CreateModel(
            name='CriminalModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='criminal/profile/')),
                ('dateOfBirth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('othere', 'othere')], default='male', max_length=255)),
                ('documant_type', models.CharField(choices=[('nid', 'National ID card'), ('passport', 'Passport'), ('driving licence', 'Driving Licence')], default='none', max_length=255)),
                ('documant', models.FileField(upload_to='criminal/id/')),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='criminal.casesmodel')),
                ('crimeType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.crimetype')),
            ],
            options={
                'verbose_name': 'Criminal',
                'verbose_name_plural': 'Criminal List',
                'db_table': 'criminal',
            },
        ),
    ]
