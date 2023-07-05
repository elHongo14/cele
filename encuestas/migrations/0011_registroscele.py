# Generated by Django 3.2 on 2023-06-27 19:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0010_encuestaalumno_encuestaestudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegistrosCELE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuestaalumno')),
            ],
        ),
    ]
