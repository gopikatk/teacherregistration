# Generated by Django 4.2.4 on 2023-09-27 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacherapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='admission',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='uid',
        ),
    ]
