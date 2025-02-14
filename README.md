# ModeladoIA
Modelado de Amenazas con IA

API Threat Modeling - PoC

Este proyecto implementa una API para el análisis de amenazas utilizando el modelo STRIDE y la evaluación DREAD. Proporciona una herramienta para identificar amenazas potenciales, mitigar riesgos y analizar posibles vectores de ataque en sistemas de software.

🚀 Requisitos Previos

Python 3.11 o superior

Entorno virtual configurado (recomendado)

Dependencias necesarias:

fastapi

uvicorn

pydantic

transformers

tf-keras

🛠️ Instalación de Dependencias

# Crear y activar entorno virtual
python -m venv env
source env/Scripts/activate  # En Windows

# Instalar dependencias
pip install fastapi uvicorn pydantic transformers tf-keras

🖥️ Ejecución de la Aplicación

Ubicar el archivo api_threat_modeling.py en el directorio deseado.

Ejecutar el siguiente comando:

uvicorn api_threat_modeling:app --reload

Acceder a la interfaz interactiva de la API en:

http://localhost:8000/docs

🧪 Uso de la API

La API expone un único endpoint para analizar amenazas:

POST /analyze_threats/

Entrada esperada (JSON):

{
  "case_description": "Evaluar riesgos relacionados con Spoofing y Tampering en las comunicaciones",
  "system_architecture": "Arquitectura en microservicios",
  "critical_assets": "Base de datos de usuarios",
  "data_flows": "Transferencia de datos entre frontend y backend",
  "involved_actors": "Usuarios, administradores, servicios externos",
  "security_controls": "Autenticación multifactor, cifrado TLS"
}

Respuesta esperada (JSON):

[
  {
    "description": "Suplantación de identidad (Spoofing)",
    "mitigation": "Implementar autenticación multifactor.",
    "stride_category": "Spoofing",
    "dread_score": 7.5
  },
  {
    "description": "Manipulación de datos (Tampering)",
    "mitigation": "Usar firmas digitales y controles de integridad.",
    "stride_category": "Tampering",
    "dread_score": 6.8
  }
]

🛠️ Mecanismo de Detección de Amenazas

La aplicación utiliza el modelo STRIDE para clasificar las amenazas en las siguientes categorías:

S: Spoofing (Suplantación de identidad)

T: Tampering (Manipulación de datos)

R: Repudiation (Repudio)

I: Information Disclosure (Divulgación de información)

D: Denial of Service (Denegación de servicio)

E: Elevation of Privilege (Elevación de privilegios)

Cada amenaza es evaluada usando el modelo DREAD, asignando un puntaje entre 4.0 y 10.0.

🛑 Posibles Errores y Soluciones

1. ModuleNotFoundError: No module named 'fastapi'

Solución:

pip install fastapi uvicorn

2. RuntimeError: Failed to import transformers...

Solución:

pip install tf-keras

3. Internal Server Error con respuesta genérica

Verificar que los términos en case_description coincidan con las categorías del modelo STRIDE.

4. No matching distribution found for tensorflow

Asegúrate de tener una versión compatible de Python y usar pip install tf-keras.

