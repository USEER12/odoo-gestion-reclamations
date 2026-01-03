# odoo-gestion-reclamations
Projet ERP Odoo – Module Gestion des Réclamations
📝 Description du projet

Ce projet consiste à développer un module spécifique pour l’ERP Odoo 17 intitulé Gestion des Réclamations.
Il permet de gérer les réclamations internes des employés au sein d’une organisation (RH, IT, administration, etc.).

Le module est déployé à l’aide de Docker, ce qui facilite l’installation et l’exécution de l’ERP.

🎯 Objectifs

Centraliser les réclamations internes

Permettre la création et le suivi des réclamations

Gérer les priorités et les états

S’intégrer dans un ERP Odoo

🧩 Fonctionnalités

Création d’une réclamation

Consultation de la liste des réclamations

Gestion des priorités (faible, moyenne, haute)

Suivi de l’état (nouvelle, en cours, traitée)

Interface simple (liste et formulaire)

🏗️ Structure du projet
odoo-docker/
├── addons/
│   └── gestion_reclamations/
│       ├── models/
│       ├── views/
│       ├── security/
│       ├── __manifest__.py
│       └── __init__.py
├── docker-compose.yml
└── README.md

🛠️ Technologies utilisées

Odoo 17

Python

XML

PostgreSQL

Docker / Docker Compose

Git / GitHub

🚀 Installation et exécution
Prérequis

Docker

Docker Compose

Étapes

Cloner le projet :

git clone https://github.com/USEER12/odoo-gestion-reclamations.git


Lancer le projet :

docker compose up -d


Accéder à Odoo :

http://localhost:8069


Installer le module Gestion des Réclamations depuis le menu Applications.
