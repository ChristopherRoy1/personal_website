# Generated by Django 3.0.2 on 2020-01-08 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0009_workitembullet_work_item_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workitembullet',
            name='work_item_ordering',
            field=models.IntegerField(),
        ),
    ]
