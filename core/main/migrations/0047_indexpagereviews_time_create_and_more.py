# Generated by Django 4.2 on 2023-04-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0046_menu_time_create_menu_time_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpagereviews',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
        migrations.AddField(
            model_name='indexpagereviews',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения'),
        ),
    ]
