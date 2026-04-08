@echo off
python Main.py
timeout /t 3
echo Abriendo carpeta logs...
start "" "%~dp0Logs"