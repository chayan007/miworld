# Generated by Django 2.1.4 on 2019-01-22 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190115_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateField(auto_created=True, null=True),
        ),
    ]
