# Generated by Django 4.2 on 2023-04-24 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_get_message_captcha_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='get_message',
            name='captcha_score',
        ),
    ]
