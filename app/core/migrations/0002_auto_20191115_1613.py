# Generated by Django 2.1.14 on 2019-11-15 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_stuff',
            new_name='is_staff',
        ),
    ]
