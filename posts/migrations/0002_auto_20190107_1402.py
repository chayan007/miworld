# Generated by Django 2.1.4 on 2019-01-07 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='heading',
            new_name='task',
        ),
    ]
