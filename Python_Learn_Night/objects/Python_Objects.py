from Python_Playable_Warrior import Warrior
from Python_Playable_Mage import Mage
from Python_Enemy_Goblin import Goblin
from Python_Enemy_Dragon import Dragon

def main():
    warrior = Warrior("Bob")
    mage = Mage("Sally")
    goblin = Goblin("Carol")
    dragon = Dragon("Lorenzo")
    
    print("{} has {}hp, {} attack, {} defense".format(warrior.name,warrior.hp,warrior.attack,warrior.defense))
    print("{} has {}hp, {} attack, {} defense".format(mage.name,mage.hp,mage.attack,mage.defense))
    print("{} has {}hp, {} attack, {} defense".format(goblin.name,goblin.hp,goblin.attack,goblin.defense))
    print("{} has {}hp, {} attack, {} defense".format(dragon.name,dragon.hp,dragon.attack,dragon.defense))

main()