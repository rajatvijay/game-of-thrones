# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Battle',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('year', models.PositiveIntegerField(db_index=True)),
                ('battle_number', models.PositiveIntegerField(db_index=True)),
                ('winner', models.CharField(max_length=10, choices=[(b'attacker', b'ATTACKER'), (b'defender', b'DEFENDER')])),
                ('battle_type', models.CharField(max_length=10, choices=[(b'pitched_battle', b'PITCHED BATTLE'), (b'ambush', b'AMBUSH'), (b'siege', b'SIEGE'), (b'razing', b'RAZING')])),
                ('major_death', models.NullBooleanField()),
                ('major_capture', models.NullBooleanField()),
                ('attacker_size', models.PositiveIntegerField()),
                ('summer', models.NullBooleanField()),
                ('location', models.CharField(max_length=20)),
                ('region', models.CharField(max_length=10, choices=[(b'westerlands', b'The Westerlands'), (b'riverlands', b'The Riverlands'), (b'north', b'The North'), (b'crownlands', b'The Crownlands'), (b'beyondwall', b'Beyond the Wall'), (b'reach', b'The Reach'), (b'stormlands', b'The Stormlands')])),
                ('note', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Commander',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='King',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='battle',
            name='attacker_commander',
            field=models.ManyToManyField(related_name='attacked_battles', to='battle.Commander'),
        ),
        migrations.AddField(
            model_name='battle',
            name='attacker_king',
            field=models.ForeignKey(related_name='attacked_battles', to='battle.King'),
        ),
        migrations.AddField(
            model_name='battle',
            name='defender_commander',
            field=models.ManyToManyField(related_name='defended_battles', to='battle.Commander'),
        ),
        migrations.AddField(
            model_name='battle',
            name='defender_king',
            field=models.ForeignKey(related_name='defended_battles', to='battle.King'),
        ),
    ]
