# Generated by Django 2.2.17 on 2021-01-20 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rutUsuario',
            field=models.CharField(default=None, max_length=10),
        ),
    ]
