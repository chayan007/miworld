# Generated by Django 2.1.4 on 2019-01-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20190107_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='like',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
