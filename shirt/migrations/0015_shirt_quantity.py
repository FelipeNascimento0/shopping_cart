# Generated by Django 4.0.2 on 2022-04-13 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0014_alter_purchaseitems_shirt'),
    ]

    operations = [
        migrations.AddField(
            model_name='shirt',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
