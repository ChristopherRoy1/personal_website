# Generated by Django 3.0.2 on 2020-01-08 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0005_auto_20200108_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationitem',
            name='education_item_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workitem',
            name='work_item_end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
