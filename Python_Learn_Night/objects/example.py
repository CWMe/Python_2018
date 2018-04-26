from Python_Playable_Warrior import Warrior
from Python_Playable_Mage import Mage
from Python_Enemy_Goblin import Goblin
from Python_Enemy_Dragon import Dragon
import random


class Game():
    warrior = Warrior()
    mage = Mage()

    goblin1 = Goblin("Goblin 1")
    goblin2 = Goblin("Goblin 2")
    dragon = Dragon()
    characters = [warrior,mage]
    enemies = [goblin1, goblin2, dragon]
    gameEnd = False
    turn = 0
    def __init__(self):
        
        while(self.gameEnd == False):
            self.turn+=1
            self.outputStats()
            self.outputCommands()
            command = input("start game: ")
            if command == "1":
                print ("attacking with warrior")
                self.warriorAttack()
            elif command == "2":
                print ("attacking with mage")
                self.mageAttack()
            elif command == "3":
                print ("skipped")
            elif command == "4":
                print ("game end")
                self.gameEnd = True
            if(self.gameEnd == False):
                if(self.turn%2==0):
                    self.enemyAction()
                self.checkHeroes()

    def checkHeroes(self):
        if(len(self.characters)==0):
            self.gameEnd = True
            print ("\n===== Results ======")
            self.outputStats()
            print ("You Lose!")
        if(len(self.enemies)==0):
            self.gameEnd = True
            print ("\n===== Results ======")
            self.outputStats()
            print ("You win!")

    def warriorAttack(self):
        if(self.warrior.hp <= 0):
            print ("warrior is dead")
            return
        if(len(self.enemies)==0):
            print ("all enemies are dead!")
            return
        index = random.randint(0,len(self.enemies)-1)
        enemy = self.enemies[index]
        enemy.hp = enemy.hp - (self.warrior.attack - enemy.defense)
        if(enemy.hp<=0):
            enemy.hp = 0
            print (enemy.name + " killed by " + self.warrior.name)
            self.enemies.pop(index)
        else:
            print (enemy.name + " hit!")

    def mageAttack(self):
        if(self.mage.hp <= 0):
            print ("mage is dead")
            return
        if(len(self.enemies)==0):
            print ("all enemies are dead!")
            return
        removeIndex = []
        for enemy in self.enemies:
            enemy.hp -= self.mage.attack
            if(enemy.hp<=0):
                enemy.hp=0
                print (enemy.name + " killed by " + self.mage.name)
                removeIndex.append(enemy)
            else:
                print (enemy.name + " hit!")
        for enemy in removeIndex:
            self.enemies.remove(enemy)

    def enemyAction(self):
        for enemy in self.enemies:
            if(len(self.characters)==0):
                break
            index = random.randint(0,len(self.characters)-1)
            hero = self.characters[index]
            hero.hp -= (enemy.attack - hero.defense)
            if(hero.hp<=0):
                hero.hp = 0
                print (hero.name + " killed by " + enemy.name)
                self.characters.remove(hero)
            else:
                print (hero.name + " hit by " + enemy.name)
    def outputCommands(self):
        print ("1 - Attack with warrior (1 random enemy, high dmg)")
        print ("2 - Attack with mage (all enemies, low pierce dmg)")
        print ("4 - Quit")
    def outputStats(self):
        if(self.gameEnd==False):
            print ("\nFight console - Turn " + str(self.turn))
        print (self.warrior.name + ": " + self.warrior.getHP())
        print (self.mage.name + ": " + self.mage.getHP() + "\n")
        print (self.goblin1.name + ": " + self.goblin1.getHP())
        print (self.goblin2.name + ": " + self.goblin2.getHP())
        print (self.dragon.name + ": " + self.dragon.getHP() + "\n")

Game()