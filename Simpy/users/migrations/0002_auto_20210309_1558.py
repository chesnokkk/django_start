# Generated by Django 3.1.7 on 2021-03-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default=None, upload_to='user_images', verbose_name='Photo'),
        ),
    ]
