from bikeshop import Bicycle, Bikeshop, Customer
profit = 0

def print_inventory():
  print "-----------"
  print "Penny's Inventory"
  print "-----------"
  for bike in penny_shop.inventory:
    print "-", bike.name

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
