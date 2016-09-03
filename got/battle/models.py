from django.db import models


class King(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Commander(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Battle(models.Model):
    WINNER_CHOICES = (('attacker', 'ATTACKER'),
                      ('defender', 'DEFENDER'))

    BATTLE_TYPE_CHOICES = (('pitched_battle', 'PITCHED BATTLE'),
                           ('ambush', 'AMBUSH'),
                           ('siege', 'SIEGE'),
                           ('razing', 'RAZING'))

    REGION_CHOICES = (('westerlands', 'The Westerlands'),
                      ('riverlands', 'The Riverlands'),
                      ('north', 'The North'),
                      ('crownlands', 'The Crownlands'),
                      ('beyondwall', 'Beyond the Wall'),
                      ('reach', 'The Reach'),
                      ('stormlands', 'The Stormlands'))

    name = models.CharField(max_length=20, blank=True)
    year = models.PositiveIntegerField(db_index=True, null=True, blank=True)
    battle_number = models.PositiveIntegerField(db_index=True, unique=True)
    winner = models.CharField(choices=WINNER_CHOICES, max_length=20, blank=True)
    battle_type = models.CharField(choices=BATTLE_TYPE_CHOICES, max_length=20, blank=True)
    major_death = models.NullBooleanField()
    major_capture = models.NullBooleanField()
    attacker_size = models.PositiveIntegerField(null=True, blank=True)
    defender_size = models.PositiveIntegerField(null=True, blank=True)
    summer = models.NullBooleanField()
    location = models.CharField(max_length=20, blank=True)
    region = models.CharField(choices=REGION_CHOICES, max_length=20, blank=True)
    note = models.TextField(blank=True)

    attacker_king = models.ForeignKey(King, related_name='attacked_battles', null=True, blank=True)
    defender_king = models.ForeignKey(King, related_name='defended_battles', null=True, blank=True)

    attacker_commander = models.ManyToManyField(Commander, related_name='attacked_battles', blank=True)
    defender_commander = models.ManyToManyField(Commander, related_name='defended_battles', blank=True)

    def __str__(self):
        return 'Battle {0}-{1}'.format(self.battle_number, self.battle_type)
