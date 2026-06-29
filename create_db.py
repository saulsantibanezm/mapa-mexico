#!/usr/bin/env python3
"""
Crea municipios.db desde el CSV de datos.

Uso:
    python create_db.py                        # usa coordenadas_municipios.csv en el mismo directorio
    python create_db.py ruta/otro_archivo.csv  # usa otro CSV

Formato del CSV requerido:
    clave_entidad, entidad, clave_municipio, municipio, longitud, latitud
"""

import sqlite3
import csv
import os
import sys


CSV_PATH = sys.argv[1] if len(sys.argv) > 1 else "coordenadas_municipios.csv"
DB_PATH  = "municipios.db"


def crear_base_datos(csv_path: str = CSV_PATH, db_path: str = DB_PATH) -> None:
    if not os.path.exists(csv_path):
        print(f"❌ No se encontró el archivo: {csv_path}")
        sys.exit(1)

    # Leer CSV
    with open(csv_path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        filas = list(reader)

    if not filas:
        print("❌ El CSV está vacío.")
        sys.exit(1)

    # Verificar columnas
    columnas_requeridas = {"clave_entidad", "entidad", "clave_municipio", "municipio", "longitud", "latitud"}
    columnas_csv = set(filas[0].keys())
    if not columnas_requeridas.issubset(columnas_csv):
        faltantes = columnas_requeridas - columnas_csv
        print(f"❌ Faltan columnas en el CSV: {faltantes}")
        sys.exit(1)

    # Agrupar por estado
    estados: dict[int, dict] = {}
    for fila in filas:
        eid  = int(fila["clave_entidad"])
        emun = int(fila["clave_municipio"])
        lat  = float(fila["latitud"])
        lon  = float(fila["longitud"])

        if eid not in estados:
            estados[eid] = {"nombre": fila["entidad"], "municipios": []}

        estados[eid]["municipios"].append({
            "clave": emun,
            "nombre": fila["municipio"],
            "lat": lat,
            "lon": lon,
        })

    # Crear / reemplazar DB
    if os.path.exists(db_path):
        os.remove(db_path)

    conn = sqlite3.connect(db_path)
    cur  = conn.cursor()

    cur.executescript("""
        PRAGMA journal_mode=WAL;

        CREATE TABLE estados (
            id      INTEGER PRIMARY KEY,
            nombre  TEXT    NOT NULL,
            lat     REAL    NOT NULL,
            lon     REAL    NOT NULL
        );

        CREATE TABLE municipios (
            id              INTEGER PRIMARY KEY AUTOINCREMENT,
            clave_municipio INTEGER NOT NULL,
            nombre          TEXT    NOT NULL,
            estado_id       INTEGER NOT NULL,
            lat             REAL    NOT NULL,
            lon             REAL    NOT NULL,
            FOREIGN KEY (estado_id) REFERENCES estados(id)
        );

        CREATE INDEX idx_mun_estado  ON municipios(estado_id);
        CREATE INDEX idx_mun_nombre  ON municipios(nombre COLLATE NOCASE);
        CREATE INDEX idx_est_nombre  ON estados(nombre COLLATE NOCASE);
    """)

    total_muns = 0
    for eid in sorted(estados):
        edo  = estados[eid]
        muns = edo["municipios"]

        # Centroide del estado = promedio de coordenadas de sus municipios
        lat_c = sum(m["lat"] for m in muns) / len(muns)
        lon_c = sum(m["lon"] for m in muns) / len(muns)

        cur.execute(
            "INSERT INTO estados VALUES (?, ?, ?, ?)",
            (eid, edo["nombre"], lat_c, lon_c)
        )

        cur.executemany(
            "INSERT INTO municipios (clave_municipio, nombre, estado_id, lat, lon) VALUES (?, ?, ?, ?, ?)",
            [(m["clave"], m["nombre"], eid, m["lat"], m["lon"]) for m in muns]
        )
        total_muns += len(muns)

    conn.commit()
    conn.close()

    print(f"✅ Base de datos creada: {db_path}")
    print(f"   {len(estados)} estados  |  {total_muns} municipios")


if __name__ == "__main__":
    crear_base_datos()
