import requests
import json
import os

"""
Direct OpenRouter API call for text correction using Gemma 3 27B model.
Configuration loaded from JSON file.
"""

def load_config():
    """
    Load configuration from config.json file.
    """
    try:
        config_path = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        raise Exception("config.json file not found")
    except json.JSONDecodeError:
        raise Exception("Invalid JSON format in config.json")

# Load configuration
config = load_config()

# Example text to correct
cuerpo_ejemplo = """
Este es un ejemplo de texto periodístico que necesita corrección.Faltan espacios después del punto,también hay hashtags como #noticia que deben eliminarse.

El autor Juan Pérez escribió esta nota con algunos errores de formateo    y espacios extras.
"""

# Prompt for text correction
# prompt_text = f"""Corrige el siguiente texto periodístico, revisando por ejemplo la correcta cantidad de espacios después de puntos y comas. 
# En el caso de detectar que los nombres propios corresponden al autor de la nota, eliminarlos. 
# También eliminar hashtags y errores que puedan estar originados en la captura del texto mediante scrapping: 

# {cuerpo_ejemplo}"""

# Prompt for text detection of entities and quotes
prompt_text = f"""Detecta entidades y citas en el siguiente texto: {cuerpo_ejemplo}"""

# Make the API call
response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {config['openrouter_api_key']}",
    "Content-Type": "application/json",
    "HTTP-Referer": config.get('site_url', ''),
    "X-Title": config.get('site_name', ''),
  },
  data=json.dumps({
    "model": config.get('model', 'google/gemma-3-27b-it:free'),
    "messages": [
      {
        "role": "user",
        "content": prompt_text
      }
    ],
    "temperature": config.get('temperature', 0.1),
    "top_p": config.get('top_p', 0.9),
    "max_tokens": config.get('max_tokens', 1000)
  })
)

# Process the response
if response.status_code == 200:
    result = response.json()
    if 'choices' in result and len(result['choices']) > 0:
        corrected_text = result['choices'][0]['message']['content']
        print("Texto corregido:")
        print(corrected_text)
    else:
        print("No se pudo obtener respuesta del modelo")
else:
    print(f"Error en la API: {response.status_code} - {response.text}")