# Generated by Django 3.2 on 2023-07-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CertificadoAlumno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(blank=True, max_length=20, null=True)),
                ('firma', models.TextField()),
                ('cadena', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Certificado Alumno',
                'verbose_name_plural': 'Certificados Alumno',
                'db_table': 'certificados_certificado_alumno',
            },
        ),
        migrations.CreateModel(
            name='CertificadoEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folio', models.CharField(blank=True, max_length=20, null=True)),
                ('firma', models.TextField()),
                ('cadena', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Certificado Estudiante',
                'verbose_name_plural': 'Certificados Estudiante',
                'db_table': 'certificados_certificado_estudiante',
            },
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo de documento')),
                ('titulo', models.CharField(blank=True, max_length=145, null=True)),
                ('subtitulo', models.CharField(blank=True, max_length=145, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=145)),
                ('imagen', models.ImageField(upload_to='certificados')),
                ('direccion', models.CharField(blank=True, max_length=145, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
            },
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=30, null=True)),
                ('tipo_plantilla', models.CharField(choices=[('Constancia UTS', 'Constancia UTS'), ('Constancia Red Conocer', 'Constancia Red Conocer'), ('Cédula de Acreditación', 'Cédula de Acreditación'), ('Reconocimiento UTS', 'Reconocimiento UTS')], default='Constancia UTS', max_length=30, verbose_name='Tipo de Plantilla')),
                ('plantilla_con_firma', models.ImageField(default='default-image-certi-850x1100.png', help_text='El tamaño de la imagen debe estar en múltiplos de 850 x 1100 pixeles', upload_to='certificados', verbose_name='Plantilla con Firma')),
                ('plantilla_sin_firma', models.ImageField(default='default-image-certi-850x1100.png', help_text='El tamaño de la imagen debe estar en múltiplos de 850 x 1100 pixeles', upload_to='certificados', verbose_name='Plantilla sin Firma')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
            ],
            options={
                'verbose_name': 'Plantila',
                'verbose_name_plural': 'Plantillas',
                'db_table': 'certificados_plantilla',
            },
        ),
        migrations.CreateModel(
            name='DocumentoLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('imagen', models.ImageField(blank=True, default='default-image-certi-540x540.png', help_text='El tamaño de la imagen debe ser de 540 x 540 pixeles', null=True, upload_to='certificados')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')),
                ('documento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='certificados.documento')),
            ],
            options={
                'verbose_name': 'Logo',
                'verbose_name_plural': 'Logos',
                'db_table': 'certificados_documento_logo',
            },
        ),
    ]
