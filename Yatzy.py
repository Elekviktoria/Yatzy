import numpy as np
        
class DICE:
    
    def __init__(self, number:int, värde:int):
        self.number=number
        self.värde=värde
        
    def roll_dice(self):
        self.värde = np.random.randint(1,7)
        print(self.värde)

def ask():
    index = list(map(int, input("\nEnter the numbers 0 - 4: ").strip().split()))[:5]
    print("\nList is - ", index)
ask()
    
dice1 = DICE(1, 0)
dice2 = DICE(2, 0)
dice3 = DICE(3, 0)
dice4 = DICE(4, 0)
dice5 = DICE(5, 0)

import numpy as np

def dice():
        dice = np.random.randint(1,7, size=5)
        print("Dice: ({},{},{},{},{})".format(dice[0], dice[1], dice[2], dice[3], dice[4]))
        index = list(map(int, input("\nEnter the numbers 0 - 4: ").strip().split()))[:5]
  
        print("\nList is - ", index)
    
        for i in range(index):
            if index[i] == 

start = input("Start? ")       

if start == "yes":
    dice()
    
