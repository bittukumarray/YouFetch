# Generated by Django 3.0.6 on 2020-09-30 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='video',
            old_name='VideoId',
            new_name='videoId',
        ),
    ]