# Generated by Django 5.1.1 on 2024-10-20 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('director', models.TextField()),
                ('cast', models.TextField()),
                ('genre', models.TextField()),
                ('duration', models.IntegerField()),
                ('year', models.IntegerField()),
                ('language', models.CharField(max_length=100)),
                ('awards', models.TextField()),
                ('description', models.TextField()),
                ('review', models.TextField()),
            ],
        ),
    ]