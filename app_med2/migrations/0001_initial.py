# Generated by Django 3.1.4 on 2021-01-27 14:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rutUsuario', models.CharField(default=None, max_length=10, primary_key=True, serialize=False, validators=[django.core.validators.MinLengthValidator(9, 'Ingresar dni en el siguiente formato 77111666-5'), django.core.validators.MaxLengthValidator(10, 'Ingresar dni en el siguiente formato 77111666-5')])),
                ('nombre', models.CharField(max_length=45, validators=[django.core.validators.MinLengthValidator(10, 'El nombre debe tener minimo 10 caracteres'), django.core.validators.MaxLengthValidator(45, 'El nombre puede tener hasta 45 caracteres')])),
                ('edad', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Error, la edad no puede ser menor a 1 '), django.core.validators.MaxValueValidator(99, 'Error, la edad no puede tener menos más de 3 números')])),
                ('direccion', models.CharField(max_length=45, validators=[django.core.validators.MinLengthValidator(10, 'Error, la dirección debe contener más de 10 caracteres'), django.core.validators.MaxLengthValidator(45, 'Error, la dirección puede contener hasta 45 caracteres ')])),
                ('staff', models.BooleanField()),
                ('usuario', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5, 'Error, el usuario debe tener mínimo 5 caracteres'), django.core.validators.MaxLengthValidator(15, 'Error, el usuario debe contener hasta 15 caracteres ')])),
                ('password', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(6, 'Error, la contraseña debe contener más de 6 caracteres'), django.core.validators.MaxLengthValidator(15, 'Error, la dirección puede contener hasta 15 caracteres ')])),
            ],
        ),
        migrations.CreateModel(
            name='PerfilLipidico',
            fields=[
                ('id_plipidico', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_plipidico', models.DateField()),
                ('nombre_plipidico', models.CharField(default='Examen de Perfil Lipidico', max_length=30)),
                ('colesterol', models.DecimalField(decimal_places=1, max_digits=4)),
                ('colesterol_ldl', models.DecimalField(decimal_places=1, max_digits=4)),
                ('colesterol_hdl', models.DecimalField(decimal_places=1, max_digits=4)),
                ('trigliceridos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observacion_plipidico', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='PerfilBioquimico',
            fields=[
                ('id_pbioquimico', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_pbioquimico', models.DateField()),
                ('nombre_pbioquimico', models.CharField(default='Examen de Perfil Bioquimico', max_length=30)),
                ('glucosa', models.DecimalField(decimal_places=1, max_digits=4)),
                ('nitrogeno_ureico', models.DecimalField(decimal_places=1, max_digits=4)),
                ('calcio', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fosforo', models.DecimalField(decimal_places=1, max_digits=4)),
                ('proteinas_totales', models.DecimalField(decimal_places=1, max_digits=4)),
                ('albumina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('colesterol_total', models.DecimalField(decimal_places=1, max_digits=4)),
                ('acido_urico', models.DecimalField(decimal_places=1, max_digits=4)),
                ('fosfatas_alcalinas', models.DecimalField(decimal_places=1, max_digits=4)),
                ('bilirrubina_total', models.DecimalField(decimal_places=1, max_digits=4)),
                ('ldh', models.DecimalField(decimal_places=1, max_digits=4)),
                ('got_ast', models.DecimalField(decimal_places=1, max_digits=4)),
                ('creatinina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observaciones_pbioquimico', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Orina',
            fields=[
                ('id_orina', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_orina', models.DateField()),
                ('nombre_orina', models.CharField(default='Examen de Orina', max_length=30)),
                ('color', models.CharField(max_length=25)),
                ('densidad', models.DecimalField(decimal_places=1, max_digits=4)),
                ('glucosa', models.DecimalField(decimal_places=1, max_digits=4)),
                ('cetonas', models.DecimalField(decimal_places=1, max_digits=4)),
                ('urobilinogeno', models.DecimalField(decimal_places=1, max_digits=4)),
                ('billirubina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observaciones_orina', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Hemograma',
            fields=[
                ('id_hemograma', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_hemograma', models.DateField()),
                ('nombre_hemograma', models.CharField(default='Examen de Hemograma', max_length=30)),
                ('eritrocito', models.DecimalField(decimal_places=1, max_digits=4)),
                ('leucocitos', models.DecimalField(decimal_places=1, max_digits=4)),
                ('hemoglobina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('hematocrito', models.DecimalField(decimal_places=1, max_digits=4)),
                ('vcm', models.DecimalField(decimal_places=1, max_digits=4)),
                ('chcm', models.DecimalField(decimal_places=1, max_digits=4)),
                ('plaquetas', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observaciones_hemograma', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Glicemia',
            fields=[
                ('id_glicemia', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_glicemia', models.DateField()),
                ('nombre_glicemia', models.CharField(default='Examen de Glicemia', max_length=30)),
                ('glicemia_basal', models.DecimalField(decimal_places=1, max_digits=4)),
                ('glicemia_120min', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observaciones_glicemia', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Diagnostico',
            fields=[
                ('fecha_diagnostico', models.DateTimeField(auto_now_add=True, primary_key=True, serialize=False)),
                ('diagnostico', models.CharField(max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Coagulacion',
            fields=[
                ('id_coagulacion', models.AutoField(default=None, primary_key=True, serialize=False)),
                ('fecha_coagulacion', models.DateField()),
                ('nombre_coagulacion', models.CharField(default='Examen de Coagulacion', max_length=30)),
                ('tiempo_protrombina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('porc_protrombina', models.DecimalField(decimal_places=1, max_digits=4)),
                ('observaciones_coagulacion', models.CharField(default='Parametros normales', max_length=100)),
                ('rutUsuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app_med2.usuario')),
            ],
        ),
    ]
