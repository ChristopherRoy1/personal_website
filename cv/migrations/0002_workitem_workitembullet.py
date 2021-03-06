# Generated by Django 3.0.2 on 2020-01-08 19:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_item_title', models.CharField(max_length=100)),
                ('work_item_company', models.CharField(max_length=100)),
                ('work_item_start_date', models.DateField(auto_now=True)),
                ('work_item_end_date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='WorkItemBullet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_item_bullet', models.CharField(max_length=100)),
                ('work_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cv.WorkItem')),
            ],
        ),
    ]
