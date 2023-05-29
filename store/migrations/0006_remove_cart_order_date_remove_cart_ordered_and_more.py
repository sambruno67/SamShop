# Generated by Django 4.2.1 on 2023-05-27 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='order_date',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='ordered',
        ),
        migrations.AddField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]