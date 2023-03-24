import numpy as np


def dice():
    for i in range(3):
        dice = np.random.randint(1,7, size=5)
        print("Dice: ({},{},{},{},{})".format(dice[0], dice[1], dice[2], dice[3], dice[4]))
        index = list(map(int, input("\nEnter the numbers : ").strip().split()))[:5]
  
        print("\nList is - ", index)
        
        
dice()