from orders import Order
from drinkorders import DrinkOrder
from mainorders import MainOrder
from sideorders import SideOrder
from inventory import MainInv,DrinkInv,SideInv
from system import System



#TESTS are towards the bottom! :)



#Setting up orders

##

##


Sys = System()

#order 1
o1 = Order(1)
d = DrinkOrder()
d.addDrink('Coca Cola 375',9)
o1.addDrinkOrder(d,Sys.drinkinv)

m = MainOrder()
m.addMain("Chicken Patty", 2)
m.addMain("Sesame Bun",3)
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
#Triple burger with 4 buns
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
o3.addSideOrder(s1,Sys.sideinv)


#order 4
#invalid inputs
o4 = Order(4)

m1 = MainOrder()
#m1.addMain("Sesame Bun", 5)
m1.addMain("Veg Patty", 2)
m1.addMain("Chicken Patty", 2)
o4.addMainOrder(m1,Sys.maininv)
print(m1.checkMainAval(Sys.maininv))

Sys.add_order(o1)
Sys.confirm_Order(1)
Sys.add_order(o2)
Sys.confirm_Order(2)
Sys.add_order(o3)
Sys.confirm_Order(3)
Sys.add_order(o4)

order = Sys.view_order(4)
main = order.mainorder

#for m in main:  
#print(main.checkMainAval(Sys.maininv))


#view confirmed orders

#confirmed_orders = Sys.view_all_orders()
#for o in confirmed_orders:
#   print(o)
   
#view all orders
for o in Sys.orders:
   print(o)
 
#for main in Sys.sideinv:  
#   if main.name == "Small Fries":
#      print("main inventory: " + str(main.weight))           

#view all orders
for o in Sys.orders:
   print(o)
 
for s in Sys.sideinv:  
   if s.name == "Fries":
      print("side inventory: " + str(s.weight)) 
 
# TESTS!   

#check order status for each order
def test_order_status():
   assert(o1.order_status == "Confirmed")
   assert(o2.order_status == "Confirmed")
   assert(o3.order_status == "Confirmed")

#check that order was put into system correctly
def test_view_order():   
   order = Sys.view_order(1)
   assert(o1 == order)
   order = Sys.view_order(2)
   assert(o2 == order)   
   order = Sys.view_order(3)
   assert(o3 == order)  

# test total price
def test_price():    
    #order1
    ordr = Sys.view_order(1)
    assert(ordr.calc_fee() == 9*5 + 3*5 + 2*5 + 15*5)
    # test order 1 drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 9*5)
    # test order 1 main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 3*5 + 2*5)
    # test order 1 side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 15*5)
    
    #order2
    ordr = Sys.view_order(2)
    assert(ordr.calc_fee() == 4*5 + 65*5 + 11*5)
    # test order 1 drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 4*5)
    # test order 1 main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 65*5)
    # test order 1 side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 11*5)

#Checking correct error messages were returned or invalid amounts
def test_invalid_mains():
   m1 = MainOrder()
   m1.addMain("Sesame Bun", 5)
   assert(m1.checkMainAval(Sys.maininv) == "" + "Invalid Quantity of Buns, please select fewer \n")

#check items in drink inventory were decremented properly
def test_drink_inv():
   for drink in Sys.drinkinv: 
        if drink.name == "Coca Cola 375":
                assert(drink.quantity == 91) 
                
   for drink in Sys.drinkinv: 
        if drink.name == "Orange Juice 250":
                assert(drink.quantity == 97)  
                
   for drink in Sys.drinkinv: 
        if drink.name == "Coca Cola 600":
                assert(drink.quantity == 96) 
                
   for drink in Sys.drinkinv: 
        if drink.name == "Orange Juice 450":
                assert(drink.quantity == 93)   
 
#check items in main inventory were decremented properly                
def test_main_inv():
   for main in Sys.maininv:  
        if main.name == "Sesame Bun":
                assert(main.quantity == 93)                 
        if main.name == "Muffin Buns":
                assert(main.quantity == 97)  
        if main.name == "Chicken Patty":
                assert(main.quantity == 94)
        if main.name == "Veg Patty":
                assert(main.quantity == 99)
        if main.name == "Beef Patty":
                assert(main.quantity == 100)             
 
#check items in side inventory were decremented properly
def test_side_inv():
   for side in Sys.sideinv: 
        if side.name == "Small Fries":
                assert(side.weight == 85)                                
        if side.name == "Medium Fries":
                assert(side.weight == 100)  
        if side.name == "Large Fries":
                assert(side.weight == 94)                                
        if side.name == "6 pack nuggets":
            assert(side.weight == 96)                                      
        if side.name == "3 pack nuggets":
            assert(side.weight == 89)         
