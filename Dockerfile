# Usa un'immagine di Python ufficiale come base
FROM python:3.9-slim

# Imposta la directory di lavoro nel contenitore
WORKDIR /app

# Copia il file requirements.txt nella directory di lavoro
COPY requirements.txt .

# Installa le dipendenze del progetto
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'applicazione nella directory di lavoro
COPY . .

# Esporta la porta su cui l'applicazione Flask sarà in ascolto
EXPOSE 5000

# Avvia l'applicazione Flask quando il contenitore viene eseguito
CMD ["python", "app.py"]
