# Generated by Django 4.2 on 2023-04-25 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0061_rename_about_us_title_ruu_about_about_us_title_fr_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_us_title_fr',
            new_name='about_us_title_ru',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about_us_txt_fr',
            new_name='about_us_txt_ru',
        ),
    ]