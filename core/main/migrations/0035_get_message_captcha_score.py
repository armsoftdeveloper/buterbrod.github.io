# Generated by Django 4.2 on 2023-04-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_termsandconditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='get_message',
            name='captcha_score',
            field=models.FloatField(default=0.0),
        ),
    ]