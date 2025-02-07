class Character:
    def __init__(self, health, weapon):
        self.health = health
        self.weapon = weapon

    def get_health(self):
        return self.health
    
    def get_weapon(self):
        return self.weapon