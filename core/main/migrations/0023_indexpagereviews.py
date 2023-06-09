# Generated by Django 4.2 on 2023-04-22 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_get_message_txt'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexPageReviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField(verbose_name='Customer Review')),
                ('star', models.IntegerField(verbose_name='Star Count')),
                ('customer_info', models.CharField(max_length=50, verbose_name='Customer Name & Surname')),
            ],
            options={
                'verbose_name': 'Reviews',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
