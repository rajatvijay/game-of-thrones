import csv
from .models import King, Commander, Battle


class BattleIngestion:
    def __init__(self, file_path):
        self.file = file_path

    def ingest_battles(self):
        with open(self.file, 'rU') as csvfile:
            reader = csv.reader(csvfile)
            for row_number, row_values in enumerate(reader):
                if row_number != 0:
                    for index, field in enumerate(row_values):
                        attacker = []
                        defender = []
                        if index == 0:
                            battle_name = str(field)
                        elif index == 1:
                            battle_year = self._parse_int_field(field=field)
                        elif index == 2:
                            battle_number = self._parse_int_field(field=field)
                        elif index == 3:
                            attacker_king = str(field)
                        elif index == 4:
                            defender_king = str(field)
                        elif index == 5 or index == 6 or index == 7 or index == 8:
                            attacker.append(str(field))
                            attacker.append(str(field))
                            attacker.append(str(field))
                            attacker.append(str(field))
                        elif index == 9 or index == 10 or index == 11 or index == 12:
                            defender.append(str(field))
                            defender.append(str(field))
                            defender.append(str(field))
                            defender.append(str(field))
                        elif index == 13:
                            attacker_outcome = str(field)
                        elif index == 14:
                            battle_type = str(field)
                        elif index == 15:
                            major_death = self._parse_int_field(field=field)
                        elif index == 16:
                            major_capture = self._parse_int_field(field=field)
                        elif index == 17:
                            attacker_size = self._parse_int_field(field=field)
                        elif index == 18:
                            defender_size = self._parse_int_field(field=field)
                        elif index == 19:
                            attacker_commander = str(field)
                        elif index == 20:
                            defender_commander = str(field)
                        elif index == 21:
                            summer = self._parse_int_field(field=field)
                        elif index == 22:
                            location = str(field)
                        elif index == 23:
                            region = str(field)
                        elif index == 24:
                            note = str(field)
                        else:
                            raise ValueError('Extra col found'.upper())

                    attacker_king = self._get_king(king_name=attacker_king)
                    defender_king = self._get_king(king_name=defender_king)
                    battle_winner = self._parse_winner(outcome=attacker_outcome)

                    print('major death = {0}, major capture = {1}, summer = {2}'.format(major_capture,
                                                                                        major_death,
                                                                                        summer).upper())

                    major_capture = self._parse_bool(number=major_capture)
                    major_death = self._parse_bool(number=major_death)
                    summer = self._parse_bool(number=summer)

                    print('major death = {0}, major capture = {1}, summer = {2}'.format(major_capture,
                                                                                        major_death,
                                                                                        summer).upper())
                    # raise ValueError('Stopped intentionally')

                    print('Attacker commander From file  = {}'.format(attacker_commander).upper())
                    attacker_commander = self._get_commaders(commanders_name=attacker_commander)

                    print('defender commander From file  = {}'.format(defender_commander).upper())
                    defender_commander = self._get_commaders(commanders_name=defender_commander)

                    self._add_battle(attacker_commander=attacker_commander,
                                     defender_commander=defender_commander,
                                     name=battle_name,
                                     year=battle_year,
                                     battle_number=battle_number,
                                     winner=battle_winner,
                                     battle_type=battle_type,
                                     major_death=major_death,
                                     major_capture=major_capture,
                                     attacker_size=attacker_size,
                                     defender_size=defender_size,
                                     summer=summer,
                                     location=location,
                                     region=region,
                                     note=note)

                    print('\n\n\n\n')

    def _get_king(self, king_name):
        king, is_new = King.objects.get_or_create(name=king_name)
        return king

    def _parse_winner(self, outcome):
        if outcome == 'win':
            return 'attacker'
        else:
            return 'defender'

    def _parse_bool(self, number):
        if number == 1:
            return True
        elif number == 0:
            return False
        else:
            return None

    def _get_commaders(self, commanders_name):
        commander = []
        commanders_name = commanders_name.split(', ')
        for commander_name in commanders_name:
            commander.append(Commander.objects.get_or_create(name=commander_name)[0])

        print('Commader list = {}'.format(commander).upper())
        return commander

    def _add_battle(self, attacker_commander, defender_commander, **kwargs):
        if not Battle.objects.filter(battle_number=kwargs['battle_number']).exists():
            battle = Battle.objects.create(**kwargs)
            print('inside add battle'.upper())
            print(attacker_commander)
            for commander in attacker_commander:
                battle.attacker_commander.add(commander)

            for commander in defender_commander:
                battle.defender_commander.add(commander)

            battle.save()
        else:
            print('Battle {} exists'.format(kwargs['battle_number']).upper())

    def _parse_int_field(self, field):
        if field == '':
            return None
        else:
            return int(field)