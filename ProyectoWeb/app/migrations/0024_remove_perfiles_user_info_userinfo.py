# Generated by Django 4.1.3 on 2022-12-29 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0023_perfiles_user_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfiles',
            name='user_info',
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userinfo', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userInfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
