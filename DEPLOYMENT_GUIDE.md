# Deployment Guide

This comprehensive guide covers deploying your Django personal website to various platforms.

## Table of Contents

1. [Pre-Deployment Checklist](#pre-deployment-checklist)
2. [Docker Deployment](#docker-deployment)
3. [Platform-Specific Guides](#platform-specific-guides)
4. [Production Configuration](#production-configuration)
5. [Monitoring & Maintenance](#monitoring--maintenance)

---

## Pre-Deployment Checklist

Before deploying to production, ensure you complete these steps:

### 1. Security Configuration

```bash
# Generate a secure SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Update your `.env` file:
```env
DEBUG=False
SECRET_KEY=<your-generated-secret-key>
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

### 2. Database Migration

If using PostgreSQL:
```bash
# Create database
createdb personal_website

# Update .env
DATABASE_URL=postgresql://user:password@localhost:5432/personal_website

# Run migrations
python manage.py migrate
```

### 3. Static Files

```bash
# Collect static files
python manage.py collectstatic --noinput
```

### 4. Email Configuration

Set up email backend (example with Gmail):
```env
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

**Note:** For Gmail, use an [App Password](https://support.google.com/accounts/answer/185833)

### 5. Initial Content

```bash
# Populate database with initial data
python manage.py populate_data

# Create superuser
python manage.py createsuperuser
```

---

## Docker Deployment

### Build and Run

```bash
# Build the Docker image
docker build -t personal-website .

# Run the container
docker run -d -p 8000:8000 \
  --env-file .env \
  --name personal-website \
  personal-website
```

### Docker Compose (Recommended)

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Docker Compose with PostgreSQL

Create a `docker-compose.prod.yml`:

```yaml
version: '3.8'

services:
  db:
    image: postgres:15-alpine
    volumes:
      - postgres_data:/var/lib/postgresql/data
    environment:
      - POSTGRES_DB=personal_website
      - POSTGRES_USER=postgres
      - POSTGRES_PASSWORD=your-secure-password
    
  web:
    build: .
    command: gunicorn personal_website.wsgi:application --bind 0.0.0.0:8000 --workers 4
    volumes:
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "8000:8000"
    environment:
      - DEBUG=False
      - SECRET_KEY=your-secret-key
      - DATABASE_URL=postgresql://postgres:your-secure-password@db:5432/personal_website
    depends_on:
      - db
  
  nginx:
    image: nginx:alpine
    volumes:
      - ./nginx.conf:/etc/nginx/nginx.conf
      - static_volume:/app/staticfiles
      - media_volume:/app/media
    ports:
      - "80:80"
      - "443:443"
    depends_on:
      - web

volumes:
  postgres_data:
  static_volume:
  media_volume:
```

---

## Platform-Specific Guides

### AWS Elastic Beanstalk

1. Install EB CLI:
```bash
pip install awsebcli
```

2. Initialize EB:
```bash
eb init -p docker personal-website
```

3. Create environment:
```bash
eb create production-env
```

4. Set environment variables:
```bash
eb setenv DEBUG=False SECRET_KEY=your-secret-key
```

5. Deploy:
```bash
eb deploy
```

### Heroku

1. Install Heroku CLI and login:
```bash
heroku login
```

2. Create app:
```bash
heroku create your-website-name
```

3. Add PostgreSQL:
```bash
heroku addons:create heroku-postgresql:hobby-dev
```

4. Set environment variables:
```bash
heroku config:set DEBUG=False
heroku config:set SECRET_KEY=your-secret-key
```

5. Deploy:
```bash
git push heroku main
```

6. Run migrations:
```bash
heroku run python manage.py migrate
heroku run python manage.py populate_data
heroku run python manage.py createsuperuser
```

### DigitalOcean App Platform

1. Create `app.yaml`:
```yaml
name: personal-website
services:
  - name: web
    github:
      repo: your-username/personal-website
      branch: main
    dockerfile_path: Dockerfile
    http_port: 8000
    envs:
      - key: DEBUG
        value: "False"
      - key: SECRET_KEY
        value: your-secret-key
        type: SECRET
    
databases:
  - name: db
    engine: PG
    version: "14"
```

2. Deploy via DigitalOcean dashboard or `doctl`

### AWS ECS/Fargate

1. Create ECR repository:
```bash
aws ecr create-repository --repository-name personal-website
```

2. Build and push image:
```bash
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account-id>.dkr.ecr.us-east-1.amazonaws.com

docker build -t personal-website .
docker tag personal-website:latest <account-id>.dkr.ecr.us-east-1.amazonaws.com/personal-website:latest
docker push <account-id>.dkr.ecr.us-east-1.amazonaws.com/personal-website:latest
```

3. Create ECS task definition and service via AWS Console or CLI

### Google Cloud Run

1. Build and push to Google Container Registry:
```bash
gcloud builds submit --tag gcr.io/PROJECT-ID/personal-website
```

2. Deploy:
```bash
gcloud run deploy personal-website \
  --image gcr.io/PROJECT-ID/personal-website \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

3. Set environment variables:
```bash
gcloud run services update personal-website \
  --set-env-vars DEBUG=False,SECRET_KEY=your-secret-key
```

### Traditional VPS (Ubuntu/Debian)

1. Update system:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Install dependencies:
```bash
sudo apt install python3-pip python3-venv postgresql nginx supervisor
```

3. Set up PostgreSQL:
```bash
sudo -u postgres createuser --interactive
sudo -u postgres createdb personal_website
```

4. Clone and setup:
```bash
git clone <your-repo> /var/www/personal-website
cd /var/www/personal-website
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

5. Configure Gunicorn with Supervisor:

`/etc/supervisor/conf.d/personal-website.conf`:
```ini
[program:personal-website]
directory=/var/www/personal-website
command=/var/www/personal-website/venv/bin/gunicorn personal_website.wsgi:application --workers 4 --bind 0.0.0.0:8000
user=www-data
autostart=true
autorestart=true
stderr_logfile=/var/log/personal-website.err.log
stdout_logfile=/var/log/personal-website.out.log
```

6. Configure Nginx:

`/etc/nginx/sites-available/personal-website`:
```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location /static/ {
        alias /var/www/personal-website/staticfiles/;
    }
    
    location /media/ {
        alias /var/www/personal-website/media/;
    }
    
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

7. Enable site and SSL:
```bash
sudo ln -s /etc/nginx/sites-available/personal-website /etc/nginx/sites-enabled/
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com
sudo systemctl restart nginx
sudo supervisorctl reread
sudo supervisorctl update
```

---

## Production Configuration

### Django Settings

Add to `settings.py`:

```python
import os
from decouple import config

# Security
SECURE_SSL_REDIRECT = config('SECURE_SSL_REDIRECT', default=False, cast=bool)
SESSION_COOKIE_SECURE = config('SESSION_COOKIE_SECURE', default=False, cast=bool)
CSRF_COOKIE_SECURE = config('CSRF_COOKIE_SECURE', default=False, cast=bool)
SECURE_HSTS_SECONDS = config('SECURE_HSTS_SECONDS', default=0, cast=int)
SECURE_HSTS_INCLUDE_SUBDOMAINS = config('SECURE_HSTS_INCLUDE_SUBDOMAINS', default=False, cast=bool)
SECURE_HSTS_PRELOAD = config('SECURE_HSTS_PRELOAD', default=False, cast=bool)

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'django.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### Environment Variables

Production `.env`:
```env
DEBUG=False
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

DATABASE_URL=postgresql://user:password@host:5432/dbname

EMAIL_HOST=smtp.sendgrid.net
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=apikey
EMAIL_HOST_PASSWORD=your-sendgrid-api-key

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS=True
SECURE_HSTS_PRELOAD=True
```

---

## Monitoring & Maintenance

### Health Checks

Create `core/views.py`:
```python
from django.http import JsonResponse

def health_check(request):
    return JsonResponse({'status': 'healthy'})
```

Add to `urls.py`:
```python
path('health/', health_check),
```

### Logging

Monitor Django logs:
```bash
# Docker
docker-compose logs -f web

# Supervisor
tail -f /var/log/personal-website.out.log
```

### Database Backups

```bash
# PostgreSQL backup
pg_dump personal_website > backup_$(date +%Y%m%d).sql

# Restore
psql personal_website < backup_20241225.sql
```

### Automated Backups (cron)

```bash
# Edit crontab
crontab -e

# Add daily backup at 2 AM
0 2 * * * pg_dump personal_website > /backups/backup_$(date +\%Y\%m\%d).sql
```

### Monitoring Services

Consider integrating:
- **Sentry**: Error tracking and monitoring
- **New Relic**: Application performance monitoring
- **DataDog**: Infrastructure and application monitoring
- **UptimeRobot**: Uptime monitoring

### SSL Certificate Renewal

If using Let's Encrypt:
```bash
# Auto-renewal is typically configured during certbot setup
# Test renewal
sudo certbot renew --dry-run
```

### Updates and Maintenance

```bash
# Pull latest code
git pull origin main

# Update dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Restart application
sudo supervisorctl restart personal-website
# or for Docker
docker-compose restart web
```

---

## Troubleshooting

### Static Files Not Loading
```bash
python manage.py collectstatic --noinput
# Check STATIC_ROOT and STATIC_URL in settings.py
```

### Database Connection Issues
```bash
# Test connection
python manage.py dbshell
# Check DATABASE_URL in .env
```

### Email Not Sending
```bash
# Test email configuration
python manage.py shell
>>> from django.core.mail import send_mail
>>> send_mail('Test', 'Test message', 'from@example.com', ['to@example.com'])
```

### 502 Bad Gateway
```bash
# Check if Gunicorn is running
sudo supervisorctl status personal-website
# Check logs
tail -f /var/log/personal-website.err.log
```

---

## Performance Optimization

### Enable Caching

Install Redis:
```bash
pip install redis django-redis
```

Update `settings.py`:
```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### Database Optimization
```python
# Use select_related and prefetch_related
projects = Project.objects.select_related('category').all()

# Add database indexes
class Meta:
    indexes = [
        models.Index(fields=['created_at']),
    ]
```

### CDN for Static Files

Use AWS S3 + CloudFront or similar:
```bash
pip install django-storages boto3
```

```python
# settings.py
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
```

---

## Support

For issues and questions:
- Check Django documentation: https://docs.djangoproject.com/
- Review project README: `/README.md`
- Open GitHub issue: <your-repo-url>/issues

---

**Deployment Complete!** Your professional personal website is now live and ready to showcase your work to the world! 🚀
