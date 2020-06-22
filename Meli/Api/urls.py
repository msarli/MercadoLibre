from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('mutant/', views.mutant,name='mutant'),
    path('stats/', views.stats,name='stats'),
    path('clearDB/', views.clearDB,name='clearDB'),
    path('list2/', views.list2,name='list2'),
]
