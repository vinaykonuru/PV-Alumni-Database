# Generated by Django 3.0.8 on 2020-07-12 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20200711_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='closing_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 12, 0, 6, 9, 906697)),
        ),
    ]