import subprocess
import requests
import threading
from flask import Flask
import webbrowser
import time

app = Flask(__name__)

def run_flask():
    # Démarre l'application Flask
    subprocess.Popen(["python", "AppliPythonPageAccueil.py"], creationflags=subprocess.CREATE_NEW_CONSOLE)

@app.route('/start_flask', methods=['GET'])
def start_flask():
    try:
        # Vérifie si l'application Flask est déjà en cours d'exécution
        response = requests.get("http://127.0.0.1:5000/")
        if response.status_code == 200:
            return "L'application Flask est déjà en cours d'exécution.", 200
    except requests.ConnectionError:
        print("L'application Flask n'est pas en cours d'exécution. Démarrage...")

    # Démarre l'application Flask dans un thread séparé
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    time.sleep(2)  # Attendre un moment pour s'assurer que Flask a démarré
    webbrowser.open("http://127.0.0.1:5000/")  # Ouvre la page HTML dans le navigateur

    return "Application Flask démarrée.", 200

if __name__ == "__main__":
    # Lancer le serveur Flask pour écouter les requêtes de démarrage
    app.run(port=8000)
