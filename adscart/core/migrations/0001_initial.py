# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-25 13:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.FloatField(blank=True)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('category', models.CharField(choices=[('Shirt', 'Shirt'), ('Sport wear', 'Sport wear'), ('Outwear', 'Outwear')], max_length=20)),
                ('lable', models.CharField(choices=[('Primary', 'primary'), ('Secondary', 'secondary'), ('Danger', 'danger')], max_length=20)),
                ('item_sale_type', models.CharField(choices=[('NEW', 'NEW'), ('Bestseller', 'Bestseller')], max_length=11)),
                ('slug', models.SlugField(max_length=200)),
                ('Description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='core.Item')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='items',
            field=models.ManyToManyField(to='core.order_item'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
