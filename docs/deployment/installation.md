# 🚀 Installation Guide

Step-by-step instructions for setting up the BOSC Community Library locally or on your server.

---

## 📋 Table of Contents

1. [System Requirements](#system-requirements)
2. [Local Development Setup](#local-development-setup)
3. [Production Setup](#production-setup)
4. [Troubleshooting](#troubleshooting)
5. [Next Steps](#next-steps)

---

## 💻 System Requirements

### Minimum Requirements
- **OS:** Windows, macOS, or Linux
- **Python:** 3.8 or higher
- **RAM:** 4GB minimum
- **Disk Space:** 2GB for application + content
- **Internet:** For initial setup and updates

### For Development
- Git client
- Text editor or IDE (VS Code recommended)
- Terminal/Command line access

### For Production
- Web server (Nginx or Apache)
- Database (PostgreSQL recommended)
- SSL certificate for HTTPS
- Backup storage

---

## 🛠️ Local Development Setup

### Step 1: Clone the Repository

```bash
# Navigate to where you want the project
cd ~/projects

# Clone the repository
git clone https://github.com/BOSC/Community-Library.git
cd BOSC-Community-Library
```

### Step 2: Create a Virtual Environment

**On macOS/Linux:**
```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate
```

**On Windows (PowerShell):**
```powershell
# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1
```

**On Windows (Command Prompt):**
```cmd
# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate.bat
```

### Step 3: Install Dependencies

```bash
# Upgrade pip
pip install --upgrade pip

# Install project dependencies
python scripts/setup.py
```

If setup.py doesn't exist, install manually:
```bash
# Install basic requirements
pip install -r requirements.txt

# If you're contributing to docs:
pip install sphinx sphinx-rtd-theme

# For development:
pip install black flake8 pytest
```

### Step 4: Verify Installation

```bash
# Test Python version
python --version

# Check if main modules load
python -c "import sys; print('Python working correctly')"

# Try running a script
python scripts/search_resources.py "test"
```

### Step 5: Set Up Your Editor

**VS Code:**
1. Open project folder in VS Code
2. Install "Python" extension by Microsoft
3. Select Python interpreter from `venv/bin/python`
4. Install "Markdown" extension for docs

**Configuration:**
- Python formatter: Black
- Linter: Flake8
- Test framework: Pytest

---

## 🌐 Production Setup

### Step 1: Server Requirements

```
Required:
- Ubuntu 20.04 LTS or similar Linux
- Python 3.8+
- Nginx or Apache web server
- PostgreSQL database (optional, if needed)
- Certbot for SSL (HTTPS)
```

### Step 2: Installation on Server

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install Python and requirements
sudo apt install -y python3 python3-pip python3-venv

# Install web server
sudo apt install -y nginx

# Clone repository
git clone https://github.com/BOSC/Community-Library.git
cd BOSC-Community-Library

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install --upgrade pip
python scripts/setup.py
```

### Step 3: Configure Web Server

See [Configuration Guide](configuration.md) for detailed web server setup.

### Step 4: Enable HTTPS

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx

# Get SSL certificate
sudo certbot certonly --nginx -d yourdomain.com

# Configure auto-renewal
sudo systemctl enable certbot.timer
```

### Step 5: Deploy Application

```bash
# Set up as system service (if applicable)
# See configuration.md for systemd service setup

# Or deploy with Docker (if using containers)
docker build -t bosc-library .
docker run -p 80:8000 bosc-library
```

---

## 🐛 Troubleshooting

### Python Not Found
```bash
# Check Python installation
python --version

# If not found, install Python:
# Ubuntu/Debian:
sudo apt install python3

# macOS (with Homebrew):
brew install python@3.11

# Windows:
# Download from python.org
```

### Virtual Environment Issues
```bash
# If venv won't activate:
# Delete and recreate
rm -rf venv
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate.bat  # Windows
```

### Dependency Installation Fails
```bash
# Try updating pip first
pip install --upgrade pip setuptools wheel

# Then try installing again
pip install -r requirements.txt

# If specific package fails, install individually:
pip install package-name
```

### Port Already in Use
```bash
# Change port in configuration file
# Or kill the process using the port

# On Linux/macOS:
lsof -i :8000  # Find process
kill -9 <PID>  # Kill it

# On Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Permission Issues
```bash
# Linux/macOS: Run with sudo if needed
sudo python scripts/setup.py

# Or change ownership
sudo chown -R $USER:$USER .
```

---

## ✅ Verification Checklist

After installation, verify:

- ✅ Python installed and accessible
- ✅ Virtual environment created and activated
- ✅ All dependencies installed without errors
- ✅ Test script runs successfully
- ✅ Project folder structure intact
- ✅ Git repository accessible
- ✅ Editor/IDE configured (for development)

---

## 📖 Next Steps

### For Contributors
1. ✅ Installation complete!
2. Read [GETTING_STARTED.md](../../GETTING_STARTED.md)
3. Create a feature branch
4. Make your first contribution

### For Development
1. Read [Architecture documentation](../architecture.md)
2. Check [Configuration Guide](configuration.md)
3. Set up your development environment
4. Run tests: `pytest`

### For Production Deployment
1. Follow [Configuration Guide](configuration.md)
2. Set up database (if needed)
3. Configure web server
4. Enable HTTPS
5. Set up monitoring

### For Questions
- Check [troubleshooting](#troubleshooting) section above
- See [main README](../../README.md) for navigation
- Open a GitHub Issue
- Check [Community Discussions](../../community/MEETINGS.md)

---

## 🎉 Ready to Go!

Your BOSC Community Library installation is ready. 

**Next:**
- [Contributing](../../GETTING_STARTED.md)
- [Architecture docs](../architecture.md)
- [Configuration](configuration.md)

---

**[← Back to Deployment](README.md) | [← Back to Docs](../README.md) | [← Back to Main README](../../README.md)**
