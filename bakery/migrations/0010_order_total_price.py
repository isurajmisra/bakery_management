# Generated by Django 3.1.7 on 2021-02-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0009_auto_20210226_1743'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0, null=True),
        ),
    ]
