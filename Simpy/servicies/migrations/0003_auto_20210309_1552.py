# Generated by Django 3.1.7 on 2021-03-09 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicies', '0002_auto_20210304_1544'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sometable',
            options={'verbose_name': 'SomeTable', 'verbose_name_plural': 'SomeTables'},
        ),
        migrations.RemoveField(
            model_name='sometable',
            name='author',
        ),
        migrations.RemoveField(
            model_name='sometable',
            name='date',
        ),
    ]
