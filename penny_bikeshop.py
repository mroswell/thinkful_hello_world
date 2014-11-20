from bikeshop import Bicycle, Bikeshop, Customer

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
    if customer.budget >= bike.customer_cost:
      customer.owned = bike
      pass
  print "owned bike: ", customer.owned.name, customer.owned.production_cost
  print "-----------"
  print "Penny's Inventory"
  print "-----------"
  for bike in penny_shop.inventory:
     print "-", bike.name

  penny_shop.sell_bike(customer.owned)

print "-----------"
print "Penny's Inventory"
print "-----------"
for bike in penny_shop.inventory:
  print "-", bike.name

