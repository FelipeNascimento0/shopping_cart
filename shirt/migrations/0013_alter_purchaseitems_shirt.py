# Generated by Django 4.0.2 on 2022-04-10 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shirt', '0012_alter_shirt_shirt_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitems',
            name='shirt',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='shirt.shirt'),
        ),
    ]
