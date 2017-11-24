# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-20 22:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='cedula_alumno',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='Cedula/Codigo'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='fecha_nacimiento',
            field=models.DateTimeField(verbose_name='Fecha De Nacimiento'),
        ),
    ]
