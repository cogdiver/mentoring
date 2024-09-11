# Usa la imagen base de Python
FROM python:3.12-slim AS dev

# Establece el directorio de trabajo
WORKDIR /app

# Copia archivo de dependencias
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia los archivos de código fuente y los requisitos al contenedor
COPY . .

FROM dev AS jupyter
# Install jupyter dependency
RUN pip install jupyter==1.0.0
# Expose port 8085 fot jupyter interfaz
EXPOSE 8085
# Run jupyter application
CMD ["jupyter", "notebook", "--ip='*'", "--port=8085", "--no-browser", "--allow-root"]

FROM dev AS prd
CMD ["python", "main.py"]
