@echo off
start python start_flask.py
timeout /t 2
start http://localhost:8000/index.html