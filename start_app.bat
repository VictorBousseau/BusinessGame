@echo off
start /B py start_flask.py
timeout /t 2
start https://victorbousseau.github.io/BusinessGame/
