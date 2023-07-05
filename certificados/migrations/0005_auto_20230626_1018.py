# Generated by Django 3.2 on 2023-06-26 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('encuestas', '0008_opcion_respuesta'),
        ('certificados', '0004_auto_20230626_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='encuestaalumno',
            name='opcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.opcion'),
        ),
        migrations.AddField(
            model_name='encuestaalumno',
            name='opciones_seleccionadas',
            field=models.ManyToManyField(blank=True, related_name='opciones_seleccionadas_alumno', to='encuestas.Opcion'),
        ),
        migrations.AddField(
            model_name='encuestaestudiante',
            name='opcion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.opcion'),
        ),
        migrations.AddField(
            model_name='encuestaestudiante',
            name='opciones_seleccionadas',
            field=models.ManyToManyField(blank=True, related_name='opciones_seleccionadas_estudiante', to='encuestas.Opcion'),
        ),
    ]
