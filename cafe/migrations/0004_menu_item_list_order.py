# Generated by Django 3.2.13 on 2023-05-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0003_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_item',
            name='list_order',
            field=models.IntegerField(default=0),
        ),
    ]
