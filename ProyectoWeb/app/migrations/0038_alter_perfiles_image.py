# Generated by Django 4.1.3 on 2023-01-06 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0037_alter_perfiles_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfiles',
            name='image',
            field=models.ImageField(default='defaul_profile.png', upload_to=''),
        ),
    ]