# Rapport de Lab Docker  
## Conteneurisation et orchestration de l’API Churn (mlops-lab-01)

---

## 1. Introduction

Dans le cadre de ce lab, l’objectif est de se familiariser avec les concepts fondamentaux de Docker à travers des manipulations progressives : exécution de conteneurs simples, compréhension des commandes Docker, puis conteneurisation et orchestration d’une API FastAPI de prédiction du churn développée lors d’un précédent projet MLOps.

Ce travail met en évidence l’intérêt de Docker pour le déploiement, la portabilité et la reproductibilité des applications de Machine Learning.

---

## 2. Étape 1 : Vérification de l’installation de Docker

### Description  
Cette étape consiste à vérifier que Docker est correctement installé et que le démon Docker fonctionne.

### Commandes exécutées

<img width="945" height="90" alt="image" src="https://github.com/user-attachments/assets/2ac0cdae-fdea-4a59-8af0-3433b07afea5" />

<img width="945" height="92" alt="image" src="https://github.com/user-attachments/assets/810b23de-a1fc-475e-b848-1b03f963355a" />


### Résultat attendu
- La version de Docker s’affiche correctement.
- La commande `docker ps` s’exécute sans erreur.


## 3. Étape 2 : Lancer un serveur Nginx dans un conteneur

### Description  
Un conteneur Nginx est lancé afin d’illustrer l’exécution d’un service web dans Docker.

### Commandes exécutées

<img width="945" height="252" alt="image" src="https://github.com/user-attachments/assets/510e48b7-bb58-4573-ba7a-6844a909b879" />

- Accès navigateur : `http://localhost:8080`

<img width="945" height="295" alt="image" src="https://github.com/user-attachments/assets/7bb700ab-ebd8-4e82-b761-ff52b0745ee1" />

<img width="945" height="79" alt="image" src="https://github.com/user-attachments/assets/5c5efd13-82dc-4d58-b357-f29de66f0300" />

<img width="945" height="193" alt="image" src="https://github.com/user-attachments/assets/3c4db09f-198f-49b9-bb52-8f803a4437ce" />

### Résultat attendu
- La page par défaut de Nginx s’affiche.
- Le conteneur apparaît dans la liste des conteneurs actifs.
- Le conteneur est arrêté puis supprimé.

## 4. Étape 3 : Ouvrir un shell Linux isolé dans un conteneur

### Description  
Cette étape permet d’explorer un environnement Linux isolé dans un conteneur Ubuntu.

### Commandes exécutées

<img width="945" height="320" alt="image" src="https://github.com/user-attachments/assets/6ffd7f54-dd41-4a01-b6ad-98ca1a14945d" />

<img width="945" height="410" alt="image" src="https://github.com/user-attachments/assets/a3acfd4e-446a-4ba6-b536-592b6d29ef22" />

<img width="945" height="485" alt="image" src="https://github.com/user-attachments/assets/7240b79a-e26d-4551-972e-bb623b914fcb" />

<img width="945" height="293" alt="image" src="https://github.com/user-attachments/assets/dd5a8496-51ac-4382-96d2-48bf67756f29" />

<img width="895" height="127" alt="image" src="https://github.com/user-attachments/assets/0094877b-d5bb-4035-b275-c1c3d968acc1" />

<img width="945" height="86" alt="image" src="https://github.com/user-attachments/assets/6d151746-ee4f-488c-90f2-e9d990f867e9" />

<img width="945" height="132" alt="image" src="https://github.com/user-attachments/assets/01ff2838-51ef-4704-a987-20b2c1a758e3" />

### Résultat attendu
- Accès à un shell Linux interactif.
- Le conteneur apparaît comme arrêté après la sortie.

## 5. Étape 4 : Comprendre la structure d’une commande docker run

### Description  
Analyse de la structure générale d’une commande `docker run`.

### Commande exécutée

<img width="945" height="81" alt="image" src="https://github.com/user-attachments/assets/13f32d82-8b30-43d0-af32-7ae4a2c8f77e" />

