class Voiture:

    def __init__(self, marque,modl,annee):
       
        self.marque = marque
        self.modl = modl
        self.annee = annee

    def afficher_info(self):
        print("la marque de voiture est:",self.marque)
        print("le modele de voiture est:",self.modl)
        print("l'annee de voiture est:",self.annee)


V1=Voiture("renaut","clio",2018)
V2=Voiture("mercedes","gclass",2020)
V3=Voiture("Hyundai","i10",2013)


V1.afficher_info()
print("-----------------------------------")
V2.afficher_info()
print("------------------------------------")
V3.afficher_info()

