# Dockerfile

# Verwende das offizielle Python-Image als Basis
FROM python:3.9

# Setze das Arbeitsverzeichnis in Container
WORKDIR /app

# Kopiere die Abhängigkeiten
COPY requirements.txt requirements.txt

# Installiere Abhängigkeiten
RUN pip install -r requirements.txt

# Kopiere den Rest des Codes
COPY . .

# Starte die Anwendung
CMD ["python", "app.py"]
