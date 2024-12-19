:: Fichier pour le démarage de l'application, double clic sur ce fichier, cela lancera le programme start_flask.py et amenera sur l'URL :https://victorbousseau.github.io/BusinessGame/ 
@echo off
echo Démarrage du serveur Flask...
start cmd /K py start_flask.py
timeout /t 5
echo Ouverture du site web...
start "" "https://victorbousseau.github.io/BusinessGame/"
pause
