from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from poetry.views import lovePoems

urlpatterns=[
    path('', views.index, name='index'),
    path('lovePoems', views.lovePoems, name='lovePoems'),
]