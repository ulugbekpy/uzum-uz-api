# Generated by Django 4.1.7 on 2023-03-18 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_remove_customer_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='123123', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='seller',
            name='phone',
            field=models.CharField(default='321321', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
