from rest_framework import serializers
from battle.models import Battle, King, Commander


class CommanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        include = ('name',)


class BattleSerializer(serializers.ModelSerializer):
    attacker_commander = CommanderSerializer(many=True, read_only=True)
    defender_commander = CommanderSerializer(many=True, read_only=True)

    class Meta:
        model = Battle
        include = ('name',
                   'battle_number',
                   'year',
                   'winner',
                   'battle_type',
                   'region',
                   'attacker_commander',
                   'defender_commander',
                   'location')
