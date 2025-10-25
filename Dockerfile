FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Collect static files for production
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

# Run using Gunicorn in production
CMD ["gunicorn", "personal_website.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--timeout", "120"]


