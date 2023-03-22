# Generated by Django 4.1.7 on 2023-03-21 09:23

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('settings', '0007_alter_station_district'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userrole',
            options={'verbose_name': 'My Custom Group Name'},
        ),
        migrations.AlterModelManagers(
            name='userrole',
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='id',
        ),
        migrations.RemoveField(
            model_name='userrole',
            name='name',
        ),
        migrations.AddField(
            model_name='userrole',
            name='group_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.group'),
            preserve_default=False,
        ),
        migrations.AlterModelTable(
            name='userrole',
            table=None,
        ),
    ]