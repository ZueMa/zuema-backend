# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('buyers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='buyer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buyers.Buyer'),
        ),
        migrations.AddField(
            model_name='cart',
            name='items',
            field=models.ManyToManyField(through='buyers.ProductCart', to='products.Product'),
        ),
    ]