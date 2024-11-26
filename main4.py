from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
import json
import sys


def get_questionnaire(url):
    # Charger le fichier JSON
    with open("information.json", "r", encoding="utf-8") as fichier:
        donnees_existantes = json.load(fichier)

    # Vérifier si le dictionnaire associé à la clé 'test_bot' existe
    if url not in donnees_existantes:
        print(f"La clé {url} n'existe pas. Arrêt du programme.")
        sys.exit()  # Arrêter le programme si la clé n'existe pas

    # Récupérer le dictionnaire associé à la clé 'test_bot'
    reponses_connues = donnees_existantes[url]

    # Afficher le dictionnaire récupéré
    print(reponses_connues)

    return reponses_connues



# # Dictionnaire des réponses connues pour chaque question
# reponses_connues = {
#     "L'installation d'applications ou de jeux sur mobile doit être effectuée depuis un store officiel.": "Vrai",
#     "Lorsqu'un collaborateur quitte une entreprise": "Supprimé",
#     "Pour empêcher le vol du Mot de Passe, il faut une authentification": "Multiple",
#     "La sécurisation de la messagerie": "URL",
#     "Les informations personnelles des collaborateurs": "Sécurisées",
#     "Il est fortement recommandé d'accéder au SI": "Professionnel",
#     "Si je perds mon mobile": "Mon RSSI",
#     "La Cybersécurité a pour rôle": "Modifier",
#     "Un antivirus fonctionne sur": "Annuaire",
#     "Un cyberpirate élabore des": "Logiciels",
#     "Un antivirus protège": "Faux",
#     "TOR est un": "Réseau informatique",
#     "Un antivirus fait en sorte": "Repérer",
#     "Chaque logiciel mal": "Signature",
#     "Laquelle de ces": "Le nom et prénom d'une personne",
#     "Pour protéger les données de ses clients, Orange": "Sensibiliser les salariés",
# }

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



def qcm(wait):
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

            print(5)
            # Cliquer sur le bouton "Suivant" après avoir répondu
            suivant_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="next-button"]')))
            time.sleep(0.5)
            print('click suivent 1')
            suivant_button.click()

            print('teste tableau de score ')
            try:
                # # Vérifier si l'élément est présent
                # titre_element = WebDriverWait(driver, 3).until(
                #     EC.presence_of_element_located((By.XPATH,
                #                                     '//*[@id="challenge-game-router"]/div/div/div/main/div[4]/section'))
                # )

                print('suivant 2')
                suivant_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '[data-functional-selector="score-next-button"]')))
                time.sleep(1)
                print('click')
                suivant_button.click()

                # # Si l'élément est trouvé, sortir de la boucle
                # print("Titre trouvé : ", titre_element.text)
                # #

            except TimeoutException:
                print('fin')

                time.sleep(2000)

                driver.get(url)

                button_not_me = WebDriverWait(driver, 4).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR,
                                                    '#challenge-game-router > div > div > main > section > div > div > button.button__Button-sc-c6mvr2-0.cQlNsw.challenge-progress__Button-sc-vq0yn-4.drUTLz'))
                )
                time.sleep(1)
                button_not_me.click()
                break

            except Exception:


                # Si l'élément n'est pas trouvé, attendre un peu avant de vérifier à nouveau
                print("Titre non trouvé, vérification prochaine...")




        except Exception as e:
            print(f"Erreur rencontrée dans la boucle while: {e}")
            # break  # Sortir de la boucle si une erreur est rencontrée (fin des questions par exemple)


def navigateur():
    # Action 1 : Vérifier et cliquer sur "Jouer dans le navigateur" si présent
    try:
        jouer_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Jouer dans le navigateur')]"))
        )
        time.sleep(1)
        jouer_btn.click()
    except:
        print("Bouton 'Jouer dans le navigateur' non trouvé, passage à l'action suivante.")

def login(name):
    # Action 2 : Entrer le pseudo dans le champ de texte
    pseudo_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "nickname"))
    )

    pseudo_input.clear()  # Efface le contenu existant

    pseudo_input.send_keys(name)  # Remplacez "MonPseudo" par le pseudo souhaité

    time.sleep(1)

    # Action 3 : Cliquer sur le bouton de confirmation
    join_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-functional-selector='join-button-username']"))
    )
    join_btn.click()


def main(num_i):
    ustilisateur_reseaux = "lmarcepo"
    incremente = 1
    for i in range(num_i):

        # Ouvre la page du challenge Kahoot
        driver.get(url)

        # Attendre que la page soit chargée
        wait = WebDriverWait(driver, 60)

        navigateur()

        erreur = True
        while erreur:
            login(f"{ustilisateur_reseaux} {i + incremente}")

            try:
                # Attendre jusqu'à 1 seconde pour que le bouton soit visible et cliquable
                bouton = WebDriverWait(driver, 1).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="dialog"]/div/div[3]/button'))
                )
                bouton.click()  # Clique sur le bouton si trouvé

                incremente += 1
                print('bouton cliqué')
                time.sleep(1)
            except Exception as e:
                print("Bouton non trouvé ou non cliquable :", e)
                erreur = False

        qcm(wait)



if __name__ == "__main__":

    url = 'https://kahoot.it/challenge/09333972?challenge-id=b33c347a-b0a1-47a0-a1af-d7938a01ddd7_1729147448495&authuser=4'

    reponses_connues = get_questionnaire(url)

    # Initialiser le driver
    driver = webdriver.Chrome()

    main(1)


    # Fermer le driver après avoir parcouru toutes les questions
    driver.quit()

# <button class="button__Button-sc-c6mvr2-0 drKTqe scoreboard__Button-sc-ryzpjh-7 cttZOj" data-functional-selector="score-next-button" type="button">Suivant</button>