# Generated by Django 4.2 on 2023-04-24 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0048_indexpagereviewsactive_time_create_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpagerefreshedmenu',
            name='is_published',
            field=models.BooleanField(default=True, null=True, verbose_name='Is Published ? '),
        ),
        migrations.AddField(
            model_name='indexpagerefreshedmenu',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время создания'),
        ),
        migrations.AddField(
            model_name='indexpagerefreshedmenu',
            name='time_update',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Время изменения'),
        ),
    ]
