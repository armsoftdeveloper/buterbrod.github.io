# Generated by Django 4.2 on 2023-04-25 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_alter_about_about_us_img_alter_about_about_us_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_us_txt',
            field=models.TextField(verbose_name='Մեր Մասին Տեքստ'),
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='food_zone_glovo',
            field=models.URLField(null=True, verbose_name='Glovo Հղում'),
        ),
        migrations.AlterField(
            model_name='basicmodel',
            name='food_zone_yandex_eat',
            field=models.URLField(null=True, verbose_name='Yandex Eat Հղում'),
        ),
        migrations.AlterField(
            model_name='get_email',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Էլ-Փոստ'),
        ),
        migrations.AlterField(
            model_name='get_message',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Էլ-Փոստ'),
        ),
        migrations.AlterField(
            model_name='get_message',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Անուն'),
        ),
        migrations.AlterField(
            model_name='get_message',
            name='phone',
            field=models.CharField(max_length=50, verbose_name='Հեռ․ Համար'),
        ),
        migrations.AlterField(
            model_name='get_message',
            name='txt',
            field=models.TextField(null=True, verbose_name='Հաղորդագրություն'),
        ),
        migrations.AlterField(
            model_name='indexpagereviews',
            name='customer_info',
            field=models.CharField(max_length=50, verbose_name='Անուն Ազգանուն'),
        ),
        migrations.AlterField(
            model_name='indexpagereviews',
            name='review',
            field=models.TextField(verbose_name='Մեկնաբանություն'),
        ),
        migrations.AlterField(
            model_name='indexpageslider',
            name='slider_img',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Նկար'),
        ),
        migrations.AlterField(
            model_name='indexpageslider',
            name='slider_title',
            field=models.CharField(max_length=50, verbose_name='Վերնագիր'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_published',
            field=models.BooleanField(default=True, null=True, verbose_name='Տեղադրված է ՞'),
        ),
        migrations.AlterField(
            model_name='menucategories',
            name='category',
            field=models.CharField(max_length=50, verbose_name='Կատեգորիայի Անուն'),
        ),
    ]
