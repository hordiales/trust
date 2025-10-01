# OpenRouter LLM Text Processor

Este proyecto utiliza la API de OpenRouter para procesar texto con el modelo Gemma 3 27B de Google.

## Configuración

### 1. Obtener API Key de OpenRouter

1. Ve a https://openrouter.ai/google/gemma-3-27b-it:free/api
2. Haz clic en el botón **"Create API Key"**
3. Sigue las instrucciones para crear tu cuenta y generar la clave API
4. Copia la API key que se genere (comienza con `sk-or-v1-`)

### 2. Configurar config.json

Completa el archivo `config.json` con los siguientes valores:

```json
{
  "openrouter_api_key": "sk-or-v1-TU_API_KEY_AQUI",
  "model": "google/gemma-3-27b-it:free",
  "site_url": "https://tu-sitio-web.com",
  "site_name": "Nombre de tu aplicación",
  "temperature": 0.1,
  "top_p": 0.9,
  "max_tokens": 1000,
  "timeout": 30
}
```

#### Campos requeridos:
- **`openrouter_api_key`**: Tu clave API de OpenRouter (obligatorio)

#### Campos opcionales:
- **`site_url`**: URL de tu sitio web (para rankings en openrouter.ai)
- **`site_name`**: Nombre de tu aplicación (para rankings en openrouter.ai)
- **`temperature`**: Controla la creatividad del modelo (0.0-1.0, default: 0.1)
- **`top_p`**: Limita las opciones de generación (0.0-1.0, default: 0.9)
- **`max_tokens`**: Máximo número de tokens a generar (default: 1000)
- **`timeout`**: Tiempo límite para la petición en segundos (default: 30)

## Uso

### Ejecutar el script directamente:
```bash
python call-gemma-llm.py
```

### Usar como función Lambda (AWS):
El archivo `lambda_function.py` contiene la implementación para AWS Lambda que acepta eventos con el campo `cuerpo`.

## Archivos

- **`call-gemma-llm.py`**: Script directo para llamar a la API
- **`lambda_function.py`**: Implementación para AWS Lambda
- **`config.json`**: Archivo de configuración (completa con tu API key)
- **`README.md`**: Este archivo de documentación

## Modelo utilizado

- **Modelo**: `google/gemma-3-27b-it:free`
- **Proveedor**: Google via OpenRouter
- **Costo**: Gratuito
- **Capacidades**: Procesamiento de texto, detección de entidades, corrección