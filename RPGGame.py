import random
import time

class Player:
    def __init__(self, Name):
        self.name = Name
        self.health = 12
    
    def Attack(self, enemy):
        dmg = random.randrange(1, 6)
        if random.randrange(1, 10) == 10:
            dmg = dmg * 2
            print(f"{self.name} HIT A CRITICAL")
        enemy.health -= dmg
        print(f"{self.name} attacked {enemy.name} for {dmg}. {enemy.name} has {enemy.health} hp")
    
    def Heal(self):
        healed = random.randrange(1, 6)
        print(f"{self.name} healed {healed} hp")
        self.health += healed
        print(f"{self.name} has {self.health} hp")
                 
class Enemy(Player):
    def __init__(self, Name, lv):
        self.name = Name
        self.health = 12 + (lv - 1)
    
    def AttackAI(self, enemy):
        choice = random.randrange(1, 3)
        if choice == 1:
            super().Attack(enemy)
        else:
            super().Heal()

You = Player(input("What is your name?\n"))

EnemyNames = ["Goblin", "Skeleton", "Orc", "Bandit", "Rat King"]

RoundNum = 1
while You.health > 0:
    Opp = Enemy(EnemyNames[random.randrange(1, len(EnemyNames))], RoundNum)
    
    print(f"ROUND {RoundNum}\n{Opp.name} VS {You.name}\nStart!!! ")
    
    while You.health > 0 and Opp.health > 0:
        choice = int(input(f"Do you wanna \nheal(1) \nfight(2)\n"))
        if choice == 1:
            You.Heal()
        elif choice == 2:
            You.Attack(Opp)
        else:
            print(f"Invalid choice {You.name} skipped their turn")

        time.sleep(.5)
        Opp.AttackAI(You)
    
    if You.health > 0:
        print(f"You win")
        RoundNum += 1

print(f"You fell after defeating {RoundNum - 1} enemies")