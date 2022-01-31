#..............cena.....att......arm...
trgovina = {
"Dagger":      [  8,     4,       0],
"Shortsword":  [ 10,     5,       0],
"Warhammer":   [ 25,     6,       0],
"Longsword":   [ 40,     7,       0],
"Greataxe":    [ 74,     8,       0],
"Leather":     [ 13,     0,       1],
"Chainmail":   [ 31,     0,       2],
"Splintmail":  [ 53,     0,       3],
"Bandedmail":  [ 75,     0,       4],
"Platemail":   [102,     0,       5],
"Damage +1":   [ 25,     1,       0],
"Damage +2":   [ 50,     2,       0],
"Damage +3":   [100,     3,       0],
"Defense +1":  [ 20,     0,       1],
"Defense +2":  [ 40,     0,       2],
"Defense +3":  [ 80,     0,       3],
}
orozja = {"Dagger", "Shortsword", "Warhammer", "Longsword", "Greataxe"}
oklepi = {"Leather", "Chainmail", "Splintmail", "Bandedmail", "Platemail", "Nothing"}
prstani = {"Damage +1", "Damage +2", "Damage +3", "Defense +1", "Defense +2", "Defense +3", "Nothing"}

class Enota:
    def __init__(self, hp, attack, armor):
        self.hp = hp
        self.att = attack
        self.arm = armor

    def oprema(self, attack, armor):
        self.att += attack
        self.arm += armor

    def napad(self, other):
        skoda = self.att - other.arm
        skoda = max(skoda, 1)
        other.hp -= skoda
        return other.hp <= 0


class Igra:
    def __init__(self, predmeti):
        self.junak = Enota(100, 0, 0)
        self.boss = Enota(103, 9, 2)

        for predmet in predmeti:
            _, at, ar = trgovina[predmet]
            self.junak.oprema(at, ar)
        
        print(predmeti)
        self.borba()
    
    def borba(self):
        na_vrsti = 0

        while True:
            if na_vrsti == 0:
                if self.junak.napad(self.boss):
                    print("Zmaga junaka, prezivel je z ", self.junak.hp)
                    self.zmagovalec = 0
                    break
            else:
                if self.boss.napad(self.junak):
                    print("Zmaga bossa, prezivel je z ", self.boss.hp)
                    self.zmagovalec = 1
                    break
            
            na_vrsti = 1 - na_vrsti



min_cena = 1000
min_oprema = []

max_cena = 0
max_oprema = []

for w in orozja:
    for a in oklepi:               
        for r1 in prstani:
            for r2 in prstani:

                oprema = [w]
                if a != "Nothing":
                    oprema.append(a)
                if r1 != "Nothing":
                    oprema.append(r1)
                if r2 != "Nothing" and r2 != r1:
                    oprema.append(r2)
                


                igra = Igra(oprema)
                cena = sum([trgovina[predmet][0] for predmet in oprema])

                if igra.zmagovalec == 0:
                    if cena < min_cena:
                        min_cena = cena
                        min_oprema = oprema
                else:
                    if cena > max_cena:
                        max_cena = cena
                        max_oprema = oprema
                
                    

print("NAJBOLJ UGODNA ZMAGA:", min_cena, min_oprema)
print("NAJBOLJ POTRATNI PORAZ:", max_cena, max_oprema)
