# Rapport de Lab – Gestion du cycle de vie des modèles avec MLflow

## Objectif du Lab
L’objectif de ce lab est de mettre en place un workflow MLOps structuré en utilisant MLflow afin de suivre les expérimentations, gérer les versions des modèles de machine learning et contrôler explicitement leur mise en production. Le lab vise également à assurer que le service d’inférence utilise en permanence le modèle actif défini dans le Model Registry.

## Étape 1 : Initialisation de l’environnement et installation de MLflow

Commandes exécutées

<img width="945" height="23" alt="image" src="https://github.com/user-attachments/assets/412e64ca-4e1d-4ecf-86f0-bc060de1e3d8" />

Cette étape a permis de préparer un environnement Python isolé et d’installer MLflow pour le projet.

## Étape 2 : Création explicite de l’espace de stockage MLflow

Commande exécutée

<img width="945" height="29" alt="image" src="https://github.com/user-attachments/assets/adbdce5d-94a6-4859-978f-f672d3d14a19" />

Cette étape a permis de créer un espace dédié au stockage des artefacts MLflow.

## Étape 3 : Configuration du client MLflow

Commandes exécutées

<img width="945" height="25" alt="image" src="https://github.com/user-attachments/assets/66eda5ef-2c86-4e43-9d58-fd50061ef047" />

Vérification :

<img width="945" height="52" alt="image" src="https://github.com/user-attachments/assets/beabef66-eca4-4e51-bf97-4d9edecc1907" />

Cette étape a permis de configurer l’envoi des runs vers le serveur MLflow central.

## Étape 4 : Démarrage du serveur MLflow

Commandes exécutées

<img width="945" height="441" alt="image" src="https://github.com/user-attachments/assets/b19cf9f8-36b9-4cf2-9398-05e00b7dbcfb" />

<img width="945" height="469" alt="image" src="https://github.com/user-attachments/assets/87c2c8bb-f37b-4ef6-95f5-c95d5f349757" />

<img width="945" height="148" alt="image" src="https://github.com/user-attachments/assets/dec12cdd-89b1-467d-af51-079d36f4d117" />

Cette étape a permis de démarrer le tracking server MLflow comme source centrale de vérité.

## Étape 5 : Instrumentation du script train.py avec MLflow

Commandes exécutées

<img width="945" height="367" alt="image" src="https://github.com/user-attachments/assets/febba266-72c9-4cc6-a682-f96178170008" />

Cette étape a permis d’enregistrer automatiquement les paramètres, métriques, artefacts et versions du modèle.

## Étape 6 : Observation du Model Registry MLflow

Commandes exécutées

* Ouverture de l’interface MLflow
* Onglet Models
* Sélection du modèle `churn_model`

<img width="945" height="468" alt="image" src="https://github.com/user-attachments/assets/62dce61a-554a-459d-87b6-6be92821712d" />

<img width="945" height="422" alt="image" src="https://github.com/user-attachments/assets/40fab5fa-5818-43d0-85d6-1abaa7d63372" />

Cette étape a permis de vérifier la création et le versionnement du modèle dans le Model Registry.

## Étape 7 : Promotion d’un modèle

Commandes exécutées

<img width="945" height="46" alt="image" src="https://github.com/user-attachments/assets/22f22010-9afb-4aab-8c5e-7e4aabdf0701" />

<img width="945" height="276" alt="image" src="https://github.com/user-attachments/assets/cb865ea6-c8ee-4bcd-8d18-d7557cd21544" />

Cette étape a permis d’activer explicitement une version du modèle via l’alias production.

## Étape 8 : Rollback via MLflow Model Registry

Commandes exécutées

Rollback automatique :

<img width="945" height="62" alt="image" src="https://github.com/user-attachments/assets/ba878907-46c9-4399-a4f0-50692018dfc2" />

<img width="945" height="412" alt="image" src="https://github.com/user-attachments/assets/3e3ef156-d8fa-410a-9376-bad77485337c" />

Cette étape a permis de revenir à une version antérieure du modèle en modifiant uniquement l’alias MLflow, sans modifier le code ni redéployer l’API.

## Étape 9 : API – Chargement du modèle actif depuis MLflow

Commandes exécutées

Démarrage du serveur FastAPI :

<img width="945" height="168" alt="image" src="https://github.com/user-attachments/assets/9431c383-5833-4e92-bbf7-c32b1f3d5186" />

<img width="945" height="443" alt="image" src="https://github.com/user-attachments/assets/dc98d536-4f91-485f-a044-f73493f1bd10" />

Cette étape a permis de garantir que l’API sert toujours la version active du modèle définie dans MLflow, même après promotion ou rollback.

## Conclusion 

Ce lab a permis de mettre en œuvre un cycle de vie complet des modèles de machine learning en s’appuyant sur MLflow. L’utilisation du Model Registry, des alias et de l’intégration avec l’API assure une gestion fiable, traçable et contrôlée des modèles en production, conforme aux bonnes pratiques MLOps.
