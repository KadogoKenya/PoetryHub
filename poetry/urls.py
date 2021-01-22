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
]