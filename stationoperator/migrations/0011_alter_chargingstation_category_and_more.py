# Generated by Django 5.0 on 2024-09-20 19:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stationoperator', '0010_rename_category_chargingstation_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chargingstation',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='stationoperator.category'),
        ),
        migrations.AlterField(
            model_name='chargingstation',
            name='slot_status',
            field=models.CharField(choices=[('disabled', 'Disabled'), ('in_review', 'in Review'), ('rejected', 'Rejected'), ('published', 'Published'), ('draft', 'Draft')], default='in_review', max_length=10),
        ),
        migrations.AlterField(
            model_name='stationreview',
            name='rating',
            field=models.IntegerField(choices=[(4, '⭐⭐⭐⭐☆'), (3, '⭐⭐⭐☆☆'), (1, '⭐☆☆☆☆'), (2, '⭐⭐☆☆☆'), (5, '⭐⭐⭐⭐⭐')], default=None),
        ),
    ]
