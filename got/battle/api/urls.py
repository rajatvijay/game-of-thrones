from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^battles/list$', views.BattleListView.as_view(), name='battle_list'),
    url(r'^battles/(?P<pk>\d+)/$', views.BattleDetailView.as_view(), name='battle_detail'),
    url(r'^battles/count$', views.BattleCountView.as_view(), name='battle_count'),
    url(r'^battles/stat$', views.StatView.as_view(), name='battle_stat'),

]