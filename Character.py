class Character:
    def __init__(self, health, weapon):
        self.health = health
        self.weapon = weapon
        self.inventory = []

    def get_health(self):
        return self.health
    
    def get_weapon(self):
        return self.weapon
    
    def get_inventory(self):
        return self.inventory
    
    def lose_health(self, damage):
        self.health -= damage

    def gain_health(self, heal):
        self.health += heal

    def grab_weapon(self, weapon):
        self.weapon = weapon
    
    def lose_weapon(self):
        self.weapon = None

    def player_damage(self, weapon):
        pass

    def add_inventory(self, item):
        self.inventory.append(item)
        print(f"\n{item} added to inventory!\n")
    
    def use_inventory(self, item):
        self.inventory.remove(item)
        print(f"{item} removed from inventory!\n")
