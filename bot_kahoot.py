import tkinter as tk
from tkinter import ttk
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

time_sleep = 0.2
time_next1 = 0.5
time_next2 = 1
url = 'https://kahoot.it/challenge/01770076?challenge-id=b33c347a-b0a1-47a0-a1af-d7938a01ddd7_1726732150588&authuser=0'


# Fonction pour lancer le bot après les configurations
def lancer_bot():
    print(
        f"Lancement du bot avec les temps : time_sleep={time_sleep}, time_next1={time_next1}, time_next2={time_next2}")
    root.destroy()

    def sleep(time_sleep):
        if time_sleep != 0:
            time.sleep(time_sleep)

    # Initialiser le driver
    driver = webdriver.Chrome()

    # Ouvre la page du challenge Kahoot
    driver.get(url)

    # Attendre que la page soit chargée
    wait = WebDriverWait(driver, 120)

    # Boucle principale pour parcourir toutes les questions
    while True:
        try:
            # Extraire le texte de la question courante
            question_text_element = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-functional-selector="block-title"]')))
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
            if question_trouvee:
                print(1)
                # Récupérer la réponse correcte attendue
                bonne_reponse = reponses_connues[question_in_dict]
                print(bonne_reponse)

                # Gérer les réponses de type "Vrai" ou "Faux"
                if bonne_reponse.lower() == "vrai":
                    print(2)
                    # Cliquer sur le bouton "Vrai"
                    vrai_button = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="answer-0"]')))
                    sleep(time_sleep)
                    vrai_button.click()
                    print(2.1)

                elif bonne_reponse.lower() == "faux":
                    print(3)
                    # Cliquer sur le bouton "Faux"
                    faux_button = wait.until(
                        EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="answer-1"]')))
                    sleep(time_sleep)
                    faux_button.click()
                    print(3.1)

                else:
                    print(4)
                    # Extraire les réponses disponibles pour d'autres types de questions
                    reponses_possibles = driver.find_elements(By.CSS_SELECTOR, '[data-functional-selector^="answer-"]')

                    # Parcourir les réponses et cliquer sur celle qui correspond à la bonne réponse
                    for reponse in reponses_possibles:
                        try:
                            # Essayer de récupérer le texte de la réponse
                            texte_reponse = reponse.find_element(By.CSS_SELECTOR, 'p').text
                            print(f"Réponse trouvée : {texte_reponse}")

                            if texte_reponse.lower() == bonne_reponse.lower():
                                reponse.click()
                                break  # Sortir de la boucle une fois la bonne réponse cliquée
                        except Exception as e:
                            print(f"Élément sans texte, peut-être une image. Erreur : {e}")
                            continue  # Ignorer cet élément et passer à la réponse suivante

                    print(4.1)

            # Cliquer sur le bouton "Suivant" après avoir répondu
            suivant_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="next-button"]')))
            time.sleep(time_next1)
            suivant_button.click()

            suivant_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[data-functional-selector="score-next-button"]')))
            time.sleep(time_next2)
            suivant_button.click()

        except Exception as e:
            print(f"Erreur rencontrée: {e}")
            break  # Sortir de la boucle si une erreur est rencontrée (fin des questions par exemple)

    # Fermer le driver après avoir parcouru toutes les questions
    driver.quit()


def next_step():
    global url
    url = link_entry.get()
    clear_frame()
    create_page2()


def add_question():
    question = question_entry.get()
    reponse = reponse_entry.get()
    if question and reponse:
        reponses_connues[question] = reponse
        question_entry.delete(0, tk.END)
        reponse_entry.delete(0, tk.END)
        print(f"Question ajoutée : {question} -> {reponse}")


def use_default_questions():
    print("Utilisation du dictionnaire de questions existant:", reponses_connues)
    next_step2()


def next_step2():
    clear_frame()
    create_page3()


def update_times():
    global time_sleep, time_next1, time_next2
    time_sleep = time_sleep_slider.get()
    time_next1 = time_next1_slider.get()
    time_next2 = time_next2_slider.get()
    print(f"Temps configurés : time_sleep={time_sleep}, time_next1={time_next1}, time_next2={time_next2}")
    lancer_bot()


def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()


def create_page1():
    global link_entry
    link_label = tk.Label(frame, text="Lien du Kahoot:")
    link_label.pack(pady=10)

    link_entry = tk.Entry(frame, width=50)
    link_entry.insert(0, url)
    link_entry.pack(pady=10)

    next_button = tk.Button(frame, text="Next", command=next_step)
    next_button.pack(pady=10)


def create_page2():
    global question_entry, reponse_entry
    question_label = tk.Label(frame, text="Question:")
    question_label.pack(pady=10)

    question_entry = tk.Entry(frame, width=50)
    question_entry.pack(pady=10)

    reponse_label = tk.Label(frame, text="Réponse:")
    reponse_label.pack(pady=10)

    reponse_entry = tk.Entry(frame, width=50)
    reponse_entry.pack(pady=10)

    add_button = tk.Button(frame, text="+", command=add_question)
    add_button.pack(pady=10)

    use_default_button = tk.Button(frame, text="Utiliser le dictionnaire", command=use_default_questions)
    use_default_button.pack(pady=10)

    next_button = tk.Button(frame, text="Next", command=next_step2)
    next_button.pack(pady=10)


def update_time_labels():
    time_sleep_label_value.config(text=f"Valeur : {time_sleep_slider.get():.2f}")
    time_next1_label_value.config(text=f"Valeur : {time_next1_slider.get():.2f}")
    time_next2_label_value.config(text=f"Valeur : {time_next2_slider.get():.2f}")


def create_page3():
    global time_sleep_slider, time_next1_slider, time_next2_slider
    global time_sleep_label_value, time_next1_label_value, time_next2_label_value

    time_sleep_label = tk.Label(frame, text="Temps de réaction (sec):")
    time_sleep_label.pack(pady=10)

    time_sleep_slider = tk.Scale(frame, from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL,
                                 command=lambda x: update_time_labels())
    time_sleep_slider.set(time_sleep)
    time_sleep_slider.pack(pady=10)

    time_sleep_label_value = tk.Label(frame, text=f"Valeur : {time_sleep:.2f}")
    time_sleep_label_value.pack(pady=10)

    time_next1_label = tk.Label(frame, text="Temps après la question (sec):")
    time_next1_label.pack(pady=10)

    time_next1_slider = tk.Scale(frame, from_=0, to=2, resolution=0.01, orient=tk.HORIZONTAL,
                                 command=lambda x: update_time_labels())
    time_next1_slider.set(time_next1)
    time_next1_slider.pack(pady=10)

    time_next1_label_value = tk.Label(frame, text=f"Valeur : {time_next1:.2f}")
    time_next1_label_value.pack(pady=10)

    time_next2_label = tk.Label(frame, text="Temps pour voir le podium (sec):")
    time_next2_label.pack(pady=10)

    time_next2_slider = tk.Scale(frame, from_=0, to=5, resolution=0.01, orient=tk.HORIZONTAL,
                                 command=lambda x: update_time_labels())
    time_next2_slider.set(time_next2)
    time_next2_slider.pack(pady=10)

    time_next2_label_value = tk.Label(frame, text=f"Valeur : {time_next2:.2f}")
    time_next2_label_value.pack(pady=10)

    launch_button = tk.Button(frame, text="Lancer le bot", command=update_times)
    launch_button.pack(pady=10)


# Création de la fenêtre principale
root = tk.Tk()
root.title("Kahoot Bot")
frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=10, pady=10)

create_page1()

# Lancer la boucle principale
root.mainloop()
