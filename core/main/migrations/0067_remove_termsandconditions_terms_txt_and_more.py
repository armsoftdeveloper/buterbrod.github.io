# Generated by Django 4.2 on 2023-04-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0066_remove_termsandconditions_terms_title_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='termsandconditions',
            name='terms_txt',
        ),
        migrations.AddField(
            model_name='termsandconditions',
            name='description',
            field=models.TextField(null=True, verbose_name='Տեքստ'),
        ),
    ]