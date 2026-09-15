# Mapa de México 🇲🇽

Aplicación web interactiva para visualizar y explorar los 32 estados y 2,478 municipios de México en un mapa. Desarrollado como proyecto de Servicio Social en el Instituto de Investigaciones en Matemáticas Aplicadas y en Sistemas (IIMAS), UNAM.

## Características

- 🗺️ Mapa interactivo con Leaflet.js
- 🔍 Búsqueda directa de estados y municipios
- 📍 Marcadores con coordenadas precisas
- 🏛️ Selección jerárquica por estado y municipio
- 🗑️ Eliminación individual o total de marcadores
- 📱 Diseño responsivo

## Requisitos

- Python 3.10 o superior → https://python.org/downloads
- En Windows: marcar "Add Python to PATH" durante la instalación


## Instalación y ejecución

### Linux y Mac

```bash
git clone https://github.com/saulsantibanezm/mapa-mexico.git
cd mapa-mexico
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python create_db.py
python -m uvicorn main:app --reload
```

### Windows

```bash
git clone https://github.com/saulsantibanezm/mapa-mexico.git
cd mapa-mexico
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python create_db.py
python -m uvicorn main:app --reload
```

Abre http://127.0.0.1:8000 en tu navegador.


## Estructura del proyecto

mapa-mexico/
├── main.py # Backend FastAPI (6 endpoints)
├── create_db.py # Genera la base de datos desde CSV
├── requirements.txt # Dependencias Python
├── coordenadas_municipios.csv # Datos geográficos de municipios
├── municipios.db # Base de datos SQLite
└── templates/
└── index.html # Interfaz web completa

## API disponible

| Endpoint | Descripción |
|---|---|
| GET / | Página principal |
| GET /api/estados | Lista de 32 estados |
| GET /api/estados/{id} | Detalle de un estado |
| GET /api/municipios/{estado_id} | Municipios de un estado |
| GET /api/municipios/detalle/{id} | Detalle de un municipio |
| GET /api/buscar | Búsqueda por texto |

## Fuente de datos

- **Coordenadas geográficas:** elaboración propia
- **Información geográfica:** 32 estados y 2,478 municipios de México

## Tecnologías

| Tecnología | Uso |
|---|---|
| Python | Lógica general del sistema |
| FastAPI | Backend con endpoints REST |
| SQLite | Base de datos relacional |
| Leaflet.js | Mapa interactivo |
| HTML5/CSS3/JS | Interfaz de usuario |
| OpenStreetMap | Proveedor de tiles del mapa base |

## Versión extendida

Este repositorio es la versión base del proyecto. La versión con indicadores de lenguas indígenas del Censo INEGI 2020 está disponible en:

👉 https://github.com/saulsantibanezm/mapa-mexico-lom

## Autor

**Saul Santibañez Molina**
Servicio Social — IIMAS, UNAM 2026
Supervisor: Dr. Ivan Vladimir Meza Ruiz
