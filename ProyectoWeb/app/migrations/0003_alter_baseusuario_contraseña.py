# Generated by Django 4.1.3 on 2022-12-01 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_crearusuario_baseusuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baseusuario',
            name='contraseña',
            field=models.CharField(max_length=20),
        ),
    ]
