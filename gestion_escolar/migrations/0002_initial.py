# Generated by Django 3.2 on 2022-06-06 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
        ('gestion_escolar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='alumnos',
            field=models.ManyToManyField(related_name='grupos', to='usuarios.Alumno'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='aula',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.aula'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.curso'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestion_escolar.nivel'),
        ),
        migrations.AddField(
            model_name='grupo',
            name='profesor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.profesor'),
        ),
    ]