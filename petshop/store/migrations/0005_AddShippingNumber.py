# Generated by Django 4.2.6 on 2023-11-01 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_AddOrderDate1'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_number',
            field=models.IntegerField(blank=True, db_index=True, null=True),
        ),
    ]