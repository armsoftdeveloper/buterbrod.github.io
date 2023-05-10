# Generated by Django 4.2 on 2023-04-23 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_menu_menucategories_delete_menubarbeque_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpageassortment',
            name='assortment_burger',
            field=models.ImageField(null=True, upload_to='media/%Y/%m/%d', verbose_name='Upload Burger Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_barbeque',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Barbeque Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_beer',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Beer Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_gril',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Gril Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_lahmajo',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Lahmajo Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_shawarma',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Shawarma Image'),
        ),
        migrations.AlterField(
            model_name='indexpageassortment',
            name='assortment_soft_drinks',
            field=models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='Upload Soft Drinks Image'),
        ),
    ]
