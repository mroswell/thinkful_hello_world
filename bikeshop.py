class Bicycle(object):
  def __init__(self, name, weight, production_cost):
    self.name = name
    self.weight = weight
    self.production_cost = production_cost

class Bikeshop(object):
  def __init__(self, name, inventory):
    self.name = name
    self.inventory = inventory
    
  def sell_bike(self,bicycle, margin):
    bicycle.customer_cost = bicycle.production_cost * (1 + margin)
    self.inventory.remove(bicycle)
    
  def determine_profit():
    pass

class Customer(object):
  def __init__(self, name, budget):
    self.name = name
    self.budget = budget
    
  def buy_and_own_bike(self,bike, bikecollection=[]):
    self.bikecollection = bikecollection.append(bike)
    self.budget = self.budget - bike.production_cost * 1.2
    
def main():
  schwinn = Bicycle('Schwinn', 12, 160)
  bikee = Bicycle('BikeE',24,1000)
  explorer = Bicycle('Explorer',20,750)
  scooter = Bicycle('Scooter',5, 300)
  folder = Bicycle('Folder',13, 1600)
  friday = Bicycle('Bike Friday', 19,1400)
  print schwinn.name
  print "Weighs", schwinn.weight, "lbs"
  print "Costs $", schwinn.production_cost, "to produce"
  penny_shop = Bikeshop("Penny's Bikes", [schwinn, bikee, explorer, scooter, folder, friday])
  joanne = Customer('Joanne', 200)
  anne = Customer('Anne', 500)
  jane = Customer('Jane', 1690)
  customers = [joanne, jane, anne]
  for customer in customers:
    print '---------------'
    print customer.name
    print '---------------'
    for bike in penny_shop.inventory:
      if customer.budget >= bike.production_cost * 1.2:
        print "-", bike.name
    print "-----------"
    print "Penny's Inventory"
    print "-----------"
    
    for bike in penny_shop.inventory:
      print "-", bike.name
      
    print "psi", penny_shop.inventory
    for bike in penny_shop.inventory:
      if customer.budget >= bike.production_cost * 1.2:
   #    customer.owned = penny_shop.inventory.pop()
        customer.owned = bike
        pass
    print "owned bike: ", customer.owned.name, customer.owned.production_cost
 #   customer.buy_and_own_bike(penny_shop.inventory.pop) 
    print "-----------"
    print "Penny's Inventory"
    print "-----------"
    for bike in penny_shop.inventory:
       print "-", bike.name
      
    penny_shop.sell_bike(customer.owned, 0.2)

  print "-----------"
  print "Penny's Inventory"
  print "-----------"
  for bike in penny_shop.inventory:
    print "-", bike.name  

    
if __name__ == '__main__':
  main()
