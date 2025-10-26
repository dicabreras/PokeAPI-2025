# pokedex_app/views.py

from django.shortcuts import render
# Importamos todas las funciones de servicio
from .pokeapi_service import (
    get_pokemon_data, 
    filter_by_weight, 
    filter_by_type, 
    filter_by_type_and_height, 
    add_new_column,
    format_pokemon_for_view # Importamos el formateador final
)

# ----------------- VISTA DE LA TABLA GENERAL -----------------
def pokedex_view(request):
    """
    Vista principal: Muestra la tabla general (los primeros 50).
    """
    # 1. Obtener los datos (ahora con peso y altura numéricos)
    raw_pokemon_data = get_pokemon_data(limit=50) 
    
    # 2. Aplicar el Requisito 4: Añadir la nueva columna (Nombre Invertido)
    # ASUMIMOS que add_new_column ahora añade 'reversed_name'
    list_with_new_column = add_new_column(raw_pokemon_data)
    
    # 3. Formatear los datos para la presentación final (añadir 'kg', 'm', formatear tipos)
    pokemon_list = format_pokemon_for_view(list_with_new_column)

    context = {
        'page_title': "Pokedex - Top 50 (General)", 
        'pokemon_list': pokemon_list,
        
        # ✅ CORRECCIÓN A: Cabecera 'Clase de Peso' reemplazada por 'Nombre Invertido'
        'column_headers': ['ID', 'Nombre', 'Nombre Invertido', 'Tipo(s)', 'Altura', 'Peso'] 
    }
    
    return render(request, 'pokedex_app/pokedex_table.html', context)


# ----------------- VISTA DE TABLAS FILTRADAS -----------------
def filtered_tables_view(request):
    """
    Vista que aplica todos los filtros y renderiza las tres tablas.
    """
    # 1. Obtener la fuente de datos bruta una sola vez (eficiencia)
    raw_data = get_pokemon_data(limit=50)

    # --- REQUISITO 1: Peso entre 30 y 80 kg ---
    # Parámetros: 30.0 < peso < 80.0
    filtered_1_raw = filter_by_weight(raw_data, 30.0, 80.0)
    # Formatear y añadir la nueva columna para la vista
    table_1 = format_pokemon_for_view(add_new_column(filtered_1_raw))

    # --- REQUISITO 2: Tipo 'Grass' ---
    filtered_2_raw = filter_by_type(raw_data, 'grass')
    table_2 = format_pokemon_for_view(add_new_column(filtered_2_raw))

    # --- REQUISITO 3: Tipo 'Flying' y Altura > 1.0 metro (10 dm) ---
    # Altura > 1.0 m
    filtered_3_raw = filter_by_type_and_height(raw_data, 'flying', 1.0)
    table_3 = format_pokemon_for_view(add_new_column(filtered_3_raw))
    
    # ✅ CORRECCIÓN B: Cabeceras para todas las tablas deben usar 'Nombre Invertido'
    headers = ['ID', 'Nombre', 'Nombre Invertido', 'Tipo(s)', 'Altura', 'Peso'] 

    context = {
        'page_title': "Pokedex - Tablas Filtradas",
        'headers': headers,
        'table_data': [
            {'title': '1. Peso entre 30.0 y 80.0 kg', 'list': table_1},
            {'title': '2. Tipo Grass', 'list': table_2},
            {'title': '3. Tipo Flying y Altura > 1.0 m', 'list': table_3},
        ]
    }
    
    return render(request, 'pokedex_app/filtered_tables.html', context)