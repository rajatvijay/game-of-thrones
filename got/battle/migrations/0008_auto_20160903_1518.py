# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0007_auto_20160903_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='attacker_commander',
            field=models.ManyToManyField(related_name='attacked_battles', to='battle.Commander', blank=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='defender_commander',
            field=models.ManyToManyField(related_name='defended_battles', to='battle.Commander', blank=True),
        ),
    ]
