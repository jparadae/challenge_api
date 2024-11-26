# API REST - Carga Archivos y Batch Insert con CSV
Esta API permite cargar datos en formato JSON en las tablas departments, jobs y hired_employees. A continuación, se detallan los pasos para probar los endpoints principales.

## Endpoints Disponibles

### 1. Cargar Datos en Tablas con Batch Insert

Este endpoint permite insertar datos en lote en las tablas `departments`, `jobs` y `hired_employees`.

- **URL:** `http://127.0.0.1:8000/api/batch-insert/`
- **Método:** `POST`
- **Encabezados:**
    - `Content-Type: application/json`
- **Cuerpo (JSON):** La estructura del JSON depende de la tabla en la que se insertarán los datos.

#### a. Insertar Datos en `departments`

**Ejemplo de JSON:**

```json
{
        "table": "departments",
        "records": [
                { "id": 1, "name": "Sales" },
                { "id": 2, "name": "Engineering" },
                { "id": 3, "name": "HR" },
                { "id": 4, "name": "Finance" }
        ]
}
```

**Descripción:** Inserta departamentos con `id` y `name` en la tabla `departments`.

#### b. Insertar Datos en `jobs`

**Ejemplo de JSON:**

```json
{
        "table": "jobs",
        "records": [
                { "id": 1, "title": "Manager" },
                { "id": 2, "title": "Engineer" },
                { "id": 3, "title": "HR Specialist" },
                { "id": 4, "title": "Finance Analyst" }
        ]
}
```

**Descripción:** Inserta trabajos con `id` y `title` en la tabla `jobs`.

#### c. Insertar Datos en `hired_employees`

**Ejemplo de JSON:**

```json
{
        "table": "hired_employees",
        "records": [
                { "id": 1, "name": "John Doe", "hire_date": "2023-01-15", "department_id": 1, "job_id": 1 },
                { "id": 2, "name": "Jane Smith", "hire_date": "2023-01-16", "department_id": 2, "job_id": 2 },
                { "id": 3, "name": "Mark Johnson", "hire_date": "2023-01-17", "department_id": 3, "job_id": 3 },
                { "id": 4, "name": "Linda Davis", "hire_date": "2023-01-18", "department_id": 4, "job_id": 4 }
        ]
}
```

**Descripción:** Inserta empleados contratados en la tabla `hired_employees`. Este JSON debe contener los campos:
- `id`: Identificador único del empleado.
- `name`: Nombre del empleado.
- `hire_date`: Fecha de contratación en formato `YYYY-MM-DD`.
- `department_id`: ID del departamento (debe existir previamente en la tabla `departments`).
- `job_id`: ID del trabajo (debe existir previamente en la tabla `jobs`).

## Probar los Endpoints

### Requisitos Previos

Asegúrate de que el servidor de la API está corriendo:

```bash
python manage.py runserver
```

Ten disponible una herramienta como Postman o cURL para enviar las solicitudes.


### Cómo Probar la API: Ejemplo de Pruebas con Postman

#### Paso 1: Carga de  Datos en `upload-csv`

Para probar la carga de archivos CSV sin encabezado, utiliza la siguiente URL:
1. Selecciona el método `POST`.
2. URL: `http://127.0.0.1:8000/api/upload-csv/` y `http://127.0.0.1:8000/api/upload-csv-no-header/?`table=hired_employees
3. Ve a la pestaña `Body` y selecciona `form-data`.
4. Agrega la key file y en value  `adjuntar.csv`.

#### Paso 2: Insertar Datos en `departments`

1. Selecciona el método `POST`.
2. URL: `http://127.0.0.1:8000/api/batch-insert/`
3. Ve a la pestaña `Body` y selecciona `raw`.
4. Cambia el tipo a `JSON`.
5. Copia y pega el JSON de `departments`:

```json
{
        "table": "departments",
        "records": [
                { "id": 1, "name": "Sales" },
                { "id": 2, "name": "Engineering" },
                { "id": 3, "name": "HR" },
                { "id": 4, "name": "Finance" }
        ]
}
```

6. Haz clic en `Send` y verifica la respuesta:

```json
{
        "message": "Data inserted into departments successfully."
}
```

#### Paso 2: Insertar Datos en `jobs`

Repite los pasos anteriores, pero usa el JSON de `jobs`:

```json
{
        "table": "jobs",
        "records": [
                { "id": 1, "title": "Manager" },
                { "id": 2, "title": "Engineer" },
                { "id": 3, "title": "HR Specialist" },
                { "id": 4, "title": "Finance Analyst" }
        ]
}
```

Haz clic en `Send` y verifica la respuesta:

```json
{
        "message": "Data inserted into jobs successfully."
}
```

#### Paso 3: Insertar Datos en `hired_employees`

Usa el JSON de `hired_employees`:

```json
{
        "table": "hired_employees",
        "records": [
                { "id": 1, "name": "John Doe", "hire_date": "2023-01-15", "department_id": 1, "job_id": 1 },
                { "id": 2, "name": "Jane Smith", "hire_date": "2023-01-16", "department_id": 2, "job_id": 2 },
                { "id": 3, "name": "Mark Johnson", "hire_date": "2023-01-17", "department_id": 3, "job_id": 3 },
                { "id": 4, "name": "Linda Davis", "hire_date": "2023-01-18", "department_id": 4, "job_id": 4 }
        ]
}
```

Haz clic en `Send` y verifica la respuesta:

```json
{
        "message": "Data inserted into hired_employees successfully."
}
```
### 4. Construcción y Despliegue en Google Cloud Run

# Construcción imagen Docker en GCP

 Tener previamente instalado el `sdk google cli` para construir la imagen de Docker directamente 
 desde el directorio raíz del proyecto:

```
   `gcloud builds submit --tag gcr.io/<your-project-id>/django-app:latest`
```

Despliega la aplicación en Cloud Run con el siguiente comando:

```
json
gcloud run deploy django-app \
    --image gcr.io/<your-project-id>/django-app:latest \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated

```

# Pruebas con  API

```
https://<your-cloud-run-url>/api/upload-csv/


```