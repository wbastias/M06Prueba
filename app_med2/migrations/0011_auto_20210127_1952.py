# Generated by Django 3.1.5 on 2021-01-27 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_med2', '0010_familiar_staff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='password',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='staff',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
