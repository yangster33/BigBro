# Generated by Django 3.0.1 on 2020-01-11 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='is_diligent_num_rise',
            field=models.BooleanField(default=False, verbose_name='勤奋指数状态'),
        ),
    ]
