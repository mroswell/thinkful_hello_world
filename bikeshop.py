class Bicycle(object):
  def __init__(self, name, weight, production_cost):
    self.name = name
    self.weight = weight
    self.production_cost = production_cost

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


