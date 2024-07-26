from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self, monster):
        pass

class Sword(Weapon):
    def attack(self, monster):
        print("Боец наносит удар мечом.")
        monster.health -= 10
        print(f"Монстр получает урон: {10}. Осталось здоровья: {monster.health}")

class Bow(Weapon):
    def attack(self, monster):
        print("Боец стреляет из лука.")
        monster.health -= 5
        print(f"Монстр получает урон: {5}. Осталось здоровья: {monster.health}")

class Fighter:
    def __init__(self, name, weapon):
        self.name = name
        self.weapon = weapon

    def change_weapon(self, new_weapon):
        self.weapon = new_weapon
        print(f"{self.name} меняет оружие на {type(new_weapon).__name__}.")

class Monster:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def is_alive(self):
        return self.health > 0

def fight(fighter, monster):
    while monster.is_alive():
        fighter.weapon.attack(monster)
        if not monster.is_alive():
            print(f"Монстр {monster.name} побежден!")
            break

fighter = Fighter("Герой", Sword())
monster = Monster("Злобный Гоблин", 20)

fight(fighter, monster)

fighter.change_weapon(Bow())
monster = Monster("Злобный Гоблин", 20)

fight(fighter, monster)