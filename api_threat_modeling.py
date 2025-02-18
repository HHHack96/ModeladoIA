from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import random
from transformers import pipeline

app = FastAPI()

# Modelos para el input y output
class ThreatInput(BaseModel):
    case_description: str
    system_architecture: str
    critical_assets: str
    data_flows: str
    involved_actors: str
    security_controls: str

class Threat(BaseModel):
    description: str
    mitigation: str
    stride_category: str
    dread_score: float

# Cargar modelo de IA para análisis de texto
nlp = pipeline("sentiment-analysis")

# Catálogo básico de amenazas
THREATS = [
    {"description": "Suplantación de identidad (Spoofing)", "stride": "Spoofing", "mitigation": "Implementar autenticación multifactor."},
    {"description": "Manipulación de datos (Tampering)", "stride": "Tampering", "mitigation": "Usar firmas digitales y controles de integridad."},
    {"description": "Repudio (Repudiation)", "stride": "Repudiation", "mitigation": "Incorporar registros de auditoría inmutables."},
    {"description": "Divulgación de información (Information Disclosure)", "stride": "Information Disclosure", "mitigation": "Aplicar cifrado de extremo a extremo."},
    {"description": "Denegación de servicio (DoS)", "stride": "Denial of Service", "mitigation": "Implementar mecanismos de rate-limiting."},
    {"description": "Elevación de privilegios (Elevation of Privilege)", "stride": "Elevation of Privilege", "mitigation": "Aplicar controles estrictos de permisos."}
]

# Función para generar amenazas basadas en la descripción usando IA
def generate_threats(input_data: ThreatInput) -> List[Threat]:
    description = input_data.case_description
    analysis = nlp(description)
    sentiment_score = analysis[0]['score']

    threats_detected = []
    for threat in THREATS:
        if any(keyword in description.lower() for keyword in threat["stride"].lower().split()):
            dread_score = round(random.uniform(4.0, 10.0) + sentiment_score, 2)
            threats_detected.append(
                Threat(
                    description=threat["description"],
                    mitigation=threat["mitigation"],
                    stride_category=threat["stride"],
                    dread_score=dread_score
                )
            )
    return threats_detected if threats_detected else [
        Threat(
            description="Amenaza potencial no categorizada",
            mitigation="Revisar la configuración y el flujo del sistema manualmente.",
            stride_category="Desconocido",
            dread_score=5.0
        )
    ]

@app.post("/analyze_threats/", response_model=List[Threat])
def analyze_threats(input_data: ThreatInput):
    threats = generate_threats(input_data)
    return threats
    
    

# Instrucciones para ejecutar la API
# 1. Guardar este código en un archivo llamado api_threat_modeling.py
# 2. Instalar dependencias: pip install fastapi pydantic uvicorn transformers
# 3. Ejecutar: uvicorn api_threat_modeling:app --reload
# 4. Probar en http://localhost:8000/docs