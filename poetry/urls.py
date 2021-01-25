from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from poetry.views import lovePoems,angerPoems,christianPoems,coronavirusPoems,deathPoems,familyPoems,friendshipPoems,holidayPoems,lifePoems,naturePoems,sadPoems,spiritualPoems



urlpatterns=[
    path('', views.index, name='index'),
    path('lovePoems', views.lovePoems, name='lovePoems'),
    path('angerPoems', views.angerPoems, name='angerPoems'),
    path('christianPoems', views.christianPoems, name='christianPoems'),
    path('coronavirusPoems', views.coronavirusPoems, name='coronavirusPoems'),
    path('deathPoems', views.deathPoems, name='deathPoems'),
    path('familyPoems', views.familyPoems, name='familyPoems'),
    path('friendshipPoems', views.friendshipPoems, name='friendshipPoems'),
    path('holidayPoems', views.holidayPoems, name='holidayPoems'),
    path('lifePoems', views.lifePoems, name='lifePoems'),
    path('naturePoems', views.naturePoems, name='naturePoems'),
    path('sadPoems', views.sadPoems, name='sadPoems'),
    path('spiritualPoems', views.spiritualPoems, name='spiritualPoems'),
    # path('spiritualPoems', views.lovePoems, name='spiritualPoems'),

    path('lovePoems_entry', views.lovePoems_entry, name='lovePoems_entry'),

]