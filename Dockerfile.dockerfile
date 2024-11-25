# Usar la imagen oficial de Python como base
FROM python:3.11-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos requeridos al contenedor
COPY . .

# Instalar las dependencias del proyecto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Crear un directorio para los archivos estáticos y recopilarlos
RUN mkdir -p /app/staticfiles
RUN python manage.py collectstatic --noinput

# Exponer el puerto que Heroku utilizará
EXPOSE 8000

# Definir el comando para ejecutar la aplicación
CMD ["gunicorn", "challenge_api.wsgi:application", "--bind", "0.0.0.0:8000"]
