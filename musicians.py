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
    
  def s_combust(self):
    print "kaboom"
  
        
def main():
  nigel = Guitarist()
  nigel.solo(7)
  print nigel.sounds
  ringo = Drummer()
  ringo.solo(8)
  print ringo.sounds 
  ringo.s_combust()
  
if __name__ == '__main__':
  main()