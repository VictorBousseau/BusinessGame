@echo off
echo Démarrage du serveur Flask...
start cmd /K ""C:\Users\helen\anaconda3\python.exe" "C:\Users\helen\OneDrive\Bureau\Victor Test\BusinessGame\start_flask.py""
timeout /t 5
echo Ouverture du site web...
start "" "https://victorbousseau.github.io/BusinessGame/"
pause
