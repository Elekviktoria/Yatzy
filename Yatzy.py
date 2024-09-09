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
        else:
            print("Stava bättre")
            self.points()
