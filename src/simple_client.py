from orders import Order
from drinkorders import DrinkOrder
from mainorders import MainOrder
from sideorders import SideOrder
from inventory import MainInv,DrinkInv,SideInv
from system import System

Sys = System()

#order 1
o1 = Order(1)
d = DrinkOrder()
d.addDrink('Coca Cola 375',9)
o1.addDrinkOrder(d,Sys.drinkinv)

m = MainOrder()
m.addMain("Sesame Bun",3)
m.addMain("Chicken Patty",2)
o1.addMainOrder(m,Sys.maininv)

s = SideOrder()
s.addSide("Small Fries",15)
o1.addSideOrder(s,Sys.sideinv)

#order 2
#Double burger with three buns
o2 = Order(2)
d1 = DrinkOrder()
d1.addDrink('Orange Juice 250', 3)
d1.addDrink('Coca Cola 600', 1)   
o2.addDrinkOrder(d1,Sys.drinkinv)

m1 = MainOrder()
m1.addMain("Muffin Buns", 3)
m1.addMain("Chicken Patty", 2)
m1.addMain("Lettuce", 20)
m1.addMain("Tomato", 40)
o2.addMainOrder(m1,Sys.maininv)

s = SideOrder()
s.addSide("3 pack nuggets", 11)
o2.addSideOrder(s,Sys.sideinv)

#order 3
#Triple Burger with four buns
o3 = Order(3)
d1 = DrinkOrder()
d1.addDrink('Orange Juice 450', 7)
d1.addDrink('Coca Cola 600', 3)   
o3.addDrinkOrder(d1,Sys.drinkinv)

m1 = MainOrder()
m1.addMain("Sesame Bun", 4)
m1.addMain("Veg Patty", 1)
m1.addMain("Chicken Patty", 2)
m1.addMain("Tomato Sauce", 15)
m1.addMain("Cheddar Cheese", 5)
o3.addMainOrder(m1,Sys.maininv)

s1 = SideOrder()
s1.addSide("Large Fries", 6)
s1.addSide("6 pack nuggets", 4)
print("*****************")
print(str(s1.cal_fry_weight()))
print(str(s1.cal_nugget_weight()))
print("*****************")
o3.addSideOrder(s1,Sys.sideinv)

#order 4
#invalid inputs
o4 = Order(4)
m4 = MainOrder()
m4.addMain("Sesame Bun", 5)
m4.addMain("Veg Patty", 1)
m4.addMain("Chicken Patty", 2)
o4.addMainOrder(m4,Sys.maininv)
Sys.add_order(o4)

Sys.add_order(o1)
print(Sys.view_order(1))
Sys.confirm_Order(1)
Sys.add_order(o2)
Sys.confirm_Order(2)
Sys.add_order(o3)
Sys.confirm_Order(3)

print("print(o4)")
print(o4)
print("print(Sys.view_order(1))")
print(Sys.view_order(4))


print("order 1" + o1.order_status)
print("order 2" + o2.order_status)
print("order 3" + o3.order_status)

Sys.complete_Order(3)

print("order 3" + o3.order_status)

print(o1.calc_fee())


