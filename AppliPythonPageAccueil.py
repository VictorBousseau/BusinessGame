#Application Python Accueil animateur
from flask import Flask, render_template_string
import matplotlib
matplotlib.use('Agg')  # Utiliser le backend Agg pour éviter Tkinter

import matplotlib.pyplot as plt
from io import BytesIO
import random
import base64

app = Flask(__name__)

# Noms des équipes et données simulées
noms_equipes = ["Équipe A", "Équipe B", "Équipe C", "Équipe D", "Équipe E"]
data = {
    "tresorerie": [random.randint(50000, 200000) for _ in noms_equipes],
    "chiffre_affaires": [random.randint(200000, 500000) for _ in noms_equipes],
    "employes": [random.randint(10, 50) for _ in noms_equipes],
    "benefices": [random.randint(10000, 100000) for _ in noms_equipes]
}

# Fonction pour créer un graphique en barres et retourner l'image en base64
def create_bar_chart(titre, valeurs, labels):
    plt.figure(figsize=(8, 6))
    plt.bar(labels, valeurs, color='skyblue')
    plt.title(titre)
    plt.xlabel("Équipes")
    plt.ylabel(titre)
    plt.tight_layout()

    # Sauvegarder l'image dans un flux de mémoire
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()

    # Encoder l'image en base64 pour l'intégrer dans le HTML
    return base64.b64encode(img.getvalue()).decode()

# Route pour la page d'accueil avec tous les graphiques
@app.route('/')
def accueil():
    tresorerie_img = create_bar_chart("Trésorerie des équipes", data["tresorerie"], noms_equipes)
    chiffre_affaires_img = create_bar_chart("Chiffre d'affaires des équipes", data["chiffre_affaires"], noms_equipes)
    employes_img = create_bar_chart("Nombre d'employés des équipes", data["employes"], noms_equipes)
    benefices_img = create_bar_chart("Bénéfices des équipes", data["benefices"], noms_equipes)

    # HTML pour afficher les images
    html = f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Classement des Équipes</title>
        <style>
            .grid-container {{
                display: flex;
                flex-wrap: wrap;
                gap: 5px; /* Espace entre les graphiques */
                justify-content: center;
            }}
            .grid-item {{
                flex: 1 1 calc(50% - 5px); /* Chaque graphique prend 50% de la largeur */
                max-width: calc(50% - 5px);
                box-sizing: border-box;
            }}
            img {{
                max-width: 100%;
                height: auto;
            }}
        </style>
    </head>
    <body>
        <h1>Bienvenue sur l'Application de Classement des Équipes</h1>
        <div class="grid-container">
            <div class="grid-item">
                <h2>Classement par Trésorerie</h2>
                <img src="data:image/png;base64,{tresorerie_img}" alt="Classement par trésorerie">
            </div>
            <div class="grid-item">
                <h2>Classement par Chiffre d'Affaires</h2>
                <img src="data:image/png;base64,{chiffre_affaires_img}" alt="Classement par chiffre d'affaires">
            </div>
            <div class="grid-item">
                <h2>Classement par Nombre d'Employés</h2>
                <img src="data:image/png;base64,{employes_img}" alt="Classement par nombre d'employés">
            </div>
            <div class="grid-item">
                <h2>Classement par Bénéfices</h2>
                <img src="data:image/png;base64,{benefices_img}" alt="Classement par bénéfices">
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
