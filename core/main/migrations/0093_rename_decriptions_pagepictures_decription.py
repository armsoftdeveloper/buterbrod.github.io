# Generated by Django 4.2 on 2023-05-10 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0092_pagepictures_decriptions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagepictures',
            old_name='decriptions',
            new_name='decription',
        ),
    ]
