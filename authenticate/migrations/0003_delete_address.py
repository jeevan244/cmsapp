# Generated by Django 4.0.4 on 2022-07-06 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_remove_address_customuser_address_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
    ]
