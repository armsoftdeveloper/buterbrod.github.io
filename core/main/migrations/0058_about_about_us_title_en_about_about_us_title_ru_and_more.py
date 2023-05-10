# Generated by Django 4.2 on 2023-04-25 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0057_alter_get_message_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='about_us_title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Վերնագիր'),
        ),
        migrations.AddField(
            model_name='about',
            name='about_us_title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Վերնագիր'),
        ),
        migrations.AddField(
            model_name='about',
            name='about_us_txt_en',
            field=models.TextField(null=True, verbose_name='Մեր Մասին Տեքստ'),
        ),
        migrations.AddField(
            model_name='about',
            name='about_us_txt_ru',
            field=models.TextField(null=True, verbose_name='Մեր Մասին Տեքստ'),
        ),
    ]
