class Chien:

    def __init__(self, nom, race, age):
       
        self.nom = nom
        self.race = race
        self.age = age

    def aboyer(self):
        print("wooof!")
mon_chien=Chien("LIFO","Berg alm","10")
mon_chien.aboyer()

