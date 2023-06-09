# Generated by Django 4.2 on 2023-04-24 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_delete_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=100, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('likes', models.CharField(max_length=250)),
                ('dob', models.DateField()),
                ('lives_in', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
