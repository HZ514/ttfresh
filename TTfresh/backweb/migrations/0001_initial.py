# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 13:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_num', models.IntegerField(default=1)),
                ('c_prices', models.FloatField(default=0)),
                ('is_select', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'tt_cart',
            },
        ),
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_img', models.CharField(max_length=200)),
                ('typeid', models.CharField(max_length=16)),
                ('typename', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'tt_foodtypes',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productid', models.CharField(max_length=16, unique=True)),
                ('productimg', models.CharField(max_length=200)),
                ('productname', models.CharField(max_length=100)),
                ('pmdesc', models.CharField(max_length=100)),
                ('is_new', models.BooleanField(default=False)),
                ('price', models.FloatField(default=0)),
                ('one_weight', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=255)),
                ('goods_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.FoodType')),
            ],
            options={
                'db_table': 'tt_goods',
            },
        ),
        migrations.CreateModel(
            name='MainSide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('trackid', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'tt_side',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(max_length=255)),
                ('order_status', models.IntegerField(default=0)),
                ('order_time', models.DateTimeField(auto_now=True)),
                ('o_prices', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
                ('userinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserReceivInfo')),
            ],
            options={
                'db_table': 'tt_oder',
            },
        ),
        migrations.CreateModel(
            name='OrderGoodsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods_price', models.FloatField(default=0)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.Order')),
            ],
            options={
                'db_table': 'tt_order_goods',
            },
        ),
        migrations.CreateModel(
            name='TypeRecommend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommend_name', models.CharField(max_length=30)),
                ('type_recommend', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.FoodType')),
            ],
            options={
                'db_table': 'tt_typerecommend',
            },
        ),
        migrations.CreateModel(
            name='UserBrowse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browse_time', models.DateTimeField(auto_now=True)),
                ('good', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.Goods')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'db_table': 'tt_userbrowse',
            },
        ),
        migrations.AddField(
            model_name='cart',
            name='goods',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backweb.Goods'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User'),
        ),
    ]
