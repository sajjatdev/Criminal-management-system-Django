# Generated by Django 4.1.7 on 2023-04-02 12:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group', to='auth.group', verbose_name='User Roles')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Account List',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='profile/photo.jpeg', upload_to='profile/', verbose_name='Photo')),
                ('station', models.CharField(blank=True, default=0, max_length=255)),
                ('address', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('userAccount', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserAccount', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Account',
                'verbose_name_plural': 'User Accounts List',
            },
        ),
        migrations.CreateModel(
            name='StaffAccountProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='profile/photo.jpeg', upload_to='profile/', verbose_name='Photo')),
                ('cardNumber', models.CharField(max_length=255, unique=True, verbose_name='ID Number')),
                ('cardImage', models.ImageField(default='cardImage/card.jpeg', upload_to='cardImage/', verbose_name='ID Photo')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='StaffAccount', to=settings.AUTH_USER_MODEL)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.postion')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='settings.station')),
            ],
            options={
                'verbose_name': 'Staff Profile  List',
                'verbose_name_plural': 'Staff Profile  List',
                'db_table': 'staffProfile',
            },
        ),
    ]
