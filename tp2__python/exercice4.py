class Personne:

   def __init__(self,nom,prenom,age):

        self.nom=nom
        self.prenom=prenom
        self.age=age
    
   def se_presenter(self):
        print(f"Bonjour, je me présente : {self.nom} {self.prenom}, {self.age} ans.")
     

##sous_class
class Etudiant(Personne):
    def __init__(self, nom, prenom, age,matricule):
        # Appeler le constructeur de la classe parent
        super().__init__(nom, prenom,age)
        self.matricule=matricule
    def etudier(self):
        print(f"Je suis l'étudiant(e) {self.prenom} {self.nom}, matricule {self.matricule}, et je suis en train d'étudier.")

P1=Personne("Assia","SEHNANI",23)
P2=Personne("ELRHIRAKI","BASMA",20)
E1=Etudiant("NMER","NOUR ELHOUDA",20,"123456")
E2=Etudiant("TOUMZEN","SOUMAYA",24,"234165")
E3=Etudiant("JABRANE","AYA",21,"765489")

print("            ***************             " )
P1.se_presenter()
print("---------------------------------------------------")
E1.etudier()
print("----------------------------------------------------------")
E3.se_presenter()
print("----------------------------------------------------------")
E2.etudier()