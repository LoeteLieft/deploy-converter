# deploy-converter Dockerfile

FROM python:3.12-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main"]

# Additional Implementation 1760957882

# Code Update 1760957882-18663

# Touch update: 1760957883

# PR Merge: 2025-10-20 - feature/merge-4614

# PR Update: 2025-10-20 - refactor/update-5807
