# Generated by Django 4.1.7 on 2023-03-20 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0005_district_upazila_station_upazila'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Upazila',
        ),
        migrations.RenameField(
            model_name='station',
            old_name='upazila',
            new_name='District',
        ),
    ]