from django.contrib import admin
from .models import King, Commander, Battle


@admin.register(King)
class KingAdmin(admin.ModelAdmin):
    pass


@admin.register(Commander)
class CommanderAdmin(admin.ModelAdmin):
    pass


@admin.register(Battle)
class BattleAdmin(admin.ModelAdmin):
    pass
