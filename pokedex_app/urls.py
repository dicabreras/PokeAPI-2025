# pokedex_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # Mapea la URL raíz de la app ('/') a la función pokedex_view
    path('', views.pokedex_view, name='pokedex_table'), 
    
    # Vista para las tablas de filtros (NUEVA)
    path('filtros/', views.filtered_tables_view, name='filtered_tables'),
]