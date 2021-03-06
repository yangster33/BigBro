# Generated by Django 3.0.1 on 2020-01-21 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeekendCostsFlows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='流程名称')),
                ('desc', models.CharField(max_length=200, verbose_name='流程描述')),
                ('flow', models.CharField(max_length=200, verbose_name='流程内容')),
                ('step', models.IntegerField(default=0, verbose_name='当前流程状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('done_time', models.DateTimeField(verbose_name='完成时间')),
            ],
            options={
                'verbose_name': '流程',
                'verbose_name_plural': '流程',
            },
        ),
    ]
