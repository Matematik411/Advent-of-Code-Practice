class Enota:
    def __init__(self, hp, attack, armor, mana, stanje):
        self.hp = hp
        self.att = attack
        self.arm = armor
        self.mana = mana
        self.stanje = stanje  # [("scit", 3)]

    def napad(self, other):
        skoda = self.att - other.arm
        skoda = max(skoda, 1)
        other.hp -= skoda
        return other.hp <= 0
    
    def raketa(self, other):
        self.mana -= 53
        other.hp -= 4
        return other.hp <= 0

    def izcrpavanje(self, other):
        self.mana -= 73
        other.hp -= 2
        self.hp += 2
        return other.hp <= 0

    def scit_spr(self):
        self.mana -= 113
        self.stanje["scit"] =  6

    def scit_ef(self, cas):
        if cas == 6:
            self.arm += 7
        elif cas == 1:
            self.arm -= 7
        return cas - 1

    def polnjenje_spr(self):
        self.mana -= 229
        self.stanje["polnjenje"] =  5

    def polnjenje_ef(self, cas):
        self.mana += 101
        return cas - 1
    
    def strup_spr(self, other):
        self.mana -= 173
        other.stanje["strup"] = 6 

    def strup_ef(self, cas):
        self.hp -= 3
        return (self.hp <= 0, cas - 1)



