from abc import ABC, abstractmethod
from random import randint, choice


class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health

    @abstractmethod
    def attack(self, another_item):
        pass

    @abstractmethod
    def buff(self):
        """Метод для підсилення зброї на наступний хід"""
        pass


class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self._sharp = 0

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"🗡 Завдаємо удару мечем {self.name} ({current_attack} шкоди). У {another_item.name} залишилось: {another_item.health} HP"

    def buff(self):
        self._sharp += 5
        print(f"✨ Меч {self.name} загострено! Додаткова шкода збільшена.")


class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 20)
        another_item.health -= current_attack
        return f"🪓 Завдаємо удару сокирою {self.name} ({current_attack} шкоди). У {another_item.name} залишилось: {another_item.health} HP"

    def buff(self):
        self.__attack_power += 3
        print(f"🔥 Сокира {self.name} розлючена! Базова атака зросла.")


class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int = 0):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power

    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"🏹 Стріляємо з лука {self.name} ({current_attack} шкоди). У {another_item.name} залишилось: {another_item.health} HP"

    def buff(self):
        self.range_power += 5
        print(f"🎯 Лучник з {self.name} прицілюється! Дальність та шкода зросли.")



print("=== ВІТАЄМО НА АРЕНІ ===")


weapons_pool = [
    Sword("Ескалібур", 40),
    Axe("Кратос", 45),
    Bow("Леголас", 35)
]

player_weapon = choice(weapons_pool)

weapons_pool.remove(player_weapon)
enemy_weapon = choice(weapons_pool)

print(f"Ваша зброя: {player_weapon.name} ({type(player_weapon).__name__})")
print(f"Зброя супротивника: {enemy_weapon.name} ({type(enemy_weapon).__name__})\n")

round_num = 1
while player_weapon.health > 0 and enemy_weapon.health > 0:
    print(f"\n--- Хід {round_num} ---")
    print(f"Ваше HP: {player_weapon.health} | HP Ворога: {enemy_weapon.health}")

    action = input("Оберіть дію (1 - Атака, 2 - Підсилення): ")
    if action == '1':
        print(player_weapon.attack(enemy_weapon))
    elif action == '2':
        player_weapon.buff()
    else:
        print("Невірний вибір, ви втрачаєте хід!")

    if enemy_weapon.health <= 0:
        print("\n🏆 ВИ ПЕРЕМОГЛИ!")
        break

    print("\nХід супротивника...")
    enemy_action = choice(['1', '1', '2'])  # Більший шанс на атаку
    if enemy_action == '1':
        print(enemy_weapon.attack(player_weapon))
    else:
        enemy_weapon.buff()

    if player_weapon.health <= 0:
        print("\n💀 ВИ ПРОГРАЛИ!")
        break

    round_num += 1