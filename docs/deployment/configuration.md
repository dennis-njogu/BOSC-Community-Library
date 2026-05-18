# ⚙️ Configuration Guide

Detailed configuration instructions for the BOSC Community Library in different environments.

---

## 📋 Table of Contents

1. [Configuration Basics](#configuration-basics)
2. [Development Configuration](#development-configuration)
3. [Production Configuration](#production-configuration)
4. [Environment Variables](#environment-variables)
5. [Web Server Setup](#web-server-setup)
6. [Database Configuration](#database-configuration)
7. [Security Settings](#security-settings)

---

## 🎯 Configuration Basics

### Config File Location
```
BOSC-Community-Library/
└── config/
    ├── development.env
    ├── production.env
    └── settings.py
```

### Configuration Hierarchy
1. **Environment Variables** (highest priority)
2. **Environment-specific .env files**
3. **Default settings.py** (lowest priority)

---

## 💻 Development Configuration

### Development .env File

Create `config/development.env`:

```env
# Application Settings
APP_ENV=development
DEBUG=True
SECRET_KEY=dev-secret-key-not-for-production

# Database (if using SQLite for development)
DATABASE_URL=sqlite:///./test.db

# Server Settings
HOST=127.0.0.1
PORT=8000
WORKERS=1

# Logging
LOG_LEVEL=DEBUG
LOG_FILE=logs/app.log

# Features (optional)
ENABLE_API=True
ENABLE_ADMIN_PANEL=True
```

### Load Configuration

**In Python:**
```python
import os
from dotenv import load_dotenv

# Load development config
load_dotenv('config/development.env')

DEBUG = os.getenv('DEBUG', 'False') == 'True'
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
```

### Running Development Server

```bash
# Load config and run
source config/development.env
python scripts/run_server.py

# Or with environment variables
export DEBUG=True
export PORT=8000
python -m server.app
```

---

## 🌐 Production Configuration

### Production .env File

Create `config/production.env`:

```env
# Application Settings
APP_ENV=production
DEBUG=False
SECRET_KEY=your-secure-random-key-here

# Database
DATABASE_URL=postgresql://user:password@db.example.com:5432/bosc_library

# Server Settings
HOST=0.0.0.0
PORT=8000
WORKERS=4

# Security
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
CORS_ORIGINS=https://yourdomain.com

# Logging
LOG_LEVEL=INFO
LOG_FILE=/var/log/bosc-library/app.log

# Backup & Monitoring
BACKUP_ENABLED=True
BACKUP_SCHEDULE=daily
BACKUP_LOCATION=/backups/bosc-library

# Email (for notifications)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=notifications@yourdomain.com
EMAIL_PASSWORD=your-email-password
```

### Generate Secure Secret Key

```bash
# Python
python -c "import secrets; print(secrets.token_urlsafe(50))"

# Or using Python's uuid
python -c "import uuid; print(str(uuid.uuid4()))"
```

---

## 🔐 Environment Variables

### Required Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `APP_ENV` | Environment (development/production) | `production` |
| `DEBUG` | Debug mode (True/False) | `False` |
| `SECRET_KEY` | Django/Flask secret key | `long-random-string` |
| `DATABASE_URL` | Database connection string | `postgresql://...` |
| `HOST` | Server host address | `0.0.0.0` |
| `PORT` | Server port | `8000` |

### Optional Variables

| Variable | Purpose | Default |
|----------|---------|---------|
| `LOG_LEVEL` | Logging level | `INFO` |
| `WORKERS` | Number of workers | `1` |
| `BACKUP_ENABLED` | Enable backups | `False` |
| `ENABLE_API` | Enable API endpoints | `True` |

### Setting Environment Variables

**Linux/macOS:**
```bash
# In terminal
export APP_ENV=production
export DEBUG=False

# Or in .env file and load
source config/production.env
```

**Windows (PowerShell):**
```powershell
$env:APP_ENV="production"
$env:DEBUG="False"
```

**Docker:**
```dockerfile
ENV APP_ENV=production
ENV DEBUG=False
ENV SECRET_KEY=your-secret-key
```

---

## 🌍 Web Server Setup

### Nginx Configuration

Create `/etc/nginx/sites-available/bosc-library`:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;

    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Certificates (from Certbot)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;

    # Proxy settings
    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    # Static files
    location /static/ {
        alias /home/bosc/BOSC-Community-Library/static/;
        expires 30d;
    }

    # Media files
    location /media/ {
        alias /home/bosc/BOSC-Community-Library/media/;
        expires 7d;
    }
}
```

Enable site:
```bash
sudo ln -s /etc/nginx/sites-available/bosc-library /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### Apache Configuration

Create `/etc/apache2/sites-available/bosc-library.conf`:

```apache
<VirtualHost *:80>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com
    Redirect permanent / https://yourdomain.com/
</VirtualHost>

<VirtualHost *:443>
    ServerName yourdomain.com
    ServerAlias www.yourdomain.com

    SSLEngine on
    SSLCertificateFile /etc/letsencrypt/live/yourdomain.com/fullchain.pem
    SSLCertificateKeyFile /etc/letsencrypt/live/yourdomain.com/privkey.pem

    ProxyPreserveHost On
    ProxyPass / http://127.0.0.1:8000/
    ProxyPassReverse / http://127.0.0.1:8000/

    <Directory /home/bosc/BOSC-Community-Library>
        Require all granted
    </Directory>
</VirtualHost>
```

Enable:
```bash
sudo a2enmod ssl proxy proxy_http
sudo a2ensite bosc-library
sudo systemctl restart apache2
```

---

## 🗄️ Database Configuration

### PostgreSQL Setup

```bash
# Install PostgreSQL
sudo apt install postgresql postgresql-contrib

# Create database and user
sudo -u postgres createdb bosc_library
sudo -u postgres createuser bosc_user
sudo -u postgres psql

# In psql prompt
ALTER USER bosc_user WITH PASSWORD 'secure_password';
GRANT ALL PRIVILEGES ON DATABASE bosc_library TO bosc_user;
\q
```

### Database URL

```env
# Format: postgresql://username:password@host:port/database
DATABASE_URL=postgresql://bosc_user:secure_password@localhost:5432/bosc_library
```

### Run Migrations

```bash
# Apply database migrations
python scripts/migrate.py

# Or if using Flask-Migrate
flask db upgrade
```

---

## 🔒 Security Settings

### Essential Security Configuration

```env
# 1. SECRET_KEY - Use a strong random string
SECRET_KEY=your-256-bit-random-key

# 2. DEBUG - MUST be False in production
DEBUG=False

# 3. ALLOWED_HOSTS - Only your domain
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com

# 4. CORS_ORIGINS - Only trusted origins
CORS_ORIGINS=https://yourdomain.com

# 5. Session Security
SESSION_COOKIE_SECURE=True
SESSION_COOKIE_HTTPONLY=True
SESSION_COOKIE_SAMESITE=Strict

# 6. HTTPS/TLS
SECURE_SSL_REDIRECT=True
SECURE_HSTS_SECONDS=31536000

# 7. Database
DATABASE_URL=postgresql://... (never commit with password)
```

### Firewall Configuration

```bash
# Ubuntu UFW
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp    # SSH
sudo ufw allow 80/tcp    # HTTP
sudo ufw allow 443/tcp   # HTTPS
sudo ufw enable
```

### Backup Security

```bash
# Secure backups location
mkdir -p /backups/bosc-library
chmod 700 /backups/bosc-library

# Encrypt backups (optional)
gpg --symmetric /backups/bosc-library/backup-2026-05-17.tar.gz
```

---

## ✅ Configuration Checklist

Before deploying to production:

- ✅ `DEBUG = False`
- ✅ `SECRET_KEY` is long and random
- ✅ Database credentials stored securely
- ✅ ALLOWED_HOSTS configured for your domain
- ✅ HTTPS/SSL certificate installed
- ✅ Firewall configured
- ✅ Backups enabled and tested
- ✅ Logging configured appropriately
- ✅ Static files collected: `python manage.py collectstatic`
- ✅ Migrations applied: `python manage.py migrate`

---

## 📞 Troubleshooting

### "Connection refused"
```
Check: Is the app running? Is the correct port open in firewall?
```

### "Invalid database URL"
```
Check: Database credentials and host are correct
Format: postgresql://user:password@host:port/database
```

### "HTTPS certificate error"
```
Renew: sudo certbot renew
Check: Certificate not expired: sudo certbot certificates
```

---

## 📖 Next Steps

- [Installation Guide](installation.md) — Server setup
- [Architecture](../architecture.md) — System design
- [Deployment](README.md) — Deployment overview
- [Main README](../../README.md) — Project overview

---

**[← Back to Deployment](README.md) | [← Back to Main README](../../README.md)**
