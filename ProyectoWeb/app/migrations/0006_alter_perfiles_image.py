# Generated by Django 4.1.3 on 2022-12-18 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='image',
            field=models.ImageField(default='prota.png', upload_to=''),
        ),
    ]
