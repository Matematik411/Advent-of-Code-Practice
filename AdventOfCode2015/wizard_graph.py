from queue import PriorityQueue

# This is day22 - works for both parts
spells = {
"missile": 53, # It instantly does 4 damage. 
"drain": 73, # It instantly does 2 damage and heals you for 2 hit points.
"shield": 113, # Effect: 6 turns. While it is active, your armor is increased by 7.
"poison": 173, # Effect: 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
"recharge": 229, # Effect: 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
}

class Unit:
    def __init__(self, hp, attack, armor, mana, effects):
        self.hp = hp
        self.att = attack
        self.arm = armor
        self. mana = mana
        self.ef = effects

    def basic_attack(self, other):
        dmg = self.att - other.arm
        dmg = max(dmg, 1)
        other.hp -= dmg
        return other.hp <= 0

    def spell(self, other, name):
        self.mana -= spells[name]
        if name == "missile":
            other.hp -= 4
        elif name == "drain":
            self.hp += 2
            other.hp -= 2
        elif name == "shield":
            self.ef[name] = 6
        elif name == "poison":
            other.ef[name] = 6
        else:
            self.ef[name] = 5
        
        return other.hp <= 0
    
    def effects(self):
        for name, timer in self.ef.items():
            if name == "shield":
                if timer > 1:
                    self.arm = 7
                else:
                    self.arm = 0
            elif name == "poison":
                self.hp -= 3
            elif name == "recharge":
                self.mana += 101

            self.ef[name] -= 1
        
        self.ef = {e:t for e, t in self.ef.items() if t > 0}
        return self.hp <= 0
            
    def __str__(self):
        s = "Unit(" + str(self.hp) + ", " + str(self.att) + ", " + str(self.arm) + ", " + str(self.mana) + ", " + str(self.ef) + ")"
        return s


def round(hero, boss, spent, part_two):
    outputs = []

    if part_two:
        hero.hp -= 1
        if hero.hp <= 0:
            return outputs

    hero.effects()
    if boss.effects():
        outputs.append((spent, "END"))

    
    for spell, cost in spells.items():
        if hero.mana >= cost and spell not in hero.ef and spell not in boss.ef:
            h_e = {e:t for e, t in hero.ef.items()}
            b_e = {e:t for e, t in boss.ef.items()}
            # print("cost", cost)
            p1 = Unit(hero.hp, hero.att, hero.arm, hero.mana, h_e) # new branch
            p2 = Unit(boss.hp, boss.att, boss.arm, boss.mana, b_e)
            result = p1.spell(p2, spell) # hero casts spell

            if result: # boss dies
                outputs.append((spent + cost, "END"))
            else: # boss lives
                p1.effects()
                if p2.effects(): # boss dies
                    outputs.append((spent + cost, "END"))
                    continue

                result = p2.basic_attack(p1) # boss attacks
                if result: # hero dies
                    continue
                else: # hero lives
                    # print(spent + cost, p1, p2)
                    outputs.append((spent + cost, (p1, p2)))
                    
    
    return outputs


start_hero = Unit(50, 0, 0, 500, {})
start_boss = Unit(71, 10, 0, 0, {})

counter = 0
pq = PriorityQueue()
pq.put((0, counter, (start_hero, start_boss)))
counter += 1
while not pq.empty():
    c, _,  x = pq.get()
    if x == "END":
        print(c)
        break

    new = round(x[0], x[1], c, True) #trigger last for part two
    for a, b in new:
        pq.put((a, counter, b))
        counter += 1
