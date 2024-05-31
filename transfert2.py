import os
import shutil
import uuid

def trouver_index_html_et_modifier(racine='.'):
    chemins_index_html = []
    for dossier, sous_dossiers, fichiers in os.walk(racine):
        for fichier in fichiers:
            if fichier == 'index.html':
                chemin_relatif = os.path.relpath(os.path.join(dossier, fichier), racine)
                chemins_index_html.append(chemin_relatif)
    
    # Traiter chaque fichier trouvé
    for chemin in chemins_index_html:
        chemin_complet = os.path.join(racine, chemin)
        
        # Copier le fichier original
        dossier_parent = os.path.basename(os.path.dirname(chemin_complet))
        nom_fichier = f"{dossier_parent}_original_{uuid.uuid4()}.html"
        chemin_copie = os.path.join(racine, nom_fichier)
        shutil.copy(chemin_complet, chemin_copie)
        
        with open(chemin_complet, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
        
        # Les chaînes à chercher et remplacer
        a_chercher = [
            'href="/bucoli'
        ]
        a_remplacer_par = 'href="'
        
        # Effectuer les remplacements
        for chaine in a_chercher:
            contenu = contenu.replace(chaine, a_remplacer_par)
        
        # Écrire les modifications dans le fichier original
        with open(chemin_complet, 'w', encoding='utf-8') as fichier:
            fichier.write(contenu)
    
    return chemins_index_html

# Exemple d'utilisation
chemins = trouver_index_html_et_modifier()
for chemin in chemins:
    print(chemin)