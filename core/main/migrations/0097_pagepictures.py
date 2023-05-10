# Generated by Django 4.2 on 2023-05-10 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0096_delete_pagepictures'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='media/%Y/%md/%d', verbose_name='Ներբեռնել Նկար')),
                ('decription', models.CharField(max_length=50, null=True, verbose_name='Էջի Անուն')),
            ],
            options={
                'verbose_name': 'Էջերի Պատկերներ',
                'verbose_name_plural': 'Էջերի Պատկերներ',
                'ordering': ['id'],
            },
        ),
    ]
