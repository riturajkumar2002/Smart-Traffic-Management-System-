@echo off
cd /d "%~dp0"
start "" python traffic_detection.py
timeout /t 5 /nobreak >nul
start http://127.0.0.1:5000/
exit
