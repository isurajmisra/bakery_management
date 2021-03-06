# Generated by Django 3.1.7 on 2021-02-26 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bakery', '0007_auto_20210226_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='products',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='billNo',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='total_quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_products', to='bakery.order')),
                ('product', models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='bakery.product')),
            ],
            options={
                'db_table': 'product_order',
            },
        ),
    ]
