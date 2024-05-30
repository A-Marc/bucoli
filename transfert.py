import re

def modifier_liens_html(input_file, output_file):
    # Lire le contenu du fichier HTML en tant qu'une chaîne de caractères
    with open(input_file, 'r', encoding='utf-8') as f:
        texte = f.read()

    # Utilisation d'une expression régulière pour trouver les liens href dans le texte HTML
    pattern = r'href="/([^"]+)"'
    texte_modifie = re.sub(pattern, r'href="\1.html"', texte)

    # Écrire le texte modifié dans un nouveau fichier
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(texte_modifie)

# Exemple d'utilisation
modifier_liens_html('index.html', 'index_modifie.html')