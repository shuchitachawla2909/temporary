# Generated by Django 5.1.1 on 2024-10-21 06:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='awards',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='cast',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='director',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='language',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='year',
        ),
    ]