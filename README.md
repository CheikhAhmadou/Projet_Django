# README.md

# 🌍 Projet Django — Visualisation de Données avec Heatmap et Folium

## 👤 Auteur

**Cheikh Ahmadou**

---

## 🤘 Description du projet

Ce projet est une **application web développée avec Django** qui permet de **visualiser des données géographiques** sous forme de **carte interactive (heatmap)** grâce à la bibliothèque **Folium**.

L'objectif est de représenter spatialement des données (ex : écoles, points d'intérêt) à partir d'un fichier CSV et de fournir une interface web accessible.

---

## 🌟 Structure du projet

```
Projet_Django/
├── dashboard/              # Application Django pour les vues et la logique métier
├── heatmapproject/         # Répertoire principal du projet Django (settings, urls, wsgi)
├── templates/              # Pages HTML et fichiers de rendu
├── web/                    # Dossier pour les fichiers statiques (CSS, JS, images)
├── les ecoles.csv          # Données géographiques utilisées pour la heatmap
├── db.sqlite3              # Base de données locale
├── manage.py               # Script principal de gestion Django
├── procfile.wsgi           # Fichier de déploiement (ex: Heroku)
└── README.md               # Ce fichier de documentation
```

---

## ⚙️ Installation et mise en place

### 1️⃣ Cloner le projet

```bash
git clone https://github.com/CheikhAhmadou/Projet_Django.git
cd Projet_Django
```

### 2️⃣ Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate   # (Linux / macOS)
venv\Scripts\activate      # (Windows)
```

### 3️⃣ Installer les dépendances

Si tu as un fichier `requirements.txt` :

```bash
pip install -r requirements.txt
```

Sinon, installer Django et Folium manuellement :

```bash
pip install django folium
```

---

## 🚀 Exécution du projet

### Démarrer le serveur de développement :

```bash
python manage.py runserver
```

Ouvre ton navigateur à l'adresse :
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Tu verras la carte interactive affichant les données issues du fichier **les ecoles.csv**.

---

## 📊 Fonctionnalités principales

* 📍 Visualisation des données géographiques sur carte (heatmap)
* 📊 Gestion des données via Django ORM
* 🧭 Interface web responsive
* ⚙️ Déploiement simplifié (via `procfile.wsgi`)

---

## 🔧 Technologies utilisées

| Catégorie       | Outils / Frameworks                  |
| --------------- | ------------------------------------ |
| Backend         | Django                               |
| Frontend        | HTML, CSS, JS                        |
| Visualisation   | Folium                               |
| Base de données | SQLite                               |
| Déploiement     | Gunicorn, Procfile (Heroku possible) |
| Versionning     | Git / GitHub                         |

---

## 👨‍💻 Auteur

**Cheikh Ahmadou**

* 🌐 [GitHub - CheikhAhmadou](https://github.com/CheikhAhmadou)
* ✉️ Contact : *(ajouter ton email si souhaité)*

---

## 🪶 Licence

Ce projet est open source et peut être réutilisé à des fins éducatives ou personnelles.
© 2025 Cheikh Ahmadou. Tous droits réservés.
