# Generated by Django 5.0 on 2024-09-19 12:59

import stationoperator.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0007_alter_chargingstation_slot_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='image',
            field=models.ImageField(default='product.jpg', upload_to=stationoperator.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('published', 'Published'), ('in_review', 'in Review'), ('rejected', 'Rejected'), ('draft', 'Draft'), ('disabled', 'Disabled')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='slotreservation',
            name='slot_status',
            field=models.CharField(choices=[('completed', 'Charging Completed'), ('reserved', 'Slot Reserved'), ('in_process', 'Booking in Process')], default='Booking in Process', max_length=30),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(5, '⭐⭐⭐⭐⭐'), (3, '⭐⭐⭐☆☆'), (4, '⭐⭐⭐⭐☆'), (2, '⭐⭐☆☆☆'), (1, '⭐☆☆☆☆')], default=None),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='image',
            field=models.ImageField(default='vendor.jpg', upload_to=stationoperator.models.user_directory_path),
        ),
    ]
