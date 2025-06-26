FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Upgrade pip and install dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy only the script from src
COPY src/main.py ./

CMD ["python", "main.py"]
