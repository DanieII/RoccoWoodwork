# Generated by Django 4.2.3 on 2024-12-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_order_delivery_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_type',
            field=models.CharField(choices=[('Офис на куриер', 'Доставка до офис на куриер - Еконт'), ('Адрес на получател', 'Доставка до адрес на получател')], default='Офис на куриер', max_length=18, verbose_name='Начин на доставка'),
        ),
    ]
