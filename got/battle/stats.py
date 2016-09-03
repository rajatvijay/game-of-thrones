from .models import Battle, King
from django.db.models import Min, Count


class Stats:
    """
    Class to represent the stats of all the battles
    """
    def __init__(self):
        self.battle_type = self._get_types_of_battles()
        self.battles_won, self.battles_lost = self._get_battles_stats()
        self.active_region = self._get_active_region()
        self.common_defender_size, self.lowest_defender, self.largest_defender = self._get_defender_stats()
        self.attacker_king, self.defender_king = self._get_active_kings()

    def _get_types_of_battles(self):
        """
        Query all the type of battles
        :return: list
        """
        type_of_battles = Battle.objects.order_by().values('battle_type').distinct()
        return [battle_type['battle_type'] for battle_type in type_of_battles if battle_type['battle_type']]

    def _get_battles_stats(self):
        """
        Query the no of battles won and lost
        :return: int, int
        """
        battles_won = Battle.objects.filter(winner='attacker').count()
        battles_lost = Battle.objects.filter(winner='defender').count()
        return battles_won, battles_lost

    def _get_active_region(self):
        """
        Query the region with max number of battles
        :return: string
        """
        return Battle.objects.values_list('region').annotate(region_count=Count('region')).order_by(
            '-region_count')[0][0]

    def _get_defender_stats(self):
        """
        Query the common lowest and largest no of defender
        :return: int, int, int
        """
        common_defender_size = Battle.objects.values_list('defender_size').annotate(defender_count=Count(
            'defender_size')).order_by('-defender_count')[0][0]
        lowest_defender_list = Battle.objects.filter().values_list('defender_size').annotate(Min(
            'defender_size')).order_by('defender_size')

        for it in range(len(lowest_defender_list)):
            print it, lowest_defender_list[it][0]
            if lowest_defender_list[it][0]:
                lowest_defender = lowest_defender_list[it][0]
                break
        for it in range(len(lowest_defender_list)-1, 0, -1):
            print it, lowest_defender_list[it][0]
            if lowest_defender_list[it][0]:
                largest_defender = lowest_defender_list[it][0]
                break

        return common_defender_size, lowest_defender, largest_defender

    def _get_active_kings(self):
        """
        Query the kings with the max no of battles
        :return: string, string
        """
        active_attacker_king_id = Battle.objects.values_list('attacker_king').annotate(
            king_count=Count('attacker_king')).order_by('-king_count')[0][0]
        active_defender_king_id = Battle.objects.values_list('defender_king').annotate(
            king_count=Count('defender_king')).order_by('-king_count')[0][0]

        attacker_king = King.objects.get(id=active_attacker_king_id).name
        defender_king = King.objects.get(id=active_defender_king_id).name

        return attacker_king, defender_king
