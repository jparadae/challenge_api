import csv
import os
from api.models import Department

def run():
    # Ruta base del proyecto
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Ruta al archivo departamentos.csv
    file_path = os.path.join(base_dir, 'data', 'departamentos.csv')

    print(f"Importando datos desde {file_path}...")

    # Abrir y leer el archivo CSV
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Crear los departamentos en la base de datos
            Department.objects.create(id=row[0], name=row[1])

    print("Datos de departamentos importados con éxito.")
