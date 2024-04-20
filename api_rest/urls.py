from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.get_produtos, name='get_all_produtos'),
    path('produto/<int:id>', views.get_id),
    path('data/', views.produto_manager)
]
