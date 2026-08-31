# Gestion Solaire Intelligente des Volets (Home Assistant)

**Blueprint avancé pour Home Assistant** qui automatise la position des volets roulants par calcul trigonométrique de la course du soleil (azimut et élévation).

## ⭐ Fonctionnalités Clés
- **📐 Géométrie Pure :** Calcul en temps réel de l'ombre en fonction de l'orientation (`Of`), de la largeur (`Lf`) et de la profondeur du tableau (`Pf`) de la baie vitrée.
- **📊 Paliers Dynamiques :** Découpage progressif de la course entre le bas de vitre (`Pmin`) et 100 % d'ouverture.
- **🛡️ Protection Sieste & Somfy My :** Ignore automatiquement les volets positionnés sous un seuil minimal configurable (par défaut 20 %) pour préserver la position favorite "My" (15 %) ou les réglages manuels.
- **🌅 Gestion Matinale & Fin de Cycle :** Options personnalisables pour libérer les volets le matin selon les pièces ou adopter une position de sortie spécifique (`ExitPos`) lorsque le soleil quitte la zone.

## 📥 Installation
### Méthode 1 : Via HACS (Recommandé)
1. Ajoutez ce dépôt comme **Custom Repository** dans HACS :
   - **Repository URL** : `https://github.com/guillaumefleuru-rgb/ha-shutters-sun-mgmt`
   - **Type** : `Integration`
2. Installez l'intégration via HACS → **Integrations** → **Explore & Download**.
3. Votre blueprint sera disponible dans **Paramètres → Automatisations & Scènes → Blueprints**.

### Méthode 2 : Import direct
Cliquez sur le badge ci-dessous pour importer directement ce Blueprint :

[![Ouvrir Home Assistant et importer le Blueprint](https://my.home-assistant.io/badges/blueprint_import.svg)](https://my.home-assistant.io/redirect/blueprint_import/?repository_url=https://github.com/guillaumefleuru-rgb/ha-shutters-sun-mgmt)

## 📖 Configuration
Voir le fichier [example.yaml](blueprints/example.yaml) pour un exemple complet de configuration.

## 🤝 Contribuer
Les contributions sont les bienvenues ! Ouvrez une issue ou une pull request sur [GitHub](https://github.com/guillaumefleuru-rgb/ha-shutters-sun-mgmt).
