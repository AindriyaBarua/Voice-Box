# Generated by Django 2.0.13 on 2019-04-17 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hashtag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hashtag',
            name='hid',
            field=models.IntegerField(),
        ),
    ]