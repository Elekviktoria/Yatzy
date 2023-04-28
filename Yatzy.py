import numpy as np
    
class DIE:
    
    value = 7
    
    def __init__(self, namn: str):
        self.namn=namn
        self.roll_die()
        self.hold = False
        
    def roll_die(self):
        if self.hold == False:
            self.value = np.random.randint(1,7)
            print(self.value)
        else:
            pass

class PLAYER:
    
    def __init__(self):
        self.dices = np.array([DIE("d1"), DIE("d2"), DIE("d3"), DIE("d4"), DIE("d5")])    #så att jag kan kalla på't och har dem fysiskt
        self.points_siffror = {"ettor":0, "tvåor":0, "treor":0, "fyror":0, "femmor":0, "sexor":0} # en dictionary kan nog funka bra
        self.points_extra = {"tretal":0, "fyrtal":0, "liten stege":0, "stor stege":0, "kåk":0, "chans":0, "yatzy":0}
        
    def ask(self):
        
        x = list(map(int, input("\nEnter the numbers 1 - 5: ").strip().split()))[:5]
        for element in x:
            hold.dices[element - 1] = not(hold.dices[element - 1])

        ### vi gör detta några gånger
    """self.dices[index - 1].hold = not(self.dices[index - 1])
        for dice in self.dices:
            dice.roll_die()"""
        
        
class START:
    
    def __init__(self):
        self.antal()
        self.getname()
        self.players = [PLAYER() for _ in range(self.antal_spelare)]
    
    def antal(self):
        print("Hur många spelare?")
        self.antal_spelare = int(input())
        
    def getname(self):
        for i in range(self.antal_spelare):
            self.name = str(input("What is your name?"))

                
Game = START()
print(Game.players[0].ask())
