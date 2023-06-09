# Generated by Django 4.2 on 2023-05-09 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0086_links_food_zone_menu_am_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PagePictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to='media/%Y/%md/%d', verbose_name='Ներբեռնել Նկար')),
                ('description', models.CharField(max_length=50, verbose_name='Վերնագիր')),
            ],
            options={
                'verbose_name': 'Էջերի Պատկերներ',
                'verbose_name_plural': 'Էջերի Պատկերներ',
            },
        ),
    ]
