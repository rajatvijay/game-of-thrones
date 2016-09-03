from rest_framework import serializers
from battle.models import Battle, King, Commander


class CommanderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commander
        fields = ('name',)


class BattleSerializer(serializers.ModelSerializer):
    attacker_commander = CommanderSerializer(many=True, read_only=True)
    defender_commander = CommanderSerializer(many=True, read_only=True)
    attacker_king = serializers.CharField(source='attacker_king.name', read_only=True)
    defender_king = serializers.CharField(source='defender_king.name', read_only=True)

    class Meta:
        model = Battle
        fields = ('name',
                   'battle_number',
                   'year',
                   'winner',
                   'battle_type',
                   'region',
                   'attacker_commander',
                   'defender_commander',
                   'location',
                   'attacker_king',
                  'defender_king')


class StatSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        return {
           "most_active": {
              "attacker_king": instance.attacker_king,
              "defender_king": instance.defender_king,
              "region": instance.active_region,
              "name": ""
           },
           "attacker_outcome": {
              "win": instance.battles_won,
              "loss": instance.battles_lost
           },
           "battle_type": instance.battle_type,
           "defender_size": {
              "average": instance.common_defender_size,
              "min": instance.lowest_defender,
              "max": instance.largest_defender
           }
        }