### Analyse de la commande `docker run`

- `-d` : exécution du conteneur en mode détaché (arrière-plan)
- `--name demo-nginx` : attribution d’un nom explicite au conteneur
- `-p 8080:80` : redirection du port 8080 de l’hôte vers le port 80 du conteneur
- `nginx` : image Docker utilisée pour créer le conteneur

## 6. Étape 5 : Préparation du projet mlops-lab-01

### Description  
Cette étape consiste à se positionner dans le projet MLOps existant et à vérifier la structure minimale requise ainsi que le bon fonctionnement de l’API en local.

### Arborescence minimale attendue

mlops-lab-01/
├── data/
├── logs/
├── models/
├── registry/
└── src/

### Vérification de l’API

<img width="945" height="271" alt="image" src="https://github.com/user-attachments/assets/780c7ff1-6bc1-43ff-81b8-1cdf1781f2d2" />

<img width="945" height="406" alt="image" src="https://github.com/user-attachments/assets/d52c67df-5bd7-4109-9140-4657b3ecd3ae" />

## 7. Étape 6 : Création du fichier requirements.txt

### Description  
Cette étape permet de définir l’ensemble des dépendances Python nécessaires à l’exécution de l’API churn dans l’image Docker.

### Dépendances principales

<img width="569" height="380" alt="image" src="https://github.com/user-attachments/assets/2482cde7-5a36-4076-bf76-39e25540f44c" />


## 8. Étape 7 : Création du Dockerfile

### Description  
Le Dockerfile définit les différentes étapes nécessaires à la construction de l’image Docker de l’API churn.

### Objectifs du Dockerfile
- Définir une image de base Python
- Installer les dépendances Python
- Copier le code source de l’application
- Exposer le port 8000
- Lancer l’API FastAPI

<img width="935" height="639" alt="image" src="https://github.com/user-attachments/assets/17570623-318b-43a8-9d36-060ceeaf57d4" />

---

## 9. Étape 8 : Vérification du modèle actif

### Description  
Avant la construction de l’image Docker, il est indispensable de vérifier qu’un modèle entraîné est disponible et défini comme modèle courant.

### Vérifications effectuées
- Contenu du dossier `models/`
  
<img width="945" height="247" alt="image" src="https://github.com/user-attachments/assets/8e92ed33-bc55-4671-92e5-b255b3fb04c8" />

## 10. Étape 9 : Construction de l’image Docker

### Description  
Cette étape consiste à construire l’image Docker de l’API churn à partir du Dockerfile.

### Commandes exécutées

<img width="932" height="289" alt="image" src="https://github.com/user-attachments/assets/ad9f9170-7173-45c1-bcd3-9c61a40f9f5c" />

<img width="945" height="286" alt="image" src="https://github.com/user-attachments/assets/67d1de07-7dbc-45f3-a308-f258fe520a40" />


### Résultat attendu  
L’image `churn-api` apparaît dans la liste des images Docker locales.

## 11. Étape 10 : Lancement de l’API churn dans un conteneur

### Description  
L’API FastAPI est lancée dans un conteneur Docker basé sur l’image construite précédemment.

<img width="945" height="47" alt="image" src="https://github.com/user-attachments/assets/0baeb1f1-c62a-4047-bd4f-b3fbaf59101b" />


### Tests effectués
- Endpoint `/health`
  
<img width="945" height="448" alt="image" src="https://github.com/user-attachments/assets/0981c13f-4f01-485e-a80c-4e7e8852a701" />

- Endpoint `/predict`

<img width="945" height="367" alt="image" src="https://github.com/user-attachments/assets/a33c22a7-c54c-4ab6-ad2d-418d08b0f010" />
<img width="945" height="394" alt="image" src="https://github.com/user-attachments/assets/35fa676b-7890-461b-b64b-b8c1a1e75cb3" />

## 12. Étape 11 : Vérification des logs du conteneur

### Description  
Cette étape permet d’analyser les logs générés par l’API lors de son exécution dans le conteneur.

