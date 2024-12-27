# FusionPDFApp

FusionPDFApp est un outil convivial, écrit en Python avec Tkinter, qui permet aux utilisateurs de fusionner plusieurs fichiers PDF en un seul document de manière intuitive. Il inclut des fonctionnalités avancées telles que la gestion de l'ordre des fichiers PDF par glisser-déposer et une interface utilisateur simple à prendre en main.

## Fonctionnalités
- **Ajouter des fichiers PDF** : Sélectionnez plusieurs fichiers PDF à fusionner via une boîte de dialogue.
- **Réorganiser l'ordre** : Modifiez l'ordre des PDF avant la fusion en les faisant glisser et déposer dans la liste.
- **Supprimer des fichiers** : Retirez facilement un PDF de la liste.
- **Fusionner les fichiers** : Combinez tous les PDF sélectionnés dans un fichier unique.
- **Interface utilisateur intuitive** : Interface basée sur Tkinter, simple et efficace.

## Prérequis
Avant de lancer l'application, assurez-vous d'avoir les éléments suivants installés sur votre système :

- **Python 3.7 ou plus récent**
- **PyPDF2** : Pour manipuler les fichiers PDF
- **Tkinter** : Intégré avec Python par défaut dans la plupart des installations

Pour installer les dépendances, exécutez :
```bash
pip install PyPDF2
pip install tk (optionnel)
```

## Installation et exécution
1. Clonez ce dépôt ou téléchargez les fichiers sources.
2. Assurez-vous que toutes les dépendances sont installées.
3. Lancez le script principal :
```bash
python fusion_pdf.py
```

## Guide d'utilisation
1. **Ajouter des fichiers PDF** : Cliquez sur le bouton "Ajouter des PDF" pour ouvrir une boîte de dialogue et choisir vos fichiers.
2. **Réorganiser les fichiers** : Cliquez sur un fichier dans la liste et faites-le glisser pour changer son emplacement.
3. **Supprimer un fichier** : Sélectionnez un fichier dans la liste et cliquez sur "Supprimer le PDF".
4. **Fusionner les fichiers** : Cliquez sur "Valider la Fusion", choisissez un emplacement pour sauvegarder le fichier fusionné, et laissez l'application effectuer la fusion.

## Structure du projet
```
ZeFusionPdf/
|-- fusion_pdf.py  # Code source principal
|-- README.md      # Documentation du projet
```

## Améliorations futures
- Ajout d'une option pour prévisualiser les fichiers PDF avant la fusion.
- Support pour d'autres opérations sur les PDF (comme la rotation ou l'extraction de pages).
- Traductions multilingues pour l'interface utilisateur.

## Contribution
Les contributions sont les bienvenues ! Si vous avez des suggestions, ouvrez une "issue" ou soumettez une "pull request". Assurez-vous que votre code est propre et bien documenté.

## Licence
Ce projet est sous licence MIT. Consultez le fichier [LICENSE](LICENSE) pour plus de détails.

---

Merci d'utiliser ZeFusionPdf ! Si vous rencontrez des problèmes, n'hésitez pas à signaler un bug ou à poser vos questions.

