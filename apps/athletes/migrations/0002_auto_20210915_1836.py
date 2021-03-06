# Generated by Django 3.1.7 on 2021-09-15 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('athletes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='athletes',
            name='athleteName',
            field=models.CharField(default='Nombre', max_length=200),
        ),
        migrations.AddField(
            model_name='athletes',
            name='athleteSurname',
            field=models.CharField(default='Apellido', max_length=200),
        ),
        migrations.AddField(
            model_name='athletes',
            name='dni',
            field=models.CharField(default='0.0.0-0', max_length=200),
        ),
        migrations.AddField(
            model_name='athletes',
            name='gender',
            field=models.IntegerField(choices=[(0, 'SIN GENERO'), (1, 'VARONES'), (2, 'DAMAS')], default=1),
        ),
    ]
