# Generated by Django 4.2 on 2023-04-22 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_alter_indexpagereviews_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indexpagereviews',
            name='star',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)], verbose_name='Star Count'),
        ),
    ]