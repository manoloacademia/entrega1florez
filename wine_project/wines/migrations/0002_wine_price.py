# Generated by Django 3.2.5 on 2022-08-06 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wines', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wine',
            name='price',
            field=models.FloatField(default=0),
        ),
    ]