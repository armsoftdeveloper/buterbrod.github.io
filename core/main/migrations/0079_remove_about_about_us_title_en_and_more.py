# Generated by Django 4.2 on 2023-05-03 18:57

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0078_menucategories_time_create_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='about_us_title_en',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_us_title_hy',
        ),
        migrations.RemoveField(
            model_name='about',
            name='about_us_title_ru',
        ),
        migrations.AlterField(
            model_name='get_message',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=50, region=None, verbose_name='Հեռ․ Համար'),
        ),
    ]