# Generated by Django 3.2 on 2023-07-07 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Categoria Slider',
                'verbose_name_plural': 'Categorias Sliders',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=200, null=True)),
                ('subtitulo', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(help_text='El tamaño de la imagen debe ser de 1920 x 850 pixeles', upload_to='blog/slider_principal')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('activo', models.BooleanField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categoriaslider')),
            ],
            options={
                'verbose_name': 'slider',
                'verbose_name_plural': 'sliders',
            },
        ),
    ]
