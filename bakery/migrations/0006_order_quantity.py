# Generated by Django 3.1.7 on 2021-02-26 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0005_auto_20210226_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
