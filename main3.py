from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Dictionnaire des réponses connues pour chaque question
reponses_connues = {
    "L'installation d'applications ou de jeux sur mobile doit être effectuée depuis un store officiel.": "Vrai",
    "Lorsqu'un collaborateur quitte une entreprise": "Supprimé",
    "Pour empêcher le vol du Mot de Passe, il faut une authentification": "Multiple",
    "La sécurisation de la messagerie": "URL",
    "Les informations personnelles des collaborateurs": "Sécurisées",
    "Il est fortement recommandé d'accéder au SI": "Professionnel",
    "Si je perds mon mobile": "Mon RSSI",
    "La Cybersécurité a pour rôle": "Modifier",
    "Un antivirus fonctionne sur": "Annuaire",
    "Un cyberpirate élabore des": "Logiciels",
    "Un antivirus protège": "Faux",
    "TOR est un": "Réseau informatique",
    "Un antivirus fait en sorte": "Repérer",
    "Chaque logiciel mal": "Signature",
    "Laquelle de ces": "Le nom et prénom d'une personne",
    "Pour protéger les données de ses clients, Orange": "Sensibiliser les salariés",
}

# reponses_connues = {
#     "Vrai": "Vrai",   # Exemple avec une réponse de type "Faux"
#     "Question 1": "Réponse A",
#     "Question 2": "Réponse B",
#     "Question 3": "Réponse D",  # Exemple avec une réponse de type "Vrai"
#
# }

time_sleep = 0.2

def sleep(time_sleep):
    time.sleep(time_sleep)


# Initialiser le driver
driver = webdriver.Chrome()

# Ouvre la page du challenge Kahoot
driver.get('https://kahoot.it/challenge/01770076?challenge-id=b33c347a-b0a1-47a0-a1af-d7938a01ddd7_1726732150588&authuser=0')

# Attendre que la page soit chargée
wait = WebDriverWait(driver, 60)

def safe_click(wait, by_selector, retries=3, vrai_faux=1, reponse=None):
    """Fonction pour réessayer un clic plusieurs fois si l'élément devient obsolète"""
    for i in range(retries):
        try:
            element = wait.until(EC.element_to_be_clickable(by_selector))
            element.click()
        except Exception as e:
            if i == retries - 1:
                print(f"Erreur après plusieurs tentatives : {e}")
                return False
            print(f"Réessai {i + 1} pour l'élément {by_selector}")
            time.sleep(0.5)  # Attente entre les essais

# Boucle principale pour parcourir toutes les questions
while True:
    try:
        # Extraire le texte de la question courante
        question_text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-functional-selector="block-title"]')))
        question_text = question_text_element.text

        question_trouvee = False
        print(question_text)
        for question in reponses_connues.keys():
            if question in question_text:
                question_trouvee = True
                question_in_dict = question
                print("trouvé")
                break

        # Si la question courante est dans ton dictionnaire des réponses
        if question_trouvee:  # question_text in reponses_connues:
            print(1)
            # Récupérer la réponse correcte attendue
            bonne_reponse = reponses_connues[question_in_dict]
            print(bonne_reponse)

            # Gérer les réponses de type "Vrai" ou "Faux"
            if bonne_reponse.lower() == "vrai":
                safe_click(wait, (By.CSS_SELECTOR, '[data-functional-selector="answer-0"]'))

            elif bonne_reponse.lower() == "faux":
                safe_click(wait, (By.CSS_SELECTOR, '[data-functional-selector="answer-1"]'))

            else:
                print(4)
                # Extraire les réponses disponibles pour d'autres types de questions
                reponses_possibles = driver.find_elements(By.CSS_SELECTOR, '[data-functional-selector^="answer-"]')

                # Parcourir les réponses et cliquer sur celle qui correspond à la bonne réponse
                for reponse in reponses_possibles:
                    texte_reponse = reponse.find_element(By.CSS_SELECTOR, 'p').text  # Sélectionne le texte de la réponse
                    print(texte_reponse)
                    if texte_reponse.lower() == bonne_reponse.lower():
                        # sleep(time_sleep)
                        retries = 3
                        for i in range(retries):
                            try:
                                reponse.click()
                            except Exception as e:
                                if i == retries - 1:
                                    print(f"Erreur après plusieurs tentatives : {e}")
                                    break
                                print(f"Réessai {i + 1} pour l'élément {reponse}")
                                time.sleep(0.5)  # Attente entre les essais
                        break  # Sortir de la boucle une fois la bonne réponse cliquée
                print(4.1)
        # Cliquer sur le bouton "Suivant" après avoir répondu
        suivant_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="next-button"]')))
        time.sleep(0.5)
        suivant_button.click()

        suivant_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="score-next-button"]')))
        time.sleep(3)
        suivant_button.click()

    except Exception as e:
        print(f"Erreur rencontrée: {e}")
        # break  # Sortir de la boucle si une erreur est rencontrée (fin des questions par exemple)

# Fermer le driver après avoir parcouru toutes les questions
driver.quit()



# <button class="button__Button-sc-c6mvr2-0 drKTqe scoreboard__Button-sc-ryzpjh-7 cttZOj" data-functional-selector="score-next-button" type="button">Suivant</button>