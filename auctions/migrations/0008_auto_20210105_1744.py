# Generated by Django 3.1.1 on 2021-01-05 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20210105_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(default='Other', max_length=225),
        ),
    ]
