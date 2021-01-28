# Generated by Django 3.1.5 on 2021-01-28 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0014_usuario_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('admin', 'admin'), ('medico', 'medico'), ('paciente', 'paciente'), ('cuidador', 'cuidador'), ('familiar', 'familiar')], default='admin', max_length=15),
        ),
    ]
