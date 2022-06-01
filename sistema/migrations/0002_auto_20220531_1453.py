# Generated by Django 3.2 on 2022-05-31 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('lada', models.CharField(max_length=4)),
            ],
            options={
                'verbose_name': 'Ciudad',
                'verbose_name_plural': 'Ciudades',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('abreviatura', models.CharField(max_length=5)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.pais')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Colonia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('codigo_postal', models.CharField(max_length=7)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.ciudad')),
            ],
            options={
                'verbose_name': 'Colonia',
                'verbose_name_plural': 'Colonias',
            },
        ),
        migrations.AddField(
            model_name='ciudad',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sistema.estado'),
        ),
    ]