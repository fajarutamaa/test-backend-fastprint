# Generated by Django 5.0 on 2023-12-11 05:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_produk_kategori_alter_produk_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produk',
            name='kategori',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='apps.kategori'),
        ),
        migrations.AlterField(
            model_name='produk',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='apps.status'),
        ),
    ]
