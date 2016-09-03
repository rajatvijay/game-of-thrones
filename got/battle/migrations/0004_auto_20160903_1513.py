# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0003_auto_20160903_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='attacker_commander',
            field=models.ManyToManyField(related_name='attacked_battles', null=True, to='battle.Commander'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='attacker_king',
            field=models.ForeignKey(related_name='attacked_battles', to='battle.King', null=True),
        ),
        migrations.AlterField(
            model_name='battle',
            name='defender_commander',
            field=models.ManyToManyField(related_name='defended_battles', null=True, to='battle.Commander'),
        ),
        migrations.AlterField(
            model_name='battle',
            name='defender_king',
            field=models.ForeignKey(related_name='defended_battles', to='battle.King', null=True),
        ),
    ]
