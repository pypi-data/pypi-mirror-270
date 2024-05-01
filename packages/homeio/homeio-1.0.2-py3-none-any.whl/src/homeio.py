import requests

class ConnexionHomeIO:
    def __init__(self, serveur="localhost", port=9797):
        self.serveur = serveur
        self.port = port

    def tester_connexion(self):
        url = f"http://{self.serveur}:{self.port}/poll"
        try:
            reponse = requests.get(url)
            if reponse.status_code == 200:
                print("Connexion réussie !")
            else:
                print(f"Échec de la connexion: {reponse.status_code} !")
        except requests.ConnectionError:
            print("Impossible de se connecter au serveur !")

class Lumiere:
    def __init__(self, connexion, piece):
        self.connexion = connexion
        self.piece = piece

    def allumer(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/swl/allumer/{self.piece}"
        requests.get(url)

    def eteindre(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/swl/eteindre/{self.piece}"
        requests.get(url)

    def regler_intensite(self, intensite):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/stl/{self.piece}/{intensite}"
        requests.get(url)

class Chauffage:
    def __init__(self, connexion, piece):
        self.connexion = connexion
        self.piece = piece

    def allumer(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/swh/allumer/{self.piece}"
        requests.get(url)

    def eteindre(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/swh/eteindre/{self.piece}"
        requests.get(url)

    def regler_temperature(self, temperature):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/sth/{self.piece}/{temperature}"
        requests.get(url)

class Volet:
    def __init__(self, connexion, piece):
        self.connexion = connexion
        self.piece = piece

    def monter(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/strs/monter/{self.piece}"
        requests.get(url)

    def descendre(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/strs/descendre/{self.piece}"
        requests.get(url)

    def arreter(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/strs/stopper/{self.piece}"
        requests.get(url)

class Portail:
    def __init__(self, connexion, type_portail):
        self.connexion = connexion
        self.type_portail = type_portail

    def ouvrir(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/cgate/ouvrir/{self.type_portail}"
        requests.get(url)

    def fermer(self):
        url = f"http://{self.connexion.serveur}:{self.connexion.port}/cgate/fermer/{self.type_portail}"
        requests.get(url)
