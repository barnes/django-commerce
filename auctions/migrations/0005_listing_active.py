# Generated by Django 3.2.5 on 2021-07-08 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_rename_desc_listing_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
