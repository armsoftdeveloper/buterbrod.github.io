# Generated by Django 4.2 on 2023-04-25 20:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0059_about_about_us_title_hy_about_about_us_txt_hy'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_us_title_ru',
            new_name='about_us_title_ruu',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='about_us_txt_ru',
            new_name='about_us_txt_ruu',
        ),
    ]
