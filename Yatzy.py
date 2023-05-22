import numpy as np

class DIE:
    def __init__(self, die_name: str):
        self.die_name = die_name
        self.hold = False
        self.value = 0

    def __repr__(self):
        return "Die: {}, value: {}".format(self.die_name, self.value)

    def roll_die(self):
        """Rolls the dice if they are not locked by the player."""
        if not self.hold:
            self.value = np.random.randint(1, 7)
        print("Die {}, value: {}".format(self.die_name, self.value))


class PLAYER:
    def __init__(self):
        self.rounds = 0
        self.dices = np.array([DIE("1"), DIE("2"), DIE("3"), DIE("4"), DIE("5")])
        self.categories = {
            "ettor": -1,
            "tvåor": -1,
            "treor": -1,
            "fyror": -1,
            "femmor": -1,
            "sexor": -1,
            "tretal": -1,
            "fyrtal": -1,
            "liten stege": -1,
            "stor stege": -1,
            "kåk": -1,
            "chans": -1,
            "yatzy": -1,
        }
        self.num = {"ettor": 1, "tvåor": 2, "treor": 3, "fyror": 4, "femmor": 5, "sexor": 6}
        self.ask()

    def ask(self):
        """Asks the player what dice to lock, checks if it is the last (13:th) round, and if so, tallies the score.
        Initiates the point funktion and the reset_dice funktion."""
        a = [
            self.categories["ettor"], self.categories["tvåor"], self.categories["treor"], self.categories["fyror"], 
            self.categories["femmor"], self.categories["sexor"], self.categories["tretal"], self.categories["fyrtal"],
            self.categories["liten stege"], self.categories["stor stege"], self.categories["kåk"], self.categories["chans"],
            self.categories["yatzy"]
            ]
        score_help = np.array(a)
        
        if self.rounds == 13:
            if self.categories["ettor"] + self.categories["tvåor"] + self.categories["treor"] + self.categories["fyror"] + self.categories["femmor"] + self.categories["sexor"] >= 63:
                score_score = np.sum(score_help) + 50
                print(f"Slut! Grattis, du fick bonusen. Dina poäng är {score_score}")
            else:
                print(f"Slut! Dina poäng är {np.sum(score_help)}")

        else:
            self.rounds += 1
            for i in range(2):
                for dice in self.dices:
                    dice.roll_die()

                x = list(map(int, input("\nSkriv vilka tärningar du vill låsa, 1 - 5, med mellanslag: ").strip().split()))[:5]

                for element in x:
                    self.dices[element - 1].hold = not self.dices[element - 1].hold
            
            for dice in self.dices:
                dice.roll_die()

            self.points()
            print(self.categories)
            self.reset_dice()    
            
    def points(self):
        """Takes in a string and matches it to the categories' dictionary. Checks if the player has the dice
        for the string, and gives points if so."""
        currentvals = np.zeros(5)

        for i, dice in enumerate(self.dices):
            currentvals[i] = dice.value

        print(f"Currentvals is {currentvals}")
        
        self.which = input("Kategori? Ettor, tvåor, kåk, o.s.v: ").lower()

        
        if self.categories[self.which] == -1:
            self.categories[self.which] = 0

            if self.which in ["ettor", "tvåor", "treor", "fyror", "femmor", "sexor"]:
                for i in self.dices:
                    if i.value == self.num[self.which]:
                        self.categories[self.which] += self.num[self.which]
                print(f"{self.which} har värde: {self.categories[self.which]}")

                        
            elif self.which == "yatzy":
                for i in range(1, 7):
                    if np.count_nonzero(currentvals == i) > 4:                        
                        self.categories[self.which] += 50
                print(f"Yatzy har värde: {self.categories[self.which]}")

                        
            elif self.which == "tretal":
                for i in range(1,7):
                    if np.count_nonzero(currentvals == i) > 2:
                        self.categories[self.which] = np.sum(currentvals)
                print(f"Tretal har värde: {self.categories[self.which]}")

            elif self.which == "fyrtal":
                for i in range(1,7):
                    if np.count_nonzero(currentvals == i) > 3:
                        self.categories[self.which] = np.sum(currentvals)
                print(f"Fyrtal har värde: {self.categories[self.which]}")

            elif self.which == "kåk":
                for i in range(1, 7):
                    if np.count_nonzero(currentvals == i) == 3:
                        for j in range(1, 7):
                            if np.count_nonzero(currentvals == j) == 2:
                                self.categories[self.which] = 25
                print(f"Kåk har värde: {self.categories[self.which]}")


            elif self.which == "chans":
                self.categories[self.which] += np.sum(currentvals)
                print(f"Chans har värde: {self.categories[self.which]}")

            
            elif self.which == "stor stege":
                lista = [self.dices[i].value for i in range(5)]
                a = lista.sort()
                storted = np.array(lista)
                if np.allclose(storted, [2, 3, 4, 5, 6]) or np.allclose(storted, [1, 2, 3, 4, 5]):
                    self.categories[self.which] += 40
                print(f"Stor stege har värde: {self.categories[self.which]}")
            
            elif self.which == "liten stege":
                if np.count_nonzero(currentvals == 1) > 0 and np.count_nonzero(currentvals == 2) > 0 and np.count_nonzero(currentvals == 3) > 0 and np.count_nonzero(currentvals == 4) > 0:
                    self.categories[self.which] += 30
                elif np.count_nonzero(currentvals == 2) > 0 and np.count_nonzero(currentvals == 3) > 0 and np.count_nonzero(currentvals == 4) > 0 and np.count_nonzero(currentvals == 5) > 0:
                    self.categories[self.which] += 30
                elif np.count_nonzero(currentvals == 3) > 0 and np.count_nonzero(currentvals == 4) > 0 and np.count_nonzero(currentvals == 5) > 0 and np.count_nonzero(currentvals == 6) > 0:
                    self.categories[self.which] += 30
                print(f"Liten stege har värde: {self.categories[self.which]}")

            else:
                pass
        else:
            print("Välj annan kategori")
            self.points()

    def reset_dice(self):
        """Resets dice so that they can be rolled again."""
        for dice in self.dices:
            dice.hold = False
        self.ask()


class START:
    def __init__(self):
        self.antal_spelare = 1
        self.name = ""
        self.players = []
        self.getname()
        self.players = [PLAYER() for _ in range(self.antal_spelare)]
        
    def getname(self):
        """Collects the name of the player, just to be welcoming."""
        for i in range(self.antal_spelare):
            self.name = str(input("Vad heter du?"))
            print("Välkommen till Elsas yatzy!")


start_game = START()
