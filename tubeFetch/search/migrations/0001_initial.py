# Generated by Django 3.0.6 on 2020-09-30 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('VideoId', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=10000)),
                ('publishedDate', models.CharField(max_length=100)),
                ('thumb_default_url', models.URLField()),
                ('thumb_medium_url', models.URLField()),
                ('thumb_high_url', models.URLField()),
            ],
        ),
    ]
