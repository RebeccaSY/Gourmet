from src.orders import Order
from src.drinkorders import DrinkOrder
from src.mainorders import MainOrder
from src.sideorders import SideOrder
from src.inventory import MainInv,DrinkInv,SideInv
from src.system import System
from src.cart_mgr import Cart, CartManager

import pytest

#----------------------------------------------------------------------------------------------
# test01
#       tests that customer is able to add orders

@pytest.fixture(scope="module")
def system_fixture():
    Sys = System()

    #Creating Orders
    
    #order 1
    o0 = Order(0)

    m = MainOrder(0)
    m.addMain("Muffin Bun",3)
    m.addMain("Beef Patty",2)
    o0.addMainOrder(m,Sys.maininv)

    d = DrinkOrder(0)
    d.addDrink('Coca Cola 375',4)
    o0.addDrinkOrder(d,Sys.drinkinv)

    s = SideOrder(0)
    s.addSide("Medium Chocolate Sundae", 2)    
    o0.addSideOrder(s,Sys.sideinv)
    
    #order 1
    o1 = Order(1)
    d = DrinkOrder(1)
    d.addDrink('Coca Cola 375',9)
    o1.addDrinkOrder(d,Sys.drinkinv)

    m = MainOrder(1)
    m.addMain("Sesame Bun",3)
    m.addMain("Chicken Patty",2)
    o1.addMainOrder(m,Sys.maininv)

    s = SideOrder(1)
    s.addSide("Small Fries",15)
    s.addSide("Medium Strawberry Sundae", 3)
    s.addSide("Small Chocolate Sundae", 7)    
    o1.addSideOrder(s,Sys.sideinv)

    #order 2
    #Double burger with three buns
    o2 = Order(2)
    d1 = DrinkOrder(2)
    d1.addDrink('Orange Juice 250', 3)
    d1.addDrink('Coca Cola 600', 1)   
    o2.addDrinkOrder(d1,Sys.drinkinv)

    m1 = MainOrder(2)
    m1.addMain("Muffin Buns", 3)
    m1.addMain("Chicken Patty", 2)
    m1.addMain("Lettuce", 20)
    m1.addMain("Tomato", 40)
    o2.addMainOrder(m1,Sys.maininv)

    s = SideOrder(2)
    s.addSide("3 pack nuggets", 11)
    s.addSide("Large Chocolate Sundae", 10)
    o2.addSideOrder(s,Sys.sideinv)

    #order 3
    #Triple Burger with four buns
    o3 = Order(3)
    d1 = DrinkOrder(3)
    d1.addDrink('Orange Juice 450', 7)
    d1.addDrink('Coca Cola 600', 3)   
    o3.addDrinkOrder(d1,Sys.drinkinv)

    m1 = MainOrder(3)
    m1.addMain("Sesame Bun", 4)
    m1.addMain("Veg Patty", 1)
    m1.addMain("Chicken Patty", 2)
    m1.addMain("Tomato Sauce", 15)
    m1.addMain("Cheddar Cheese", 5)
    o3.addMainOrder(m1,Sys.maininv)

    s1 = SideOrder(3)
    s1.addSide("Large Fries", 6)
    s1.addSide("6 pack nuggets", 4)
    o3.addSideOrder(s1,Sys.sideinv)

    #order 4
    #invalid inputs
    o4 = Order(4)
    m4 = MainOrder(4)
    m4.addMain("Sesame Bun", 5)
    m4.addMain("Veg Patty", 1)
    m4.addMain("Chicken Patty", 2)
    o4.addMainOrder(m4,Sys.maininv)

    Sys.add_order(o0)
    Sys.add_order(o1)
    Sys.confirm_Order(1)
    Sys.add_order(o2)
    Sys.confirm_Order(2)
    Sys.add_order(o3)
    Sys.confirm_Order(3)
    Sys.add_order(o4)

    Sys.complete_Order(3)

    return Sys


#----------------------------------------------------------------------------------------------
# TESTS!   
#testing the order status and that the correct orders were confirmed/completed
def test_order_status(system_fixture):
    o0 = system_fixture.view_order(0)
    o1 = system_fixture.view_order(1)
    o2 = system_fixture.view_order(2)
    o3 = system_fixture.view_order(3)
    assert(o0.order_status == "Pending")
    assert(o1.order_status == "Confirmed")
    assert(o2.order_status == "Confirmed")
    assert(o3.order_status == "Complete")

#testing that the correct order can be viewed according to order id
def test_view_order(system_fixture):   
    order = system_fixture.view_order(1)
    assert(order.order_id == 1)
    order = system_fixture.view_order(2)
    assert(order.order_id == 2)
    order = system_fixture.view_order(3)
    assert(order.order_id == 3)
           
# test drink inventory system decrementing after confirmed order
def test_drink_inv(system_fixture):
    for drink in system_fixture.drinkinv: 
        if drink.name == "Coca Cola 375":
                assert(drink.quantity == 91)                 
        if drink.name == "Orange Juice 250":
                assert(drink.quantity == 97)                 
        if drink.name == "Coca Cola 600":
                assert(drink.quantity == 96)                     
        if drink.name == "Orange Juice 450":
                assert(drink.quantity == 93)   
 
