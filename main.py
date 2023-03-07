from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
# navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))


print("""
Bricks-Buyer  Copyright (C) 2023  Linares Julien
This program comes with ABSOLUTELY NO WARRANTY; for details look at README.md and LICENSE files.
This is free software, and you are welcome to redistribute it
under certain conditions; for details look at README.md and LICENSE files.""")




with open("mdp.txt", "r") as mdp:
    email, mdp = mdp.readlines(0)[0].split("|")


def timer_define(lien):
    #Cette fonction sert à enregistrer le temps restant avant la fin du décompte
    navigateur = webdriver.Firefox(service=Service("geckodriver.exe"))
    navigateur.implicitly_wait(20)
    navigateur.get(lien)
    if navigateur.find_element(By.NAME, "email") and navigateur.find_element(By.NAME, "password"):
        print("connection en cours...")
        navigateur.find_element(By.NAME, "email").send_keys(email)
        navigateur.find_element(By.NAME, "password").send_keys(mdp)
        connecté = False #variable servant pour tout les while unique (genre seulment pour les while ou ont y rentre une seule fois)
        while connecté != True:
            for bouton in navigateur.find_elements(By.TAG_NAME, "button"):
                if bouton.text == "Login" or bouton.text == "Se connecter":
                    bouton.click()
                    print("connecté ;)")
                    connecté = True
        connecté = False
        while connecté != True:
                for boutonprop in navigateur.find_elements(By.TAG_NAME, "a"):
                    try:
                        if boutonprop.get_property('href') == "https://app.bricks.co/properties":
                            boutonprop.click()
                            print("Menu Propriété")
                            connecté = True
                            break
                    except:
                        pass
        connecté = False
        while connecté != True:
                for boutonlien in navigateur.find_elements(By.TAG_NAME, "a"):
                    try:
                        if boutonlien.get_property('href') == lien:
                            boutonlien.click()
                            print("Propriété trouvé")
                            connecté = True
                            break
                    except:
                        pass
                    
    else:
        print("déja connecté")

    print("En attente de l'apparition du boutton achat...")
    connecté = False
    while connecté != True:
            for boutonachat in navigateur.find_elements(By.TAG_NAME, "button"):
                try:
                    if boutonachat.get_property('title') == "Achat de Bricks" or boutonachat.get_property('title') == "Buy bricks":
                        boutonachat.click()
                        print("bouton achat présent")
                        connecté = True
                        break
                except:
                    pass
    connecté = False
    while connecté != True:
            for caseb in navigateur.find_elements(By.TAG_NAME, "input"):
                try:
                    if caseb.get_property('name') == "quantity":
                        caseb.send_keys(nbbricks)
                        print("nb bricks rentré")
                        connecté = True
                        break
                except:
                    pass
    connecté = False
    while connecté != True:
            for boutonaachat in navigateur.find_elements(By.TAG_NAME, "button"):
                try:
                    if boutonaachat.get_property('title') == "Acheter {} bricks".format(nbbricks) or boutonaachat.get_property('title') == "Acheter {} brick".format(nbbricks) or boutonaachat.get_property('title') == "Purchase {} brick".format(nbbricks) or boutonaachat.get_property('title') == "Purchase {} bricks".format(nbbricks):
                        boutonaachat.click()
                        print("acheté")
                        connecté = True
                        break
                except:
                    pass
    print("Fin de la v0,5")

lienause = input("lien: ")
nbbricks = input("Nombre de bricks: ")
timer_define(lienause)