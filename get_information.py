from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import json
import os
import random

time_sleep = 0.2




def add_new_information(titre, question, reponse):
    # Vérifier si le fichier existe, sinon créer un dictionnaire vide
    if not os.path.exists("information.json"):
        with open("information.json", "w", encoding="utf-8") as fichier:
            json.dump({}, fichier)

    # Charger le fichier JSON pour ajouter la nouvelle entrée
    with open("information.json", "r", encoding="utf-8") as fichier:
        donnees_existantes = json.load(fichier)

    # Initialiser 'titre' s'il n'existe pas encore
    if titre not in donnees_existantes:
        donnees_existantes[titre] = {}

    # Ajouter la nouvelle question au sous-dictionnaire 'titre'
    donnees_existantes[titre].update({question: reponse})

    # Enregistrer les données dans un fichier JSON
    with open("information.json", "w", encoding="utf-8") as fichier:
        json.dump(donnees_existantes, fichier, indent=4, ensure_ascii=False)

    # Vérifier le contenu du fichier (affichage pour l'exemple)
    print(json.dumps(donnees_existantes, indent=4, ensure_ascii=False))


def sleep(time_sleep):
    time.sleep(time_sleep)


def get_title():
    try:
        # Attendre jusqu'à ce que l'élément <h1> avec la classe spécifiée soit visible
        h1_element = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, 'h1.block-title__Title-sc-1kt4e1p-0.jGllbp')))

        # Récupérer le texte de l'élément <h1>
        h1_text = h1_element.text
        print(f"Texte trouvé : {h1_text}")
        return h1_text
    except Exception as e:
        print(f"Erreur rencontrée: {e}")
        return "Titre_non_trouvé"


def login(name="test1.0"):
    # Action 1 : Vérifier et cliquer sur "Jouer dans le navigateur" si présent
    try:
        jouer_btn = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Jouer dans le navigateur')]"))
        )
        time.sleep(1)
        jouer_btn.click()
    except:
        print("Bouton 'Jouer dans le navigateur' non trouvé, passage à l'action suivante.")

    # Action 2 : Entrer le pseudo dans le champ de texte
    pseudo_input = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.ID, "nickname"))
    )
    pseudo_input.send_keys(name)  # Remplacez "MonPseudo" par le pseudo souhaité

    # Action 3 : Cliquer sur le bouton de confirmation
    join_btn = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-functional-selector='join-button-username']"))
    )
    join_btn.click()
    
def click():
    try:
        # Localiser l'élément contenant les boutons
        button_container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                        '#challenge-game-router > div > div > main > div.styles__Wrapper-sc-42g9v0-1.fQeiMP.question-choices__QuestionChoices-sc-vfgbd-0.eAybHt')))

        # Trouver le premier bouton dans le conteneur
        button = button_container.find_element(By.TAG_NAME,
                                               'button')  # Assure-toi que les boutons sont des éléments <button>

        # Cliquer sur le bouton
        button.click()
        print("Bouton cliqué.")

    except Exception as e:
        print(f"Erreur rencontrée: {e}")

def get_reponse():
    try:
        # Récupérer le texte de la première réponse (non désactivée)
        element = driver.find_element(By.XPATH,
                                      "//div[@type='button' and not(@disabled)]//span[contains(@class, 'question-choice-content__QuestionChoiceText-sc')]//p")

        # Obtenir le texte
        texte_reponse = element.text
        return texte_reponse
    except Exception:
        print("ce n'est pas une question à choix multiple")

    try:
        # Attendre que les éléments soient présents
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'card__PassiveCard-sc-lblpdo-0'))
        )

        # Récupérer le texte de l'élément qui est la bonne réponse
        bonne_reponse_element = driver.find_element(By.XPATH,
                                                    "//div[@data-functional-selector='answer-1' and not(@disabled)]")
        bonne_reponse_texte = bonne_reponse_element.find_element(By.TAG_NAME, 'p').text

        print("La bonne réponse est :", bonne_reponse_texte)
        return bonne_reponse_texte

    except Exception as e:
        print("Une erreur s'est produite :", e)
        return None

def main():

    login(str(random.random())[2:])

    # titre = get_title()

    titre = url

    # Boucle principale pour parcourir toutes les questions
    while True:
        try:
            # Extraire le texte de la question courante
            question_text_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-functional-selector="block-title"]')))
            question_text = question_text_element.text

            sleep(1)

            click()

            sleep(1)

            bonne_reponse = get_reponse()

            add_new_information(titre, question_text, bonne_reponse)


            # Cliquer sur le bouton "Suivant" après avoir répondu
            suivant_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="next-button"]')))
            time.sleep(0.5)
            suivant_button.click()

            suivant_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="score-next-button"]')))
            time.sleep(3)
            suivant_button.click()

            time.sleep(1)

            try:
                # Vérifier si l'élément est présent
                titre_element = driver.find_element(By.XPATH,
                                                    "//header[contains(@class, 'styles__TopContent-sc-468pf5-0')]//h1[text()='Tableau des scores']")

                # Si l'élément est trouvé, sortir de la boucle
                print("Titre trouvé : ", titre_element.text)
                break
            except NoSuchElementException:
                # Si l'élément n'est pas trouvé, attendre un peu avant de vérifier à nouveau
                print("Titre non trouvé, vérification prochaine...")

        except Exception as e:
            print(f"Erreur rencontrée: {e}")
            # break  # Sortir de la boucle si une erreur est rencontrée (fin des questions par exemple)

if __name__ == "__main__":

    url = 'https://kahoot.it/challenge/09333972?challenge-id=b33c347a-b0a1-47a0-a1af-d7938a01ddd7_1729147448495&authuser=4'
    # Initialiser le driver
    driver = webdriver.Chrome()

    # Ouvre la page du challenge Kahoot
    driver.get(url)

    # Attendre que la page soit chargée
    wait = WebDriverWait(driver, 60)


    main()