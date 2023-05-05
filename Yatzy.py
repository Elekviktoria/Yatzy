import numpy as np
    
class DIE:
    
    value = 7
    
    def __init__(self, die_name: str):
        self.die_name=die_name
        self.hold = False
        self.roll_die()
    
    def __repr__(self):
        return "Die: {}, value: {}".format(self.die_name, self.value)
    
    def roll_die(self):
        """Rolls the dice, if the attribute "hold" is false, which is determined by the players 
        after the first round. Also prints the numbers of the dice."""
    
        if self.hold == False:
            self.value = np.random.randint(1,7)
            print("Die {}, value: {}".format(self.die_name, self.value))
        else:
            print("Die {}, value: {}".format(self.die_name, self.value))

class PLAYER:
    
    def __init__(self):
        self.dices = np.array([DIE("1"), DIE("2"), DIE("3"), DIE("4"), DIE("5")])    #så att jag kan kalla på't och har dem fysiskt
        self.points_siffror = {"ettor":0, "tvåor":0, "treor":0, "fyror":0, "femmor":0, "sexor":0} # en dictionary kan nog funka bra
        self.points_extra = {"tretal":0, "fyrtal":0, "liten stege":0, "stor stege":0, "kåk":0, "chans":0, "yatzy":0}
        
    def ask(self):
        """Asks the player to input a list of numbers, locks/unlocks the corresponding dice."""    
        
        x = list(map(int, input("\nEnter which dice to lock, 1 - 5, with spaces between: ").strip().split()))[:5]
        
        for element in x:
            self.dices[element - 1].hold = not(self.dices[element - 1].hold)
       
        for i in range(2):
            for dice in self.dices:
                dice.roll_die()
        
        self.points()
        self.reset()
            
    def points(self):
        if self.dices[0].value == self.dices[1].value and self.dices[0].value == self.dices[2].value 
        and self.dices[0].value == self.dices[3].value and self.dices[0].value == self.dices[4].value:
            self.points_extra = 
                
    def reset_dice(self):
        for i in self.dices:
            self.dices[i].hold = False
        self.ask()
    
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
            self.name = str(input("What player {}'s name? ".format(i+1)))

                
Game = START()
print(Game.players[0].ask())