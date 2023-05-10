# Generated by Django 4.2 on 2023-04-24 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_rename_friendform_friend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Get_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='Phone Number')),
                ('txt', models.TextField(null=True, verbose_name='')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Ստեղծվելու Ամսաթիվ')),
            ],
            options={
                'verbose_name': 'Messages',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterModelOptions(
            name='friend',
            options={},
        ),
        migrations.RemoveField(
            model_name='friend',
            name='email',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='name',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='time_create',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='txt',
        ),
        migrations.AddField(
            model_name='friend',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='first_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='likes',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='lives_in',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='friend',
            name='nick_name',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]