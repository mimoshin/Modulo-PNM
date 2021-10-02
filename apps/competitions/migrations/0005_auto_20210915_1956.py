# Generated by Django 3.1.7 on 2021-09-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competitions', '0004_jumpheats_mdheats_speedheats_throwheats'),
    ]

    operations = [
        migrations.AddField(
            model_name='jumpheats',
            name='numberHeat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jumpheats',
            name='observation',
            field=models.CharField(default='S/O', max_length=200),
        ),
        migrations.AddField(
            model_name='mdheats',
            name='numberHeat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mdheats',
            name='observation',
            field=models.CharField(default='S/O', max_length=200),
        ),
        migrations.AddField(
            model_name='speedheats',
            name='numberHeat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='speedheats',
            name='observation',
            field=models.CharField(default='S/O', max_length=200),
        ),
        migrations.AddField(
            model_name='throwheats',
            name='numberHeat',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='throwheats',
            name='observation',
            field=models.CharField(default='S/O', max_length=200),
        ),
    ]
