# Generated by Django 4.2 on 2023-04-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_rename_user_person'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='User',
        ),
    ]
