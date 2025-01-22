class Personne:

   def __init__(self,prenom):
      
      self.prenom = prenom
      self.amis=[]
    
   def ajouter_amis(self,ami):
      self.amis.append(ami)
      print(f"'{ami.prenom}' est ajouté au liste des amis de '{self.prenom}' ")
 
   def afficher_amis(self):
      if not self.amis:
         print("liste est vide")
      else:
       print(f"Liste des amis de '{self.prenom}' :")
      for index, ami in enumerate(self.amis, start=1):
       print(f"{index}. {ami.prenom}")


p1=Personne("Basma")
p2=Personne("Soumaya")
p3=Personne("Nour elhouda")
p4=Personne("Aya")

p1.ajouter_amis(p3)
p4.ajouter_amis(p2)
p3.afficher_amis()
p1.afficher_amis()
p4.afficher_amis()