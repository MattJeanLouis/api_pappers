import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

ENTREPRISE_URL = "https://api.pappers.fr/v2/entreprise"
API_TOKEN = os.getenv("API_TOKEN")

def obtenir_details_entreprise(siren):
    params = {
        "api_token": API_TOKEN,
        "siren": siren
    }
    
    response = requests.get(ENTREPRISE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Erreur: {response.status_code}")
        print(f"Détails de l'erreur : {response.text}")
        return None

def afficher_details(details, niveau=0, max_niveau=2):
    if niveau > max_niveau:
        return

    if isinstance(details, dict):
        for cle, valeur in details.items():
            if valeur is None:
                print("  " * niveau + f"{cle}: Non renseigné")
            elif isinstance(valeur, (dict, list)):
                print("  " * niveau + f"{cle}:")
                afficher_details(valeur, niveau + 1, max_niveau)
            else:
                print("  " * niveau + f"{cle}: {valeur}")
    elif isinstance(details, list):
        if not details:
            print("  " * niveau + "Aucun élément")
        else:
            for index, item in enumerate(details):
                print("  " * niveau + f"[{index}]:")
                afficher_details(item, niveau + 1, max_niveau)
    else:
        print("  " * niveau + str(details))

def main():
    print("Obtention des détails d'une entreprise avec l'API Pappers")
    
    siren = input("Entrez le numéro SIREN de l'entreprise : ")
    
    details = obtenir_details_entreprise(siren)
    
    if details:
        print("\nRésumé des informations principales :")
        infos_principales = {
            "nom_entreprise": details.get("nom_entreprise"),
            "siren": details.get("siren"),
            "forme_juridique": details.get("forme_juridique"),
            "adresse": details.get("siege", {}).get("adresse_ligne_1"),
            "code_postal": details.get("siege", {}).get("code_postal"),
            "ville": details.get("siege", {}).get("ville"),
            "activite": details.get("libelle_code_naf"),
            "date_creation": details.get("date_creation_formate"),
            "capital": details.get("capital_formate")
        }
        afficher_details(infos_principales, max_niveau=1)
        
        print("\nVoulez-vous voir toutes les informations détaillées ? (o/n)")
        reponse = input().lower()
        if reponse == 'o':
            print("\nInformations détaillées :")
            print(json.dumps(details, indent=2, ensure_ascii=False))
    else:
        print("Impossible d'obtenir les détails de l'entreprise.")

if __name__ == "__main__":
    main()