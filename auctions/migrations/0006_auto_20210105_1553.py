# Generated by Django 3.1.1 on 2021-01-05 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210105_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(choices=[('CL', 'Clothing')], default='Other', max_length=225),
        ),
    ]