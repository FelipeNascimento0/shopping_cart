# Generated by Django 4.0.2 on 2022-04-06 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0010_alter_shirt_shirt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='shirt_price',
            field=models.FloatField(),
        ),
    ]
