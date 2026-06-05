# Docker Guardian

## Project Overview

Docker Guardian is an Intelligent Docker Monitoring and Auto-Healing System developed to solve real-world container management challenges faced in modern DevOps environments.
The system continuously monitors Docker containers, detects abnormal resource usage, predicts potential failures, automatically restarts unhealthy containers, and provides real-time visualization through a Flask-based dashboard.
This project demonstrates practical implementation of Linux automation, Docker administration, Python development, and intelligent monitoring techniques.

---

## Problem Statement

Organizations using Docker frequently face issues such as:

* Unexpected container crashes
* High CPU utilization
* Excessive memory consumption
* Large Docker log files
* Manual monitoring overhead
* Service downtime

These issues reduce application reliability and increase operational costs.
Docker Guardian automates monitoring and recovery processes to minimize downtime and improve system stability.

---

## Key Features

### Real-Time Monitoring

* Monitor all running Docker containers
* Track CPU usage
* Track memory consumption
* View container status

### Auto-Healing

* Detect stopped containers
* Restart failed containers automatically
* Reduce application downtime

### Alert System

* Detect abnormal resource utilization
* Generate alerts for administrators
* Display warning status on dashboard

### AI-Based Risk Prediction

* Analyze container resource usage
* Estimate failure probability
* Classify risk levels:

  * Low Risk
  * Medium Risk
  * High Failure Risk

### Storage Optimization

* Remove unused Docker images
* Remove stopped containers
* Clear oversized log files

### Web Dashboard

* Flask-based monitoring interface
* Live container information
* Resource utilization visualization

---

## Technology Stack
- Linux     : Operating System     
-  Docker   : Container Management 
- Python    : Backend Logic        
- Flask     : Web Dashboard        
- Bash      : Automation Scripts   
- Cron      : Scheduled Tasks     
- Git       : Version Control      
- GitHub    : Source Code Hosting 

---

## Installation Guide

### Step 1: Clone Repository

```bash
git clone https://github.com/yourusername/docker-guardian.git
cd docker-guardian
```

### Step 2: Install Dependencies

```bash
sudo apt update
sudo apt install docker.io python3 python3-pip -y
```

### Step 3: Install Python Packages

```bash
pip3 install flask
```

### Step 4: Start Docker

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

### Step 5: Run Test Containers

```bash
docker run -d --name nginx-test -p 8080:80 nginx
docker run -dit --name ubuntu-test ubuntu
```

### Step 6: Launch Dashboard

```bash
python3 app.py
```

Open browser:

```text
http://127.0.0.1:5000
```

---

## Dashboard Features

The dashboard displays:

* Container Name
* CPU Usage
* Memory Usage
* Alert Status
* Failure Risk Prediction

Example:

```text
Container: nginx-test
CPU Usage: 0.00%
Memory Usage: 0.05%
Alert Status: Normal
Failure Risk: Low
```

---

## Testing

### Simulate Container Failure

```bash
docker stop nginx-test
```

### Run Monitoring

```bash
./monitor.sh
```

Expected Result:

```text
Container detected as stopped
Container restarted automatically
```

---

### Dashboard

```text
Add screenshot:
screenshots/dashboard.png
```

### Monitoring Output

```text
Add screenshot:
screenshots/monitoring.png
```

### Auto-Healing Demonstration

```text
Add screenshot:
screenshots/healing.png
```

---

## Challenges Faced

* Real-time Docker statistics collection
* Dashboard synchronization
* Threshold tuning
* Container restart automation
* Risk prediction accuracy

---

## Benefits

* Reduced downtime
* Improved reliability
* Automated monitoring
* Better resource management
* Lightweight architecture
* Easy deployment

---

## Future Enhancements

* Kubernetes Integration
* Telegram Alerts
* WhatsApp Notifications
* Multi-Server Monitoring
* Cloud Integration
* Advanced Machine Learning Models
* Security Threat Detection

---

## References

* Docker Documentation
* Flask Documentation
* Python Documentation
* Kubernetes Documentation
* Prometheus Monitoring Documentation
* Grafana Documentation

---

## 👩‍💻 Author

**Vaishnavi Manepatil**

Mini Projet Engineering Project

Docker Guardian – Intelligent Docker Monitoring & Auto-Healing System

---

⭐ If you found this project useful, consider giving it a star.
