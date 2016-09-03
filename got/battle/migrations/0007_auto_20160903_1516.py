# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('battle', '0006_auto_20160903_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='battle',
            name='battle_number',
            field=models.PositiveIntegerField(db_index=True),
        ),
    ]
