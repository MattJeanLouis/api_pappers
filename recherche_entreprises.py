import os
import requests
from dotenv import load_dotenv

load_dotenv()

SUGGESTIONS_URL = "https://suggestions.pappers.fr/v2"

def recherche_entreprises(q, longueur=10, cibles="nom_entreprise"):
    params = {
        "q": q,
        "longueur": longueur,
        "cibles": cibles
    }
    
    response = requests.get(SUGGESTIONS_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur: {response.status_code}")
        print(f"Détails de l'erreur : {response.text}")
        return None

def afficher_resultats(resultats):
    for cible, entreprises in resultats.items():
        print(f"\nRésultats pour {cible}:")
        for entreprise in entreprises:
            print(f"- {entreprise.get('nom_entreprise', 'N/A')} (SIREN: {entreprise.get('siren', 'N/A')})")

def main():
    print("Recherche d'entreprises avec l'API Pappers")
    
    q = input("Entrez le début de votre recherche : ")
    longueur = int(input("Nombre de résultats (max 100) : "))
    cibles = input("Cibles de la recherche (séparées par des virgules) : ")
    
    resultats = recherche_entreprises(q, longueur, cibles)
    
    if resultats:
        afficher_resultats(resultats)
    else:
        print("Aucun résultat trouvé.")

if __name__ == "__main__":
    main()