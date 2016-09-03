from ..models import Battle, King
from .serializers import BattleSerializer, StatsSerializer
from got.response import JSONResponse
from rest_framework.views import APIView
from ..stats import Stats


class BattleListView(APIView):
    """
    API View for the /list endpoint
    """
    permission_classes = ()

    def get(self, request):
        batlles = BattleSerializer(instance=Battle.objects.all(), many=True).data
        return JSONResponse(batlles)


class BattleDetailView(APIView):
    """
    API View for the detail view of the battles /battles/<pk>
    """
    permission_classes = ()

    def get(self, request, pk):
        battle = BattleSerializer(instance=Battle.objects.get(id=pk)).data
        return JSONResponse(battle)


class BattleCountView(APIView):
    """
    API View for the count of all the records in the db /count
    """
    permission_classes = ()

    def get(self, request):
        count = Battle.objects.count()
        return JSONResponse(count)


class StatsView(APIView):
    """
    API View for the stats of all the data in the db /stats
    """
    permission_classes = ()

    def get(self, request):
        stat = StatsSerializer(instance=Stats()).data
        return JSONResponse(stat)


class SearchView(APIView):
    """
    API View for the search request using name, attacker_king, defender_king,
     location, type of battle /search
    """
    permission_classes = ()

    def get(self, request):
        name = request.query_params.get('name', None)
        type = request.query_params.get('type', None)
        location = request.query_params.get('location', None)
        attacker_king = request.query_params.get('attacker_king', None)
        defender_king = request.query_params.get('defender_king', None)
        if name:
            battle = BattleSerializer(instance=Battle.objects.get(name__iexact=name)).data
            return JSONResponse(battle)
        elif type:
            battle = BattleSerializer(instance=Battle.objects.filter(battle_type__iexact=type), many=True).data
            return JSONResponse(battle)
        elif location:
            battle = BattleSerializer(instance=Battle.objects.filter(location__iexact=location), many=True).data
            return JSONResponse(battle)
        elif attacker_king:
            king_object = King.objects.get(name__iexact=attacker_king)
            battle = BattleSerializer(instance=Battle.objects.filter(attacker_king=king_object), many=True).data
            return JSONResponse(battle)
        elif defender_king:
            king_object = King.objects.get(name__iexact=defender_king)
            battle = BattleSerializer(instance=Battle.objects.filter(defender_king=king_object), many=True).data
            return JSONResponse(battle)
        else:
            return JSONResponse(name)
