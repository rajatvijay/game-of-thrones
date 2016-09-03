# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0002_auto_20160903_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle',
            name='defender_size',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='attacker_size',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='battle_number',
            field=models.PositiveIntegerField(db_index=True, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='battle_type',
            field=models.CharField(blank=True, max_length=20, choices=[(b'pitched_battle', b'PITCHED BATTLE'), (b'ambush', b'AMBUSH'), (b'siege', b'SIEGE'), (b'razing', b'RAZING')]),
        ),
        migrations.AlterField(
            model_name='battle',
            name='location',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='name',
            field=models.CharField(max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='note',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='region',
            field=models.CharField(blank=True, max_length=20, choices=[(b'westerlands', b'The Westerlands'), (b'riverlands', b'The Riverlands'), (b'north', b'The North'), (b'crownlands', b'The Crownlands'), (b'beyondwall', b'Beyond the Wall'), (b'reach', b'The Reach'), (b'stormlands', b'The Stormlands')]),
        ),
        migrations.AlterField(
            model_name='battle',
            name='winner',
            field=models.CharField(blank=True, max_length=20, choices=[(b'attacker', b'ATTACKER'), (b'defender', b'DEFENDER')]),
        ),
        migrations.AlterField(
            model_name='battle',
            name='year',
            field=models.PositiveIntegerField(db_index=True, null=True, blank=True),
        ),
    ]
