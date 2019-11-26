import random as r
from pynput.keyboard import Key, Listener
class Gamer:
    def __init__(self, name, comp=False):
        self.health = 100
        self.name = name
        self.comp = comp
    @property
    def _is_35(self):
        return self.comp and self.health <= 50
    def _1(self):  #def moderate_damage(self):
        """causes moderate damage"""
        damage = r.randint(18,25)
        return -damage
    def _2(self):    #def big_damage(self):
        """causes big damage"""
        damage = r.randint(10, 35)
        return -damage
    def _3(self):    #def healing(self):
        """is healed"""
        res = r.randint(18,25)
        self.health += res
        return res
    def action(self):
        rand = r.randint(1,3)
        if self._is_35 and rand != 3 and not r.randint(0,3):
            rand = 3
            #print(self.name)
        met_name = "_{}".format(rand)
        action = getattr(self,met_name)
        #res = action_35(action) if self._is_35 else action()
        res = action()
        string_res = "player named {} makes a move: {}".format(self.name,action.__doc__)
        string_res += " {}".format(res)
        print(string_res)
        return res if res < 0 else 0
class Game:
    def __init__(self,you,other):
        self.gamers = {1:you, 0:other}
        self._exit = True
    def on_press(self,key):
        return False
    def on_release(self,key):
        if key == Key.esc:
            self._exit = True
            return False
    def begin(self):
        while True:
            self.gamers.get(1).health = self.gamers.get(0).health = 100
            self._exit = False
            while True:#self.gamers.get(1).health > 0 and self.gamers.get(0).health > 0:
                index = r.randint(0, 1)
                action = self.gamers.get(index).action()
                self.gamers.get(not index).health += action

                print("{} you left {} lives!".format(self.gamers.get(1).name,
                                                     0 if self.gamers.get(1).health < 0 else self.gamers.get(1).health),
                      "{} left {} lives!".format(self.gamers.get(0).name,
                                                 0 if self.gamers.get(0).health < 0 else self.gamers.get(0).health),
                      sep="\n")

                if self.gamers.get(1).health <= 0 or self.gamers.get(0).health <= 0:
                    break

                print("do you want to continue? Ctrl/Esc")
                with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
                    listener.join()

                if self._exit:
                    break

            if not self._exit:
                if self.gamers.get(1).health > 0:
                    print("You won!")
                else:
                    print("you beat")

            if input("new game? y/n?  ") == 'n':
                break


game = Game(Gamer("misha"),Gamer("computer",True))
game.begin()

