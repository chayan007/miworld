# Generated by Django 2.1.4 on 2019-01-22 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medias', '0003_auto_20190116_0959'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='image',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='image',
            name='name',
        ),
        migrations.RemoveField(
            model_name='video',
            name='extension',
        ),
        migrations.RemoveField(
            model_name='video',
            name='memory',
        ),
        migrations.RemoveField(
            model_name='video',
            name='name',
        ),
        migrations.AlterField(
            model_name='video',
            name='video',
            field=models.FileField(upload_to='videos/'),
        ),
    ]
