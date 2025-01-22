class livre:

    def __init__(self,titre,auteur,annee_pub):
        self.titre=titre
        self.auteur=auteur
        self.annee_pub=annee_pub
    
class bibliotheque:
  
    def __init__(self):
      
        self.livres = []
    def ajouter_livre(self,livre):
        self.livres.append(livre)
        print(f"le livre ' {livre } ' est ajouté au bibliothèque")

    def afficher_livres(self):
        if not self.livres:
            print("la bibliothèque est vide")
        else:
            print(f"les livres sont :'{self.livres}'")
    

livre1 = livre("Les Misérables","Victor Hugo",1862)
livre2 = livre("Harry Potter à l'école des sorciers","J.K. Rowling",1997)
livre3 = livre("La Peste","Albert Camus",1947)

bibliotheque = bibliotheque()

bibliotheque.ajouter_livre("Les Misérables")
bibliotheque.ajouter_livre("La Peste")
bibliotheque.afficher_livres()
