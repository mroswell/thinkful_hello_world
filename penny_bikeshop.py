from bikeshop import Bicycle, Bikeshop, Customer, Wheel, Frame
profit = 0

def print_inventory():
  print "-----------"
  print "Penny's Inventory"
  print "-----------"
  for bike in penny_shop.inventory:
    print "-", bike.name

little_wheel = Wheel('Little Wheel', 2, 20)
medium_wheel = Wheel('Medium Wheel', 3, 25)
large_wheel = Wheel('Large Wheel', 5, 30)

aluminum = Frame(8, 75, 'Aluminum')
carbon = Frame(7, 100, 'Carbon')
steel = Frame(11, 70, 'Steel')

# schwinn = Bicycle('Schwinn', 12, 160, [little_wheel, little_wheel], aluminum)
# bikee = Bicycle('BikeE',24,1000, [medium_wheel, medium_wheel], aluminum)
# explorer = Bicycle('Explorer',20,750, [large_wheel,large_wheel], carbon)
# scooter = Bicycle('Scooter',5, 300, [medium_wheel, medium_wheel], steel)
# folder = Bicycle('Folder',13, 1600, [little_wheel, little_wheel], aluminum)
# friday = Bicycle('Bike Friday', 19,1400, [little_wheel, little_wheel], carbon)

schwinn = Bicycle('Schwinn', 160, [little_wheel, little_wheel], aluminum)
bikee = Bicycle('BikeE',1000, [medium_wheel, medium_wheel], aluminum)
explorer = Bicycle('Explorer',750, [large_wheel,large_wheel], carbon)
scooter = Bicycle('Scooter', 300, [medium_wheel, medium_wheel], steel)
folder = Bicycle('Folder', 1600, [little_wheel, little_wheel], aluminum)
friday = Bicycle('Bike Friday',1400, [little_wheel, little_wheel], carbon)

print schwinn.name
print "Weighs", schwinn.weight, "lbs"
print "Costs $", schwinn.production_cost, "to produce"

penny_shop = Bikeshop("Penny's Bikes", [schwinn, bikee, explorer, scooter, folder, friday])
joanne = Customer('Joanne', 200)
anne = Customer('Anne', 500)
jane = Customer('Jane', 1690)
customers = [joanne, jane, anne]

print_inventory()

for customer in customers:
  print '---------------'
  print customer.name
  print '---------------'
  # for bike in penny_shop.inventory:
  #   if customer.budget >= bike.production_cost * 1.2:
  #     print "-", bike.name
  print "Bikes within {}'s budget:".format(customer.name)
  for bike in penny_shop.inventory:
    if customer.budget >= bike.customer_cost:
        print "-", bike.name
        customer.owned = bike
#        profit += penny_shop.determine_profit(customer.owned)
  profit += customer.owned.profit
#  print customer.owned.profit
  penny_shop.sell_bike(customer.owned)

  print "{} purchased a {}.\n It cost: ${:.2f}\n Remaining budget: ${:.2f}".format(customer.name, customer.owned.name,customer.owned.customer_cost,customer.budget - customer.owned.customer_cost)

print_inventory()
print("{} earned ${:.2f} in profit".format(penny_shop.name,profit))
