# Generated by Django 5.1.2 on 2024-11-28 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('powerint', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Units',
            new_name='Unit',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]