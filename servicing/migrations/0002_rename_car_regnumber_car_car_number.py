# Generated by Django 4.0.6 on 2022-09-13 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicing', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='car_RegNumber',
            new_name='car_number',
        ),
    ]