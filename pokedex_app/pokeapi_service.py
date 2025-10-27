# pokedex_app/pokeapi_service.py

import requests # Library for making HTTP requests to the PokeAPI
from typing import List, Dict # This improves legibility of data type

POKEAPI_BASE_URL = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon_data(limit: int = 50) -> List[Dict]:   # Numero por default de pokemones a analizar;

    all_pokemon_details = []
    # 1. First request: Get the list of the first N = limit = 50 Pokemons (names and URLs)
    # We use 'offset' (where to start) and 'limit' (how many to get)
    try:
        response_list = requests.get(f"{POKEAPI_BASE_URL}?offset=0&limit={limit}") # Pide los primeros 50 pokemones
        response_list.raise_for_status() # Throws an exception for errors 4xx/5xx (HTTP errors)
        pokemon_list = response_list.json().get('results', []) # Convierte el archivo .json obtenido de la respuesta HTTP en un diccionario de Python y luego accede a los pokemones 
    except requests.exceptions.RequestException as e:
        # This handles red errors or HTTP errors
        print(f"Error al obtener la lista de Pokémon: {e}")
        return []
    
    # 2. Secondary requests: Obtain details about each Pokemon
    for idx, poke_summary in enumerate(pokemon_list):
        
        # El ID se calcula sumando 1 al índice porque la lista de la API empieza en 0
        pokemon_id = idx + 1
        
        try:
            # Usamos la URL individual que viene en la lista para obtener los detalles
            response_detail = requests.get(poke_summary['url'])  # URL individual de cada pokemon
            response_detail.raise_for_status()
            detail = response_detail.json()
            
            # 3. Procesamiento y Formateo del Dato (Paso crucial para la tabla)
            
            # Obtiene los tipos (puede ser 1 o 2) y los une en una sola cadena
            # Ejemplo: ['grass', 'poison'] -> "Grass, Poison"
            types = ", ".join([t['type']['name'].capitalize() for t in detail['types']])
            
            # Formatea la altura (decímetros) y el peso (hectogramos) para ser más legible
            # 10 dm = 1.0 m / 10 hg = 1.0 kg
            height_m = detail['height'] / 10.0 
            weight_kg = detail['weight'] / 10.0
            
            # Creamos una lista separada de los tipos para facilitar el filtrado
            type_list = [t['type']['name'] for t in detail['types']]
            
            # Objeto limpio para la vista
            pokemon_data = {
                'id': detail['id'],
                'name': detail['name'].capitalize(),
                'types': types,       # Cadena legible (ej: "Grass, Poison")
                'type_list': type_list, # Lista de tipos (ej: ['grass', 'poison']) - NUEVO
                'height': height_m,   # Valor numérico puro (m) - MODIFICADO
                'weight': weight_kg,   # Valor numérico puro (kg) - MODIFICADO
            }
            
            all_pokemon_details.append(pokemon_data)

        except requests.exceptions.RequestException as e:
            print(f"Error al obtener detalles del Pokémon ID {pokemon_id}: {e}")
            # Si falla uno, continuamos con el siguiente
            continue

    return all_pokemon_details

def filter_by_weight(pokemon_list: List[Dict], min_weight: float, max_weight: float) -> List[Dict]: 
    """
    Filtra Pokémon por un rango de peso (en kilogramos).
    """
    return [
        p for p in pokemon_list 
        if min_weight < p['weight'] < max_weight
    ]

def filter_by_type(pokemon_list: List[Dict], required_type: str) -> List[Dict]: # Filtrado por tipo específico
    """
    Filtra Pokémon que tienen un tipo específico.
    """
    required_type = required_type.lower()
    return [
        p for p in pokemon_list 
        if required_type in p['type_list']
    ]

def filter_by_type_and_height(pokemon_list: List[Dict], required_type: str, min_height: float) -> List[Dict]:  #En esta linea de codigo se filtra por los atributos especificados
    """
    Filtra Pokémon por tipo y una altura mínima (en metros).
    """
    required_type = required_type.lower()
    return [
        p for p in pokemon_list 
        if required_type in p['type_list'] and p['height'] > min_height
    ]

# --- FUNCIÓN DE NOMBRE INVERTIDO ---

def add_new_column(pokemon_list) -> List:
    """
    Añade la nueva columna 'Nombre Invertido' (reversed_name) a cada Pokémon.
    """
    processed_list = []
    for pokemon in pokemon_list:
        # Crea una copia mutable del diccionario.
        p = pokemon.copy() 
        
        # Calcular el Nombre Invertido
        original_name = p.get('name', '').lower()
        
        # Invertir el nombre y capitalizar la primera letra
        p['reversed_name'] = original_name[::-1].capitalize() 
        
        
        processed_list.append(p)
    return processed_list


def format_pokemon_for_view(pokemon_list) -> List:
    """
    Formatea los campos numéricos y de lista para su visualización en HTML.
    """
    formatted_list = []
    for pokemon in pokemon_list:
        p = pokemon.copy()
        
        # Formateo de unidades
        p['height'] = f"{p.get('height', 0):.1f} m"
        p['weight'] = f"{p.get('weight', 0):.1f} kg"
        
        # Formateo de tipos
        p['types'] = ", ".join([t.capitalize() for t in p.get('type_list', [])])
        
        formatted_list.append(p)
    return formatted_list


# Ejemplo de uso para depuración (opcional, pero útil)
if __name__ == '__main__':
    data = get_pokemon_data(5)
    #print(data)
    
