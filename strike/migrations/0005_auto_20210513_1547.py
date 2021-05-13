# Generated by Django 3.2.2 on 2021-05-13 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strike', '0004_auto_20210513_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='card_demand_category',
        ),
        migrations.AddField(
            model_name='card',
            name='card_demand_types',
            field=models.ManyToManyField(to='strike.DemandType', verbose_name='Характер требований'),
        ),
    ]
