# Mapa de México 🇲🇽

Aplicación web interactiva para visualizar y explorar los 32 estados y más de 2,400 municipios de México en un mapa.

## Características

- 🗺️ Mapa interactivo con Folium
- 🔍 Búsqueda directa de estados y municipios
- 📍 Marcadores con coordenadas precisas
- 🏛️ Selección por estado y municipio
- 📱 Diseño responsivo

## Instalación y ejecución

```bash
git clone https://github.com/saulsantibanezm/mapa-mexico.git
cd mapa-mexico
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python -m uvicorn main:app --reload
