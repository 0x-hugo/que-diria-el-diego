# Qué diria el diego [WIP]
Este script de Python utiliza el modelo GPT-3 de OpenAI para simular al 10.

## Cómo funciona

El script solicita una entrada al usuario con la frase "Pedile un consejo al Diegote". La entrada del usuario, junto con un contexto predefinido sobre el mas grande, se envía al modelo GPT-3. El modelo genera una respuesta que luego se imprime en la consola.

Además, la solicitud del usuario y la respuesta del modelo se guardan como un objeto JSON en el archivo history.txt.

## Configuración

Para ejecutar el script, necesitas tener Python 3 y el paquete openai de Python instalado. Puedes instalar el paquete usando pip:

```bash
pip install openai
```

También necesitas obtener una clave API de OpenAI y guardarla en un archivo config.py:

```python
# config.py
OPENAI_API_KEY = 'tu-api-key'
```

Reemplaza 'tu-api-key' con tu clave API real.

## Uso

Para ejecutar el script, usa el siguiente comando en tu terminal:

```bash
python main.py
```

Cuando se te solicite, introduce tu pregunta o solicitud de consejo. El asistente generará e imprimirá una respuesta.
