
class Musician(object):
    def __init__(self, sounds):
        self.sounds = sounds

    def solo(self, length):
        for i in range(length):
            print self.sounds[i % len(self.sounds)],
        print ""

class Bassist(Musician): # The Musician class is the parent of the Bassist class
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Bassist, self).__init__(["Twang", "Thrumb", "Bling"])

class Guitarist(Musician):
    def __init__(self):
        # Call the __init__ method of the parent class
        super(Guitarist, self).__init__(["Boink", "Bow", "Boom"])

    def tune(self):
        print "Be with you in a moment"
        print "Twoning, sproing, splang"
        
class Drummer(Musician):
  def __init__(self):
    super(Drummer, self).__init__(["a-one", "a-two", "a-three", "and four"])
    
  def count_time(self):
    print "a-one, a-two, a-three, and four"
    
  def s_combust(self):
    print "kaboom"
  
class Band(): 
  def __init__(self, name, members):
    self.name = name
    self.members = members
    
  def hire(self, musician):
    self.members.append(musician)
  
  def fire(self, musician):
    self.members.remove(musician)
  
def main():
  margie = Guitarist()
#  margie.solo(16)
  nigel = Guitarist()
#  nigel.solo(7)
 # print nigel.sounds
  ringo = Drummer()
  kazoo_player = Musician(["zzshm", "zzzjh", "neeer", "zhz"])
#  ringo.solo(8)
  #print ringo.sounds 
#  ringo.s_combust()
  TheRedOranges = Band("The Red Oranges", [nigel, ringo])
  TheRedOranges.hire(margie)
  ringo.count_time()
  for musician in TheRedOranges.members:
    if type(musician).__name__ != "Drummer":
      musician.solo(8)
  TheRedOranges.fire(nigel)
  TheRedOranges.hire(kazoo_player)
  ringo.count_time()
  
  for musician in TheRedOranges.members:
    if type(musician).__name__ != "Drummer":
      musician.solo(8)
if __name__ == '__main__':
  main()