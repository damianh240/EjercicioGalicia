# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al contenedor
#COPY . /app
COPY requirements.txt .

# Instala las dependencias en el contenedor
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente al contenedor
COPY . .

# Exponer el puerto que usará FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
# 0.0.0.0 => todas las interfaces de red disponibles
