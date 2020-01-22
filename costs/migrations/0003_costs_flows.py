# Generated by Django 3.0.1 on 2020-01-21 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0001_initial'),
        ('costs', '0002_remove_costs_flows'),
    ]

    operations = [
        migrations.AddField(
            model_name='costs',
            name='flows',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='flows.WeekendCostsFlows', verbose_name='流程'),
            preserve_default=False,
        ),
    ]
