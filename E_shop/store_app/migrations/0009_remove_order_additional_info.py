# Generated by Django 5.1.3 on 2025-02-27 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0008_order_paid_order_payment_id_alter_order_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='additional_info',
        ),
    ]
