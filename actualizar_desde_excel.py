import sqlite3
import openpyxl
import re

print("📦 Actualizando base de datos desde Excel...")

# Conectar a la base de datos
conn = sqlite3.connect('municipios.db')
cursor = conn.cursor()

# Agregar columna de población si no existe
try:
    cursor.execute("ALTER TABLE municipios ADD COLUMN poblacion INTEGER DEFAULT 0")
    print("✅ Columna 'poblacion' agregada")
except:
    print("ℹ️ La columna 'poblacion' ya existe")

# Cargar el archivo Excel
wb = openpyxl.load_workbook('municipios_con_coordenadas.xlsx')
sheet = wb.active

actualizados = 0
no_encontrados = 0

print("📊 Procesando datos...")

for row in sheet.iter_rows(min_row=2, values_only=True):  # Saltar encabezado
    if not row or not row[0]:
        continue
    
    clave_estado = str(row[0]).strip().zfill(2)
    clave_municipio = str(row[2]).strip().zfill(3)
    nombre_municipio = row[3].strip() if row[3] else ""
    latitud = row[5] if row[5] else 0
    longitud = row[4] if row[4] else 0
    poblacion = row[6] if len(row) > 6 and row[6] else 0
    
    # Actualizar municipio
    cursor.execute("""
        UPDATE municipios 
        SET lat = ?, lon = ?, poblacion = ?
        WHERE clave_estado = ? AND clave_municipio = ?
    """, (latitud, longitud, poblacion, clave_estado, clave_municipio))
    
    if cursor.rowcount > 0:
        actualizados += 1
    else:
        # Si no existe por clave, intentar por nombre
        cursor.execute("""
            UPDATE municipios 
            SET lat = ?, lon = ?, poblacion = ?
            WHERE nombre = ? AND clave_estado = ?
        """, (latitud, longitud, poblacion, nombre_municipio, clave_estado))
        if cursor.rowcount > 0:
            actualizados += 1
        else:
            no_encontrados += 1
            print(f"⚠️ No encontrado: {clave_estado}-{clave_municipio} {nombre_municipio}")

conn.commit()

# Verificar resultados
print(f"\n✅ Municipios actualizados: {actualizados}")
print(f"⚠️ Municipios no encontrados: {no_encontrados}")

# Mostrar ejemplos
print("\n📌 Ejemplos de municipios actualizados:")
cursor.execute("SELECT nombre, lat, lon, poblacion FROM municipios WHERE lat != 0 LIMIT 5")
for row in cursor.fetchall():
    print(f"  {row[0]}: ({row[1]}, {row[2]}) - Población: {row[3]}")

conn.close()
print("\n✅ Actualización completada")
