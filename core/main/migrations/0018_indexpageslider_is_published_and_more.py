# Generated by Django 4.2 on 2023-04-22 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_indexpageslideractive'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpageslider',
            name='is_published',
            field=models.BooleanField(default=True, null=True, verbose_name='Is Published ?'),
        ),
        migrations.AddField(
            model_name='indexpageslideractive',
            name='is_published',
            field=models.BooleanField(default=True, null=True, verbose_name='Is Published'),
        ),
    ]
