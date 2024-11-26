# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto esperado por Cloud Run
EXPOSE 8080

# Comando para ejecutar el servidor de Django y usar la variable PORT
CMD ["sh", "-c", "python manage.py runserver 0.0.0.0:$PORT"]
