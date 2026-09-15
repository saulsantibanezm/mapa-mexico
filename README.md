# Mapa de México 🇲🇽

Aplicación web interactiva para visualizar y explorar los 32 estados y 2,478 municipios de México en un mapa.

## Características

- 🗺️ Mapa interactivo con Leaflet.js
- 🔍 Búsqueda directa de estados y municipios
- 📍 Marcadores con coordenadas precisas
- 🏛️ Selección jerárquica por estado y municipio
- 📱 Diseño responsivo

## Tecnologías

- **Backend:** Python, FastAPI, SQLite
- **Frontend:** HTML5, CSS3, JavaScript, Leaflet.js
- **Mapa base:** OpenStreetMap

## Instalación y ejecución

```bash
git clone https://github.com/saulsantibanezm/mapa-mexico.git
cd mapa-mexico
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python create_db.py
python -m uvicorn main:app --reload
```

Abre http://127.0.0.1:8000 en tu navegador.

## Versión extendida

Este repositorio es la versión base del proyecto. La versión con indicadores de lenguas indígenas del Censo INEGI 2020 está disponible en:
👉 https://github.com/saulsantibanezm/mapa-mexico-lom

## Autor

Saul Santibañez Molina — Servicio Social IIMAS, UNAM 2026
Supervisor: Dr. Ivan Vladimir Meza Ruiz
