FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY recherche_entreprises.py .
COPY details_entreprise.py .
COPY .env .

CMD ["python", "recherche_entreprises.py"]