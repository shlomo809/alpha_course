class Hero:
    def __init__(self, hero_name):
        self.hero_name = hero_name
        self.hero_level = 1
        self.hero_damege = 2
        self.hero_health = 10
        self.hero_coins = 0
        self.if_defend = False
        self.M = 1.3

    def Heal(self):
        self.hero_health += self.hero_health*self.M

        if(self.hero_health >= 10+(self.M)**self.hero_level-1):
            self.hero_health = 10+(self.M)**self.hero_level-1

    def level_up(self):
        self.hero_coins -= self.hero_level*2
        self.hero_level += 1
        self.hero_health = 10+(self.M)**self.hero_level-1
        self.hero_damege *= self.M

    def Attack(self, monster):
        monster.Reduce_Health(self)

    def Defend(self):
        return True

    def Reduce_Health(self, monster):
        if(self.if_defend):
            self.hero_health -= monster.monster_damege*0.8
        else:
            self.hero_health -= monster.monster_damege

        if(self.hero_health < 0):
            return 0

        return self.hero_health

    def Choose_Action(self, monster):
        action = input(
            "What do you want to do in this turn:\n 1: Attck\2 2:Defend\n 3:Heal yourself\n 4:level up\n")

        if(action == '1'):
            self.Attack(monster)
        elif(action == '2'):
            self.if_defend = self.Defend()
        elif(action == '3'):
            self.Heal()
        elif(action == '4'):
            if(self.hero_coins >= self.hero_level*2):
                self.level_up()
            else:
                print("you dont have enough coins to level up")
                self.Choose_Action(monster)
        else:
            print("you inpute is not good")
            self.Choose_Action(monster)
