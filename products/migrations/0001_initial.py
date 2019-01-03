# Generated by Django 2.1.4 on 2019-01-03 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('price', models.IntegerField()),
                ('discount', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('days', models.IntegerField()),
            ],
        ),
    ]
