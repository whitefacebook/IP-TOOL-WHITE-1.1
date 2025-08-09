# IP-TOOL-WHITE-1.1
**infoTools.py** est un script Python interactif conçu pour **Termux** (Android) ou tout environnement Linux.  
Il offre un ensemble d’outils pour la collecte d’informations réseau et système, adaptés à la **cybersécurité éthique** et à l’apprentissage.

## ✨ Fonctionnalités

### Outils Réseau
- 📍 **Localiser une IP** (géolocalisation avec Google Maps link)
- 🌐 **Voir votre IP publique**
- 🛰 **Traceroute**
- 📡 **Ping**
- 🔍 **Whois lookup**

### Outils Système & Réseau (nouveau)
- `ifconfig` → Voir IP locale et interfaces réseau
- `netstat` → Connexions réseau actives
- `ss` → Ports ouverts
- `arp -a` → Table ARP (appareils connectés en local)
- `uptime` → Temps depuis le dernier démarrage
- `top` → Utilisation CPU/RAM en temps réel
- `df -h` → Utilisation du stockage
- `du -sh` → Taille d’un dossier
- `whoami` → Utilisateur actuel
- `uname -a` → Infos système

## 📥 Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/whitefacebook/IP-TOOL-WHITE-1.1.git
cd <TON-DEPOT>

2. Installer les dépendances

pkg update && pkg upgrade
pkg install python
pkg install traceroute
pkg install net-tools
pkg install iproute2
pkg install whois
pip install colorama requests

3. Rendre le script exécutable

chmod +x infoTools.py


▶️ Utilisation

Méthode exécutable :


./infoTools.py

Méthode classique :


python infoTools.py

Naviguez dans le menu et sélectionnez les outils souhaités.
Appuyez sur Entrée pour revenir au menu après chaque action.


⚠️ Avertissement légal

Cet outil est conçu uniquement pour des fins éducatives, d’audit interne, ou de pentest avec autorisation explicite.
L’auteur n’est pas responsable de toute mauvaise utilisation.
