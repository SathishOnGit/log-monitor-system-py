# Log Monitoring & Analysis System

## Overview

The Log Monitoring & Analysis System is a Python-based application designed to monitor, analyze, and manage application log files. It helps developers and system administrators detect errors, track warnings, analyze log activity, and generate reports automatically.

This project demonstrates core Python concepts such as Object-Oriented Programming (OOP), File Handling, Multithreading, Logging, CSV Report Generation, and Modular Programming.

---

## Features

* Analyze log files
* Count INFO, WARNING, and ERROR logs
* Search logs by keyword
* Real-time log monitoring
* CSV report generation
* Multithreaded monitoring
* Application logging
* Modular project structure
* Easy to extend and maintain

---

## Technologies Used

* Python 3
* Threading
* Logging Module
* CSV Module
* File Handling
* Object-Oriented Programming (OOP)

---

## Project Structure

```text
log-monitor-system/

│
├── logs/
│   └── app.log
│
├── reports/
│   └── log_report.csv
│
├── analyzer.py
├── monitor.py
├── search.py
├── report_generator.py
├── logger_config.py
├── main.py
│
└── README.md
```

---

## How It Works

1. Reads application log files.
2. Identifies INFO, WARNING, and ERROR messages.
3. Generates summary statistics.
4. Detects errors in real time.
5. Searches logs using keywords.
6. Exports analysis results to CSV reports.
7. Stores application activity using Python logging.

---

## Sample Log File

```text
2026-06-05 10:00:00 INFO User login successful
2026-06-05 10:01:15 ERROR Database connection failed
2026-06-05 10:02:30 WARNING Disk space low
2026-06-05 10:03:00 INFO File uploaded
2026-06-05 10:04:00 ERROR API timeout
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/log-monitor-system.git
```

Navigate to the project directory:

```bash
cd log-monitor-system
```

Run the application:

```bash
python main.py
```

---

## Example Output

```text
LOG SUMMARY

INFO: 3
WARNING: 1
ERROR: 2

ERROR DETAILS

2026-06-05 10:01:15 ERROR Database connection failed
2026-06-05 10:04:00 ERROR API timeout
```

---

## Python Concepts Demonstrated

### Object-Oriented Programming

* Classes
* Methods
* Constructors

### File Handling

* Reading log files
* Processing large datasets

### Multithreading

* Background log monitoring

### Logging

* Application activity tracking
* Debugging support

### CSV Processing

* Report generation

### Exception Handling

* File access errors
* Runtime issues

---

## Challenges Solved

* Real-time log monitoring
* Efficient log analysis
* Modular code organization
* Automated report generation

---

## Future Enhancements

* SQLite Database Integration
* Email Alerts
* PDF Reports
* Regex Pattern Matching
* Flask Dashboard
* REST API Integration
* Docker Deployment

