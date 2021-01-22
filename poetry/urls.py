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
    path('angerPoems', views.lovePoems, name='angerPoems'),
    path('christianPoems', views.lovePoems, name='christianPoems'),
    path('coronavirusPoems', views.lovePoems, name='coronavirusPoems'),
    path('deathPoems', views.lovePoems, name='deathPoems'),
    path('familyPoems', views.lovePoems, name='familyPoems'),
    path('friendshipPoems', views.lovePoems, name='friendshipPoems'),
    path('holidayPoems', views.lovePoems, name='holidayPoems'),
    path('lifePoems', views.lovePoems, name='lifePoems'),
    path('naturePoems', views.lovePoems, name='lifePoems'),
    path('sadPoems', views.lovePoems, name='sadPoems'),
    path('spiritualPoems', views.lovePoems, name='spiritualPoems'),
    # path('spiritualPoems', views.lovePoems, name='spiritualPoems'),

]