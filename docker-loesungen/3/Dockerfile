FROM python:3.9-alpine

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port 3000 to allow external access
EXPOSE 3000

CMD ["python", "app.py"]