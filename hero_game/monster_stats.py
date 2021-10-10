class Monster:
    def __init__(self,monster_name):
        self.monster_name=monster_name
        self.monster_health=5
        self.monster_damege=1
        self.monster_level=1
        self.M=1.3


    def constructor(self):
        self.monster_health=self.monster_health*1.3*self.monster_level-1
        self.monster_damege=self.monster_damege*1.3*self.monster_level-1
        

    def Attack(self,hero):
        hero.Reduce_Health(self)

    def Reduce_Health(self,hero):
        self.monster_health-=hero.hero_damege
        if(self.monster_health<0):
            self.monster_health=0
        


