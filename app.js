# deploy-converter Dockerfile

FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main"]

# Code Update 1760957882-11898

# Touch update: 1760957883

# Touch update: 1760957884

# Touch update: 1760957884

# Touch update: 1760957884