### Commandes exécutées
<img width="945" height="55" alt="image" src="https://github.com/user-attachments/assets/ea012872-1f62-483b-89f7-3928cdcaef4b" />

<img width="945" height="78" alt="image" src="https://github.com/user-attachments/assets/fca47fd1-0441-496c-bf2b-9c0dd81582d3" />

<img width="945" height="79" alt="image" src="https://github.com/user-attachments/assets/931ca8d3-7e73-48af-a0ec-5205588aa705" />

## 13. Étape 12 : Orchestration locale avec Docker Compose

### Description  
Docker Compose est utilisé afin de faciliter l’orchestration et la gestion du service churn-api.

<img width="804" height="537" alt="image" src="https://github.com/user-attachments/assets/db65a36f-0601-4e28-9f26-b4a9c8463129" />

---

## 14. Étape 13 : Démarrage de l’API avec Docker Compose

### Description  
Le service churn-api est démarré via Docker Compose et testé comme précédemment.

### Commandes exécutées

<img width="945" height="311" alt="image" src="https://github.com/user-attachments/assets/bf635b71-a289-4ac0-ae6a-73ae037946d2" />

<img width="945" height="223" alt="image" src="https://github.com/user-attachments/assets/9c7abe03-007a-4586-9a56-595f9100eb02" />

---

## 15. Étape 14 : Lancer les services en arrière-plan et observer les logs

### Description  
Cette étape consiste à lancer les services en mode détaché et à observer les logs en temps réel pendant l’exécution des requêtes.

### Commandes exécutées

<img width="945" height="97" alt="image" src="https://github.com/user-attachments/assets/41ed3c66-3ed8-4bed-8025-1e08b67a295d" />

<img width="945" height="100" alt="image" src="https://github.com/user-attachments/assets/008426d7-aa7f-4be4-a348-f045d131d7ca" />

<img width="945" height="423" alt="image" src="https://github.com/user-attachments/assets/5d422e79-21b6-4251-a16c-db33bad06f20" />

- Tests des endpoints `/health` et `/predict`
  
<img width="945" height="394" alt="image" src="https://github.com/user-attachments/assets/3f5f3f02-7a92-4d22-8976-04bd117da42e" />
<img width="945" height="448" alt="image" src="https://github.com/user-attachments/assets/cc99489e-093b-4238-8636-19f3a08e52d5" />


- docker compose down

<img width="945" height="139" alt="image" src="https://github.com/user-attachments/assets/b014d6b0-1183-4628-92e3-0154ad6d1416" />


### Résultat attendu
- Les services s’exécutent en arrière-plan.
- Les logs s’affichent en temps réel lors des appels à l’API.
- Les services sont correctement arrêtés.

## 16. Étape 15 : Lier Docker Compose au reste du cours (Git + DVC)

### Description  
Cette étape permet de relier le lab Docker aux autres briques du cours MLOps, notamment Git et DVC. L’objectif est de montrer que l’API churn s’inscrit désormais dans un environnement MLOps cohérent, versionné et reproductible.

### Vérifications préalables  
Avant de continuer, il est nécessaire de s’assurer que :
- le projet **mlops-lab-01** est versionné avec **Git** (lab Git),
- les données et les modèles volumineux sont suivis avec **DVC** (lab DVC),
- l’API est conteneurisée à l’aide de **Docker** et orchestrée avec **Docker Compose** (lab Docker).

### Ajout des fichiers Docker au versionnement Git  
Les fichiers nécessaires à la conteneurisation doivent être ajoutés au dépôt Git.

#### Commandes exécutées

<img width="1043" height="163" alt="image" src="https://github.com/user-attachments/assets/1e437e4c-2d89-448e-8756-c2e05a38a908" />

## Conclusion

Ce lab a permis de mettre en place un environnement MLOps local en combinant Git, DVC et Docker. La conteneurisation de l’API churn et son orchestration avec Docker Compose assurent un déploiement reproductible, une meilleure portabilité et une traçabilité complète du code, des données et des modèles.
