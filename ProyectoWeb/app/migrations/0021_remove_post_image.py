# Generated by Django 4.1.3 on 2022-12-27 21:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]