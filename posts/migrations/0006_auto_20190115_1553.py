# Generated by Django 2.1.4 on 2019-01-15 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_comment_hook'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0, null=True),
        ),
    ]