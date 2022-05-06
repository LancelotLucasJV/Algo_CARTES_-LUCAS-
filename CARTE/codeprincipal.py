class Carte:
    def __init__(self):
        self.cardtype = [1,2,3]

    def nameofcard(self) :
        if(self.cardtype)[1]:
            print("monstre")
        if(self.cardtype)[2]:
            print ("cristal")
        if(self.cardtype)[3]:
            print ("blast")
        
    def description(self):
        if(self.cardtype)[1]:
            print("Une carte monstre, pouvant attaquer joueur et autre monstres, est defausser quand ses PV atteigne 0")
        if(self.cardtype)[2]:
            print ("augmente la mana, reste dans la zone de jeu")
        if(self.cardtype)[3]:
            print ("inflige des dégats à un joueur ou un monstre, puis est defausser")

        
    def cardeffect(self):

        self.estsurleterrain = True, False
        self.peutattaquer = True, False
        self.donneMana = True, False
        self.peutmourir = True, False
        self.prixmana 
        if(self.cardtype)[1]: self.prixmana = 50
        if (self.cardtype)[2]: self.prixmana = 30
        if (self.cardtype)[2]: self.prixmana = 100
                

    def cardfunction(self):
        if(self.cardtype)[1]:
            D
        if (self.cardtype)[2]:
            D
        if (self.cardtype)[3]:
            print(self._valeur, end=" ")
        else:
            print("X", end=" ")
 

class Mage:
    def __init__(self, name ):
        self.playername = name
        self.MaxMana = 500
        self.MaxPv = 500
    def mort(self) :
        if self.MaxPv : 0
        print ("Défaite.")



class Jeu:
    def __init__(self)
    
