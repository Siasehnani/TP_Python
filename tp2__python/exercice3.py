class Comptebancaire:

    def __init__(self,titu,solde):
       
        self.titulaire = titu
        self.solde = solde

    def deposer(self,montant):
        if montant>0:  
            self.solde+=montant
            print("le depot de montant est réussi :",self.solde)
        else:
            print("erreur!le montant doit etre positif")
    
    def retirer(self,montant):
        if montant<=self.solde:
            self.solde-=montant
        else:
            print("le solde est insuffisant!!")
    
    def affichsolde(self):
        print("Votre solde est:",self.solde)
    
compte1=Comptebancaire("SEHNANI_ASSIA",1200)
compte2=Comptebancaire("NMER_NOUR ELHOUDA",4000)

compte1.deposer(200)
compte2.retirer(6000)       
compte2.affichsolde()
compte1.affichsolde()


