# School Manager

Application Django de gestion scolaire réalisée à partir des TP 1 à 3 :
pages d'accueil et de présentation, gestion des étudiants et des enseignants,
recherche, filtre par classe et administration Django.

## Prérequis

- Python compatible avec Django 6.1
- PowerShell sous Windows

## Installation

Depuis le dossier `school_manager` :

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r .\school_project\requirements.txt
python .\school_project\manage.py migrate
```

Le projet conserve les étudiants déjà présents dans la base et les adapte au
nouveau modèle. Le champ `age` est conservé comme facultatif pour ne pas perdre
les données déjà enregistrées.

## Lancement

```powershell
python .\school_project\manage.py runserver
```

Ouvrir <http://127.0.0.1:8000/>.

## Adresses disponibles

- `/` : accueil et statistiques
- `/about/` : à propos
- `/students/` : liste et recherche d'étudiants
- `/students/<id>/` : fiche d'un étudiant
- `/students/classe/<classe>/` : filtre par classe
- `/teachers/` : liste des enseignants
- `/admin/` : administration Django

Pour créer le compte d'administration :

```powershell
python .\school_project\manage.py createsuperuser
```