class Igra:
    def __init__(self, hp1, arm1, mana1, stanje1, hp2, stanje2, skupno):


        self.junak = Enota(hp1, 0, arm1, mana1, stanje1)
        self.boss = Enota(hp2, 10, 0, 0, stanje2)
        self.skupno = skupno
        self.konec = False

        self.efekti()

    def efekti(self):
        
        if "scit" in self.junak.stanje:
            preostalo = self.junak.scit_ef(self.junak.stanje["scit"])
            if preostalo == 0:
                del self.junak.stanje["scit"]
            else:
                self.junak.stanje["scit"] = preostalo - 1


        if "polnjenje" in self.junak.stanje:
            preostalo = self.junak.polnjenje_ef(self.junak.stanje["polnjenje"])
            if preostalo == 0:
                del self.junak.stanje["polnjenje"]
            else:
                self.junak.stanje["polnjenje"] = preostalo - 1
        
        if "strup" in self.boss.stanje:
            rez = self.boss.strup_ef(self.boss.stanje["strup"])
            if rez[0]:
                self.konec = True
            if rez[1] == 0:
                del self.boss.stanje["strup"]
            else:
                self.boss.stanje["strup"] = rez[1] - 1
        
    
    def borba(self):
        if self.konec:
            return self.skupno
        min_poraba = 10000

        #junak
        for i in range(5):
            
            if i == 0 and self.junak.mana >= 53:
                

                junak_nov = Enota(self.junak.hp, 0, self.junak.arm, self.junak.mana, self.junak.stanje)
                boss_nov = Enota(self.boss.hp, 10, 0, 0, self.boss.stanje)

                if junak_nov.raketa(boss_nov):
                    min_poraba = min(self.skupno + 53, min_poraba)
                else:
                    self.efekti()
                    if self.konec:
                        return self.skupno + 53
                    if not boss_nov.napad(junak_nov):
                        print("aaaaaaaaa", self.skupno)
                        nova = Igra(
                            junak_nov.hp, 
                            junak_nov.arm,
                            junak_nov.mana,
                            junak_nov.stanje,
                            boss_nov.hp,
                            boss_nov.stanje,
                            self.skupno + 53)
                        nova.borba()
                        print("asdasd", nova.skupno)
                        min_poraba = min(nova.skupno, min_poraba)
                

            elif i == 1 and self.junak.mana >= 73:
                junak_nov = Enota(self.junak.hp, 0, self.junak.arm, self.junak.mana, self.junak.stanje)
                boss_nov = Enota(self.boss.hp, 10, 0, 0, self.boss.stanje)
                
                if junak_nov.izcrpavanje(boss_nov):
                    min_poraba = min(self.skupno+73, min_poraba)
                else:
                    self.efekti()
                    if self.konec:
                        return self.skupno + 73
                    if not boss_nov.napad(junak_nov):
                        print("aaaaaaaaa", self.skupno)
                        nova = Igra(
                            junak_nov.hp, 
                            junak_nov.arm,
                            junak_nov.mana,
                            junak_nov.stanje,
                            boss_nov.hp,
                            boss_nov.stanje,
                            self.skupno+73)
                        nova.borba()
                        print("asdasd", nova.skupno)
                        min_poraba = min(nova.skupno, min_poraba)
            

            elif i == 2 and self.junak.mana >= 113 and "scit" not in self.junak.stanje:
                junak_nov = Enota(self.junak.hp, 0, self.junak.arm, self.junak.mana, self.junak.stanje)
                boss_nov = Enota(self.boss.hp, 10, 0, 0, self.boss.stanje)
                
                junak_nov.scit_spr()
                self.efekti()
                if self.konec:
                    return self.skupno + 113
                if not boss_nov.napad(junak_nov):
                    print("aaaaaaaaa", self.skupno)
                    nova = Igra(
                        junak_nov.hp, 
                        junak_nov.arm,
                        junak_nov.mana,
                        junak_nov.stanje,
                        boss_nov.hp,
                        boss_nov.stanje,
                        self.skupno+113)
                    nova.borba()
                    print("asdasd", nova.skupno)
                    min_poraba = min(nova.skupno, min_poraba)
            

            elif i == 3 and self.junak.mana >= 173 and "strup" not in self.boss.stanje:
                junak_nov = Enota(self.junak.hp, 0, self.junak.arm, self.junak.mana, self.junak.stanje)
                boss_nov = Enota(self.boss.hp, 10, 0, 0, self.boss.stanje)

                junak_nov.strup_spr(boss_nov)
                self.efekti()
                if self.konec:
                    return self.skupno + 173
                if not boss_nov.napad(junak_nov):
                    print("aaaaaaaaa", self.skupno)
                    nova = Igra(
                        junak_nov.hp, 
                        junak_nov.arm,
                        junak_nov.mana,
                        junak_nov.stanje,
                        boss_nov.hp,
                        boss_nov.stanje,
                        self.skupno+173)
                    nova.borba()
                    print("asdasd", nova.skupno)
                    min_poraba = min(nova.skupno, min_poraba)
            

            elif i == 4 and self.junak.mana >= 229 and "polnjenje" not in self.junak.stanje:
                junak_nov = Enota(self.junak.hp, 0, self.junak.arm, self.junak.mana, self.junak.stanje)
                boss_nov = Enota(self.boss.hp, 10, 0, 0, self.boss.stanje)

                junak_nov.polnjenje_spr()
                self.efekti()
                if self.konec:
                    return self.skupno + 229
                print("asdasdasdasdasd", self.junak.stanje, self.boss.stanje)
                if not boss_nov.napad(junak_nov):
                    print("aaaaaaaaa", self.skupno)
                    nova = Igra(
                        junak_nov.hp, 
                        junak_nov.arm,
                        junak_nov.mana,
                        junak_nov.stanje,
                        boss_nov.hp,
                        boss_nov.stanje,
                        self.skupno+229)
                    nova.borba()
                    print("asdasd", nova.skupno)
                    min_poraba = min(nova.skupno, min_poraba)

        self.skupno = min_poraba
        print(self.junak.stanje, self.boss.stanje)
        return min_poraba












        # self.skupno += 53
        # if self.junak.raketa(self.boss):
        #     print("Zmaga junaka, prezivel je z ", self.junak.hp)
        #     self.zmagovalec = 0

        # #boss
        # if self.boss.napad(self.junak):
        #     print("Zmaga bossa, prezivel je z ", self.boss.hp)
        #     self.zmagovalec = 1


igra = Igra(50, 0, 500, {}, 71, {},  0)
igra.borba()
print(igra.skupno)

