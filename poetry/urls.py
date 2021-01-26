from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from poetry.views import lovePoems,angerPoems,christianPoems,coronavirusPoems,deathPoems,familyPoems,friendshipPoems,holidayPoems,lifePoems,naturePoems,sadPoems,spiritualPoems
from poetry.views import lovePoems_entry,angerPoems_entry,christianPoems_entry,coronavirusPoems_entry,deathPoems_entry,familyPoems_entry,friendshipPoems_entry,holidayPoems_entry,lifePoems_entry,naturePoems_entry,sadPoems_entry,spiritualPoems_entry


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
    path('angerPoems_entry', views.angerPoems_entry, name='angerPoems_entry'),
    path('christianPoems_entry', views.christianPoems_entry, name='christianPoems_entry'),
    path('coronavirusPoems_entry', views.coronavirusPoems_entry, name='coronavirusPoems_entry'),
    path('deathPoems_entry', views.deathPoems_entry, name='deathPoems_entry'),
    path('familyPoems_entry', views.familyPoems_entry, name='familyPoems_entry'),
    path('friendshipPoems_entry', views.friendshipPoems_entry, name='friendshipPoems_entry'),
    path('holidayPoems_entry', views.holidayPoems_entry, name='holidayPoems_entry'),
    path('lifePoems_entry', views.lifePoems_entry, name='lifePoems_entry'),
    path('naturePoems_entry', views.naturePoems_entry, name='naturePoems_entry'),
    path('sadPoems_entry', views.sadPoems_entry, name='sadPoems_entry'),
    path('spiritualPoems_entry', views.spiritualPoems_entry, name='spiritualPoems_entry'),
    # path('lovePoems_entry', views.lovePoems_entry, name='lovePoems_entry'),


]