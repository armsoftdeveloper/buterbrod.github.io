# Generated by Django 4.2 on 2023-04-25 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0055_delete_indexpageslideractive_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='IndexPageReviewsActive',
        ),
        migrations.AlterModelOptions(
            name='indexpagereviews',
            options={'ordering': ['id'], 'verbose_name': 'Կարծիքների Սլայդեր', 'verbose_name_plural': 'Կարծիքների Սլայդեր'},
        ),
    ]
