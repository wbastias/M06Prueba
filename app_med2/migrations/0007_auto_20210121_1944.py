# Generated by Django 3.1.4 on 2021-01-21 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0006_auto_20210121_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostico',
            name='fecha_diagnostico',
            field=models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False),
        ),
    ]