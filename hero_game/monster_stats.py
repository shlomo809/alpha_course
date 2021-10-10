class Monster:
    def __init__(self, monster_name, monster_level):
        self.monster_name = monster_name
        self.monster_level = monster_level
        self.monster_health = 5+1.3*(self.monster_level-1)
        self.monster_damege = 1+1.3*(self.monster_level-1)
        print(self.monster_damege)

        self.M = 1.3

    def Attack(self, hero):
        hero.Reduce_Health(self)

    def Reduce_Health(self, hero):
        self.monster_health -= hero.hero_damege
        if(self.monster_health < 0):
            self.monster_health = 0
