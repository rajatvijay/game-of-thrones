# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0005_auto_20160903_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='attacker_king',
            field=models.ForeignKey(related_name='attacked_battles', blank=True, to='battle.King', null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='defender_king',
            field=models.ForeignKey(related_name='defended_battles', blank=True, to='battle.King', null=True),
        ),
    ]