# test main inventory system decrementing after confirmed order
def test_main_inv(system_fixture):
    for main in system_fixture.maininv:  
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
 
# test side inventory system decrementing after confirmed order
def test_side_inv(system_fixture):
    for side in system_fixture.sideinv: 
        if side.name == "Fries":
                assert(side.weight == 47825)                                            
        if side.name == "Nuggets":
                assert(side.weight == 48575)
        if side.name == "Strawberry Sundae":
                assert(side.weight == 49625)
        if side.name == "Chocolate Sundae":
                assert(side.weight == 47725)                            
                 

# test for confirming order correctly with no error messages returned   
def test_confirm_order(system_fixture):
    #Triple Burger with four buns
    o3 = Order(5)
    d1 = DrinkOrder(5)
    d1.addDrink('Orange Juice 450', 7)
    d1.addDrink('Coca Cola 600', 3)   
    o3.addDrinkOrder(d1,system_fixture.drinkinv)

    m1 = MainOrder(5)
    m1.addMain("Sesame Bun", 4)
    m1.addMain("Veg Patty", 1)
    m1.addMain("Chicken Patty", 2)
    m1.addMain("Tomato Sauce", 15)
    m1.addMain("Cheddar Cheese", 5)
    o3.addMainOrder(m1,system_fixture.maininv)

    s1 = SideOrder(5)
    s1.addSide("Large Fries", 6)
    s1.addSide("6 pack nuggets", 4)
    o3.addSideOrder(s1,system_fixture.sideinv)
    system_fixture.add_order(o3)
    assert(system_fixture.confirm_Order(3) == '')


# insufficient quantity testing 
def test_insufficient_quantity_order(system_fixture):
    o1 = Order(6)
    m1 = MainOrder(6)
    m1.addMain("Sesame Bun", 4)
    m1.addMain("Veg Patty", 3)
    m1.addMain("Lettuce", 2000)
    m1.addMain("Tomato", 40)
    o1.addMainOrder(m1,system_fixture.maininv)
    assert(len(o1.mainorder) == 0)

    d1 = DrinkOrder(6)
    d1.addDrink('Orange Juice 450', 7000)
    d1.addDrink('Coca Cola 600', 3)   
    o1.addDrinkOrder(d1,system_fixture.drinkinv)
    assert(len(o1.drinkorder) == 0)

    s1 = SideOrder(6)
    s1.addSide("Large Fries", 6)
    s1.addSide("6 pack nuggets", 400)
    o1.addSideOrder(s1,system_fixture.sideinv)
    assert(len(o1.sideorder) == 0)

    # add success 
    s1.addSide("Large Fries", 6)
    s1.addSide("6 pack nuggets", 4)
    o1.addSideOrder(s1,system_fixture.sideinv)
    assert(len(o1.sideorder) == 1)
    pass


#Checking correct error messages were returned or invalid amounts
def test_invalid_mains(system_fixture):
    #error choosing more than 4 buns
    o7 = Order(7)
    m4 = MainOrder(7)
    m4.addMain("Sesame Bun", 5)
    m4.addMain("Veg Patty", 1)
    m4.addMain("Chicken Patty", 2)
    assert(m4.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Buns, please select fewer \n""Invalid Quantity of buns, for a triple burger please select 4 buns \n")
    
    #Triple burger - error choosing 4 buns but not correct number of patties
    o8 = Order(8)
    m5 = MainOrder(8)
    m5.addMain("Sesame Bun", 4)
    m5.addMain("Veg Patty", 2)
    assert(m5.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a triple burger please select 4 buns \n""Invalid Quantity of buns, for a double burger please select 3 buns \n")

    #Double burger - error choosing 3 buns but not correct number of patties    
    o9 = Order(9)
    m6 = MainOrder(9)
    m6.addMain("Sesame Bun", 3)
    m6.addMain("Veg Patty", 2)
    m6.addMain("Beef Patty", 1)
    assert(m6.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a double burger please select 3 buns \n""Invalid Quantity of buns, for a triple burger please select 4 buns \n")  
    
    #Single burger - error choosing 2 buns but not correct number of patties    
    o10 = Order(10)
    m7 = MainOrder(10)
    m7.addMain("Sesame Bun", 2)
    m7.addMain("Chicken Patty", 2)
    assert(m7.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a single burger please select 2 buns \n""Invalid Quantity of buns, for a double burger please select 3 buns \n")  
    
    #error for too many patties and no buns
    o11 = Order(11)
    m8 = MainOrder(11)
    m8.addMain("Chicken Patty", 2)
    m8.addMain("Veg Patty", 2)
    assert(m8.checkMainAval(system_fixture.maininv) ==  "Invalid Quantity of Patties, please select fewer \n") 
    


# test correct total price is calculated and displayed to customer
def test_price(system_fixture):
    ordr = system_fixture.view_order(1)
    # test total price

    assert(ordr.calc_fee() == 9*5 + 3*5 + 2*5 + 15*5 + 3*5 + 7*5)
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
    assert(sprice == 25*5)
    #order 2

    ordr = system_fixture.view_order(2)
    assert(ordr.calc_fee() == 4*5 + 65*5 + 11*5 + 10*5)
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
    assert(sprice == 21*5)
    
