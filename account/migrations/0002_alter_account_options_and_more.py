# Generated by Django 4.1.7 on 2023-03-26 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Account'},
        ),
        migrations.AlterModelOptions(
            name='staffaccountprofile',
            options={'verbose_name': 'Staff Profile  List', 'verbose_name_plural': 'Staff Profile  List'},
        ),
        migrations.AlterModelOptions(
            name='useraccount',
            options={'verbose_name': 'User Account', 'verbose_name_plural': 'User Accounts List'},
        ),
    ]