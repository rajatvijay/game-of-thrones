# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='battle_type',
            field=models.CharField(max_length=20, choices=[(b'pitched_battle', b'PITCHED BATTLE'), (b'ambush', b'AMBUSH'), (b'siege', b'SIEGE'), (b'razing', b'RAZING')]),
        ),
        migrations.AlterField(
            model_name='battle',
            name='note',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='region',
            field=models.CharField(max_length=20, choices=[(b'westerlands', b'The Westerlands'), (b'riverlands', b'The Riverlands'), (b'north', b'The North'), (b'crownlands', b'The Crownlands'), (b'beyondwall', b'Beyond the Wall'), (b'reach', b'The Reach'), (b'stormlands', b'The Stormlands')]),
        ),
        migrations.AlterField(
            model_name='battle',
            name='winner',
            field=models.CharField(max_length=20, choices=[(b'attacker', b'ATTACKER'), (b'defender', b'DEFENDER')]),
        ),
    ]
