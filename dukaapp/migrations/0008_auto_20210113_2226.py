# Generated by Django 3.1.3 on 2021-01-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dukaapp', '0007_auto_20210113_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='phone_no',
            field=models.CharField(max_length=100),
        ),
    ]