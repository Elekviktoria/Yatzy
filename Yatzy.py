import numpy as np
    
class DIE:
    
    value = 7
    hold = False
    
    def __init__(self, namn: str):
        self.namn=namn
        self.roll_die()
        
        
    def roll_die(self):
        if self.hold == False:
            self.value = np.random.randint(1,7)
            print(self.value)
        else:
            pass

class PLAYERS:
    
    antal_spelare = 0
    dices = np.array([DIE("d1"), DIE("d2"), DIE("d3"), DIE("d4"), DIE("d5")])
    points_siffror = {"ettor":0, "tvåor":0, "treor":0, "fyror":0, "femmor":0, "sexor":0}
    points_extra = {"tretal":0, "fyrtal":0, "liten stege":0, "stor stege":0, "kåk":0, "chans":0, "yatzy":0}
    
    def __init__(self,name):
        self.name=name
    
        
    def antal(self):
        antal_spelare = input(int("Hur många spelare?"))
        
    def getname(self):
        for i in range(antal_spelare):
            self.name = input(str("What is your name?"))
        
class START:
    def __init__(self):
        
    def ask():
        index = list(map(int, input("\nEnter the numbers 0 - 4: ").strip().split()))[:5]
        print("\nList is - ", index)
