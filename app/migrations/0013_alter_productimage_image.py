# Generated by Django 4.1.7 on 2023-03-27 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_shop_seller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='products/'),
        ),
    ]
