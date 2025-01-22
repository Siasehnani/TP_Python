class Rectangle:
    
    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur
    
    def calculer_surface(self):
        surface=self.largeur*self.hauteur
        print("la surface de rectangle est :",surface)
    
    def calculer_perimetre(self):
        perimetre=self.largeur+self.hauteur
        print("le perimetre de rectangle est :",perimetre)
    
rect1=Rectangle(5,4)
rect2=Rectangle(6,8)

rect1.calculer_perimetre()
rect2.calculer_surface()
    