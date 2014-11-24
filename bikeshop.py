class Wheel(object):
  """Represents a bike wheel"""

  def __init__(self, name, weight, production_cost):
    self.name = name
    self.weight = weight
    self.production_cost = production_cost


class Frame(object):
  """Represents a bike frame"""
  def __init__(self, weight, production_cost, type):
    self.weight = weight
    self.production_cost = production_cost
    self.type = type

class Bicycle(object):
  def __init__(self, name, wheel_choice, frame):
    self.name = name
    self.weight = 0
#    for wheel in wheels:
#      self.weight += wheel.weight
#      print self.weight
    self.weight = wheel_choice.weight * 2 + frame.weight
    self.production_cost = wheel_choice.production_cost * 2 + frame.production_cost

class Bikeshop(object):
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory
    for bike in inventory:
      bike.customer_cost  = bike.production_cost * 1.2
      bike.profit = bike.customer_cost -  bike.production_cost

  def sell_bike(self,bicycle):
    self.inventory.remove(bicycle)

#  def determine_profit(self,bicycle):
#    print self.inventory[bicycle].customer_cost - biproduction_cost

class Customer(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    self.bikes = []

  def buy_and_own_bike(self,bike):
    self.budget = self.budget - bike.customer_cost
    self.bikes.append(bike)


