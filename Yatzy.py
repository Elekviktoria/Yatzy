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

class POINTS:
    def __init__(self, type_:str):         #Endast till för att kunna göra changeability, antagligen ineffektivt, se senare.
        self.changeability = True
        self.type_=type_
        
    def give(self):
        for i in self.categories:
            
            

class PLAYER:
    
    def __init__(self):
        self.dices = np.array([DIE("1"), DIE("2"), DIE("3"), DIE("4"), DIE("5")])    #så att jag kan kalla på't och har dem fysiskt
        self.categories = {POINTS("ettor"):0, POINTS("tvåor"):0, POINTS("treor"):0, POINTS("fyror"):0, POINTS("femmor"):0, POINTS("sexor"):0
                            POINTS("tretal"):0, POINTS("fyrtal"):0, POINTS("liten stege"):0, POINTS("stor stege"):0, POINTS("kåk"):0, POINTS("chans"):0, POINTS("yatzy"):0}
        
    def ask(self):
        """Asks the player to input a list of numbers, locks/unlocks the corresponding dice."""    
        
        x = list(map(int, input("\nSkriv vilka tärningar du vill låsa, 1 - 5, med mellanslag : ").strip().split()))[:5]
        
        for element in x:
            self.dices[element - 1].hold = not(self.dices[element - 1].hold)
       
        for i in range(2):
            for dice in self.dices:
                dice.roll_die()
        
        self.points()
        self.reset()
            
    def points(self):
        self.which = input("Kategori? Ettor, tvåor, kåk, o.s.v").lower()
        
        if self.categories().self.chageability == True
            
            if 
            
            """else: 
                self.categories[self.which] = 0 and self.categories[self.which].self.changeability = False"""
        
        else:
            print("choose another")
            points()
        
    def reset_dice(self):
        
        for i in self.dices:
            self.dices[i].hold = False 
            
        self.ask()
    
class START:
    
    def __init__(self):
        self.antal()
        self.getname()
        self.players = [PLAYER() for _ in range(self.antal_spelare)]
    
    def new_round(self):
        self.reset_dice()
        for i in self.categories:
            self.categories(i).self.changeability = True
    
    def antal(self):
        print("Hur många spelare?")
        self.antal_spelare = int(input())
        
    def getname(self):
        for i in range(self.antal_spelare):
            self.name = str(input("What player {}'s name? ".format(i+1)))

                
Game = START()
print(Game.players[0].ask())