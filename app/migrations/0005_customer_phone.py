# Generated by Django 4.1.7 on 2023-03-17 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_user_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(default='2170900', max_length=20, unique=True),
            preserve_default=False,
        ),
    ]
