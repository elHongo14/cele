# Generated by Django 3.2 on 2023-06-21 16:25

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Descripción')),
                ('activo', models.BooleanField(default=False)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Encuesta',
                'verbose_name_plural': 'Encuestas',
                'db_table': 'encuestas_encuesta',
            },
        ),
        migrations.CreateModel(
            name='Opcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_opcion', models.CharField(max_length=200, verbose_name='Texto opción')),
                ('valor', models.IntegerField(default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Opción',
                'verbose_name_plural': 'Opciones',
                'db_table': 'encuestas_opcion',
            },
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_pregunta', models.CharField(max_length=245, verbose_name='Texto de la pregunta')),
                ('texto_ayuda', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Texto de ayuda')),
                ('activo', models.BooleanField(default=True)),
                ('requerido', models.BooleanField(default=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuesta')),
            ],
            options={
                'verbose_name': 'Pregunta',
                'verbose_name_plural': 'Preguntas',
                'db_table': 'encuestas_pregunta',
            },
        ),
        migrations.CreateModel(
            name='TipoPregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Tipo de Pregunta',
                'verbose_name_plural': 'Tipo de Preguntas',
                'db_table': 'encuestas_tipo_pregunta',
            },
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto_respuesta', models.TextField(blank=True, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('encuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.encuesta')),
                ('opcion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='encuestas.opcion')),
                ('pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.pregunta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Respuesta',
                'verbose_name_plural': 'Respuestas',
                'db_table': 'encuestas_respuesta',
            },
        ),
        migrations.AddField(
            model_name='pregunta',
            name='tipo_pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.tipopregunta'),
        ),
        migrations.AddField(
            model_name='opcion',
            name='pregunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='encuestas.pregunta'),
        ),
    ]
