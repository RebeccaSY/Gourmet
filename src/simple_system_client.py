from orders import Order
from drinkorders import DrinkOrder
from mainorders import MainOrder
from sideorders import SideOrder
from inventory import MainInv,DrinkInv,SideInv
from system import System

Sys = System()

o = Order(1)
print(o)

d = DrinkOrder()
d.addDrink('Coca Cola 375',10)
print(d)
o.addDrinkOrder(d,Sys.drinkinv)

m = MainOrder()
m.addMain("Sesame Bun",3)
m.addMain("Chicken Patty",2)
print(m)
o.addMainOrder(m,Sys.maininv)


s = SideOrder()
s.addSide("Small Fries",15)
print(s)
o.addSideOrder(s,Sys.sideinv)

print("\nworking 1 ")

print(o)

Sys.add_order(o)
Sys.confirm_Order(1)
Sys.update_OrderStatus(o, "Confirmed")
print(o)

confirmed_orders = Sys.view_all_orders()
for o in confirmed_orders:
   print(o)

# find inventory quantity 
print("\nworking 2 ")
for Coca in Sys.drinkinv: 
        if Coca.name == "Coca Cola 375":
                print(Coca.name)
                print(Coca.quantity)

Sys.update_drinkinv("Coca Cola 375", 7)
print("\nworking 3")
for Coca in Sys.drinkinv: 
        if Coca.name == "Coca Cola 375":
                print(Coca.name)
                print(Coca.quantity)
