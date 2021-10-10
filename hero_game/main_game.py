from hero_stats import Hero
from monster_stats import Monster
import random


def main():
    monster_level = 1
    hero_name = input("please enter your hero name:\n")
    print(f"Hello there {hero_name} and welcome to Caverns of the Frozen Morass this  is a scary dangerous place  Be careful and may the god be with you\n")
    monster_name = random.choice(["Brineclaw", "Hauntmorph", "Smokebody", "Blightfang", "The Infamous Ooze",
                                 "The Grim Demon", "The Black Tumor", "The Golden Rot Lizard", "The Dark Doom Freak", "Voodoochild", ])
    hero = Hero(hero_name)
    monster = Monster(monster_name, monster_level)
    while(hero.hero_health > 0):
        hero.Choose_Action(monster)
        monster.Attack(hero)
        print("your hero health is:", hero.hero_health)
        if(monster.monster_health == 0):
            monster_level = random.randint(
                hero.hero_level-1, hero.hero_level+1)
            if(monster_level == 0):
                monster_level = 1
            print("the monster level is:", monster_level)
            monster = Monster(monster_name, monster_level)
            monster_name = random.choice(["Brineclaw", "Hauntmorph", "Smokebody", "Blightfang", "The Infamous Ooze",
                                         "The Grim Demon", "The Black Tumor", "The Golden Rot Lizard", "The Dark Doom Freak", "Voodoochild", ])
            hero.hero_coins += 1
        hero.hero_coins += 1
    print("you lost the game, you got to level:", monster.monster_level)


if __name__ == "__main__":
    main()
