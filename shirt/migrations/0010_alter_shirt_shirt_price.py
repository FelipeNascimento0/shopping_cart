# Generated by Django 4.0.2 on 2022-04-05 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0009_alter_purchaseitems_purchase'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='shirt_price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
