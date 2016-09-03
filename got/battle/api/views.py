from rest_framework import generics
from ..models import Battle
from .serializers import BattleSerializer, StatSerializer
from got.response import JSONResponse
from rest_framework.views import APIView
from ..stats import Stats


class BattleListView(generics.ListAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


class BattleDetailView(generics.RetrieveAPIView):
    queryset = Battle.objects.all()
    serializer_class = BattleSerializer


# class BattleDetailView(APIView):
#     permission_classes = ()
#
#     def get(self, request, pk):
#         battle = BattleSerializer(instance=Battle.objects.get(id=pk))
#         return JSONResponse(battle)
#

class BattleCountView(APIView):
    permission_classes = ()

    def get(self, request):
        count = Battle.objects.count()
        return JSONResponse(count)

class StatView(APIView):
    permission_classes = ()

    def get(self, request):
        stat = StatSerializer(instance=Stats()).data
        return JSONResponse(stat)