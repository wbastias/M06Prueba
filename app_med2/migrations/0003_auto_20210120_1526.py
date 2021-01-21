# Generated by Django 2.2.17 on 2021-01-20 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_med2', '0002_auto_20210120_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coagulacion',
            name='fecha_coagulacion',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='diagnostico',
            name='fecha_diagnostico',
            field=models.DateField(default=None, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='glicemia',
            name='fecha_glicemia',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='hemograma',
            name='fecha_hemograma',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='orina',
            name='fecha_orina',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='perfilbioquimico',
            name='fecha_pbioquimico',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='perfillipidico',
            name='fecha_plipidico',
            field=models.DateField(),
        ),
    ]