from orders import Order
from drinkorders import DrinkOrder
from mainorders import MainOrder
from sideorders import SideOrder
from inventory import MainInv,DrinkInv,SideInv
from system import System

import pytest

@pytest.fixture(scope="module")
def system_fixture():
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
    Sys.confirm_Order(1)
    Sys.add_order(o2)
    Sys.confirm_Order(2)
    Sys.add_order(o3)
    Sys.confirm_Order(3)

    Sys.complete_Order(3)

    return Sys


# TESTS!   
def test_order_status(system_fixture):
    o1 = system_fixture.view_order(1)
    o2 = system_fixture.view_order(2)
    o3 = system_fixture.view_order(3)
    assert(o1.order_status == "Confirmed")
    assert(o2.order_status == "Confirmed")
    assert(o3.order_status == "Complete")


def test_view_order(system_fixture):   
    order = system_fixture.view_order(1)
    assert(order.order_id == 1)
    order = system_fixture.view_order(2)
    assert(order.order_id == 2)
    order = system_fixture.view_order(3)
    assert(order.order_id == 3)

# test inventory system decrementing    
def test_drink_inv(system_fixture):
    for drink in system_fixture.drinkinv: 
        if drink.name == "Coca Cola 375":
                assert(drink.quantity == 91) 
                
    for drink in system_fixture.drinkinv: 
        if drink.name == "Orange Juice 250":
                assert(drink.quantity == 97)  
                
    for drink in system_fixture.drinkinv: 
        if drink.name == "Coca Cola 600":
                assert(drink.quantity == 96) 
                
    for drink in system_fixture.drinkinv: 
        if drink.name == "Orange Juice 450":
                assert(drink.quantity == 93)   
 
# test inventory system decrementing 
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
 
# test inventory system decrementing 
def test_side_inv(system_fixture):
    for side in system_fixture.sideinv: 
        if side.name == "Small Fries":
                assert(side.weight == 85)                                
        if side.name == "Medium Fries":
                assert(side.weight == 100)  
        if side.name == "Large Fries":
                assert(side.weight == 94)                                        
        if side.name == "3 pack nuggets":
                assert(side.weight == 89)                            
        if side.name == "6 pack nuggets":
                assert(side.weight == 96)           

# test total price 
def test_price(system_fixture):
    ordr = system_fixture.view_order(1)
    # test total price

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
    #order 2

    ordr = system_fixture.view_order(2)
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

# TESTS!   
def test_confirm_order(system_fixture):
    #Triple Burger with four buns
    o3 = Order(3)
    d1 = DrinkOrder()
    d1.addDrink('Orange Juice 450', 7)
    d1.addDrink('Coca Cola 600', 3)   
    o3.addDrinkOrder(d1,system_fixture.drinkinv)

    m1 = MainOrder()
    m1.addMain("Sesame Bun", 4)
    m1.addMain("Veg Patty", 1)
    m1.addMain("Chicken Patty", 2)
    m1.addMain("Tomato Sauce", 15)
    m1.addMain("Cheddar Cheese", 5)
    o3.addMainOrder(m1,system_fixture.maininv)

    s1 = SideOrder()
    s1.addSide("Large Fries", 6)
    s1.addSide("6 pack nuggets", 4)
    o3.addSideOrder(s1,system_fixture.sideinv)
    system_fixture.add_order(o3)
    assert(system_fixture.confirm_Order(3) == 3)


# insufficient quantity testing 
def test_insufficient_quantity_order(system_fixture):
    o1 = Order(1)
    m1 = MainOrder()
    m1.addMain("Sesame Bun", 4)
    m1.addMain("Veg Patty", 3)
    m1.addMain("Lettuce", 2000)
    m1.addMain("Tomato", 40)
    o1.addMainOrder(m1,system_fixture.maininv)
    assert(len(o1.mainorder) == 0)

    d1 = DrinkOrder()
    d1.addDrink('Orange Juice 450', 7000)
    d1.addDrink('Coca Cola 600', 3)   
    o1.addDrinkOrder(d1,system_fixture.drinkinv)
    assert(len(o1.drinkorder) == 0)

    s1 = SideOrder()
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
    m4 = MainOrder()
    m4.addMain("Sesame Bun", 5)
    m4.addMain("Veg Patty", 1)
    m4.addMain("Chicken Patty", 2)
    assert(m4.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Buns, please select fewer \n")
    
    #Triple burger - error choosing 4 buns but not correct number of patties
    m5 = MainOrder()
    m5.addMain("Sesame Bun", 4)
    m5.addMain("Veg Patty", 2)
    assert(m5.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a triple burger please select 4 buns \n")

    #Double burger - error choosing 3 buns but not correct number of patties    
    m6 = MainOrder()
    m6.addMain("Sesame Bun", 3)
    m6.addMain("Veg Patty", 2)
    m6.addMain("Veg Patty", 1)
    assert(m6.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a double burger please select 3 buns \n")  
    
    #Single burger - error choosing 2 buns but not correct number of patties    
    m7 = MainOrder()
    m7.addMain("Sesame Bun", 2)
    m7.addMain("Chicken Patty", 2)
    assert(m7.checkMainAval(system_fixture.maininv) == "Invalid Quantity of Patties, for a single burger please select 2 buns \n")  
    
    #error for too many patties and no buns
    m8 = MainOrder()
    m8.addMain("Chicken Patty", 2)
    m8.addMain("Veg Patty", 2)
    assert(m8.checkMainAval(system_fixture.maininv) ==  "Invalid Quantity of patties, please select fewer \n")
