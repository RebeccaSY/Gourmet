from src.orders import Order
from src.drinkorders import DrinkOrder
from src.mainorders import MainOrder
from src.sideorders import SideOrder
from src.inventory import MainInv,DrinkInv,SideInv
from src.system import System
from src.cart_mgr import Cart, CartManager

import pytest

#----------------------------------------------------------------------------------------------
# test02
#       tests that customer is able to checkout and confirm the orders

@pytest.fixture(scope="module")
def system_fixture():
    Sys = System()

    #Create Orders
    
    # order A
    # order a standard base burger with sides and drinks 
    o1 = Order(1)
    d = DrinkOrder(1)
    d.addDrink('Orange Juice 450', 1)
    d.addDrink('Coca Cola 600', 1)
    o1.addDrinkOrder(d, Sys.drinkinv)

    m = MainOrder(1)
    m.addMain("Sesame Bun", 2)
    m.addMain("Chicken Patty", 1)
    m.addMain("Lettuce", 1)
    m.addMain("Tomato", 1)
    o1.addMainOrder(m, Sys.maininv)

    s = SideOrder(1)
    s.addSide("Small Strawberry Sundae", 1)
    s.addSide("Small Chocolate Sundae", 1)    
    o1.addSideOrder(s, Sys.sideinv)

    # order B
    # order a fast meal with new item 
    o2 = Order(2)
    m2 = MainOrder(2)
    m2.addMain("Sesame Bun", 2)
    m2.addMain("Veg Patty", 1)
    m2.addMain("Lettuce", 1)
    m2.addMain("Tomato", 1)
    o2.addMainOrder(m2, Sys.maininv)
    
    d = DrinkOrder(2)
    d.addDrink('Coca Cola 375',1)
    o2.addDrinkOrder(d, Sys.drinkinv)

    s2 = SideOrder(2) 
    s2.addSide("Small Strawberry Sundae", 1)
    o2.addSideOrder(s2, Sys.sideinv)

    # order C
    # order a base burger with new items
    o3 = Order(3)
    m = MainOrder(3)
    m.addMain("Sesame Bun", 2)
    m.addMain("Chicken Patty", 1)
    m.addMain("Lettuce", 1)
    m.addMain("Tomato", 1)
    o3.addMainOrder(m, Sys.maininv)
    
    d = DrinkOrder(3)
    d.addDrink('Coca Cola 375',1)
    d.addDrink('Orange Juice 250', 2)
    o3.addDrinkOrder(d, Sys.drinkinv)
    
    s3 = SideOrder(3)
    s3.addSide("Medium Strawberry Sundae", 2)  
    s3.addSide("Small Strawberry Sundae", 1)
    s3.addSide("Large Fries", 2)  
    o3.addSideOrder(s3, Sys.sideinv)


    # order D
    # order a fast meal with sides and drinks         
    o4 = Order(4)
    m4 = MainOrder(2)
    m4.addMain("Sesame Bun", 2)
    m4.addMain("Chicken Patty", 1)
    m4.addMain("Lettuce", 1)
    m4.addMain("Tomato", 1)
    o4.addMainOrder(m4, Sys.maininv)
    
    d4 = DrinkOrder(4)
    d4.addDrink('Orange Juice 450', 2)
    o4.addDrinkOrder(d4, Sys.drinkinv)

    s4 = SideOrder(4) 
    s4.addSide("Small Strawberry Sundae", 2)
    s4.addSide("Small Chocolate Sundae", 2)
    o4.addSideOrder(s4, Sys.sideinv)


    # order E
    # order a fast meal with new items
    o5 = Order(5)
    m5 = MainOrder(5)
    m5.addMain("Sesame Bun", 2)
    m5.addMain("Chicken Patty", 1)
    m5.addMain("Lettuce", 1)
    m5.addMain("Tomato", 1)
    o5.addMainOrder(m5, Sys.maininv)
    
    d5 = DrinkOrder(5)
    d5.addDrink('Coca Cola 600',1)
    d5.addDrink('Orange Juice 450', 1)
    o5.addDrinkOrder(d5, Sys.drinkinv)

    s5 = SideOrder(5) 
    s5.addSide("Small Strawberry Sundae", 2)
    o5.addSideOrder(s5, Sys.sideinv)


    Sys.add_order(o1)
    Sys.confirm_Order(1)
    Sys.complete_Order(1)
    Sys.add_order(o2)
    Sys.confirm_Order(2)
    Sys.complete_Order(2)
    Sys.add_order(o3)
    Sys.confirm_Order(3)
    Sys.complete_Order(3)
    Sys.add_order(o4)
    Sys.confirm_Order(4)
    Sys.add_order(o5)
    Sys.confirm_Order(5)

    return Sys


#----------------------------------------------------------------------------------------------
# TESTS! 

# testing that correct price is calculated and displayed to customer
def test_price(system_fixture):


    # order A
    ordr = system_fixture.view_order(1)
    # test order A total price
    assert(ordr.calc_fee() == 45)
    # test order A drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 10)
    # test order A main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 25)
    # test order A side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 10)


    # order B
    ordr = system_fixture.view_order(2)
    # test order B total price
    assert(ordr.calc_fee() == 25 + 5 + 5)
    # test order B drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 5)
    # test order B main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 25)
    # test order B side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 5)


    # order C
    ordr = system_fixture.view_order(3)
    # test order C total price
    assert(ordr.calc_fee() == 25 + 5*3 + 5*3 + 2*5)
    # test order C drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 15)
    # test order C main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 25)
    # test order C side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 25)


    # order D
    ordr = system_fixture.view_order(4)
    # test order D total price
    assert(ordr.calc_fee() == 55)
    # test order D drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 10)
    # test order D main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 25)
    # test order D side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 20)


    # order E
    ordr = system_fixture.view_order(5)
    # test order E total price
    assert(ordr.calc_fee() == 45)
    # test order E drink price 
    dprice = 0
    for do in ordr.drinkorder:
        dprice = dprice + do.cal_price()
    assert(dprice == 10)
    # test order E main price
    mprice = 0
    for mo in ordr.mainorder:
        mprice = mprice + mo.cal_price()
    assert(mprice == 25)
    # test order E side price
    sprice = 0
    for so in ordr.sideorder:
        sprice = sprice + so.cal_price()
    assert(sprice == 10)


# testing that the order status is correctly displayed
def test_order_status(system_fixture):
        o1 = system_fixture.view_order(1)
        o2 = system_fixture.view_order(2)
        o3 = system_fixture.view_order(3)
        o4 = system_fixture.view_order(4)
        o5 = system_fixture.view_order(5)
        assert(o1.order_status == "Complete")
        assert(o2.order_status == "Complete")
        assert(o3.order_status == "Complete")
        assert(o4.order_status == "Confirmed")
        assert(o5.order_status == "Confirmed")


# testing that the correct order can be viewed based on order id
def test_view_order(system_fixture):   
        order1 = system_fixture.view_order(1)
        assert(order1.order_id == 1)
        order2 = system_fixture.view_order(2)
        assert(order2.order_id == 2)
        order3 = system_fixture.view_order(3)
        assert(order3.order_id == 3)
        order4 = system_fixture.view_order(4)
        assert(order4.order_id == 4)
        order5 = system_fixture.view_order(5)
        assert(order5.order_id == 5)


# test that staff can increase inventory quantitiies correctly             
def test_refill_inv(system_fixture):
        system_fixture.update_maininv("Sesame Bun", 100)
        system_fixture.update_maininv("Muffin Buns", 50)
        system_fixture.update_maininv("Chicken Patty", 50)
        system_fixture.update_maininv("Veg Patty", 50)
        system_fixture.update_maininv("Beef Patty", 50)
        
        system_fixture.update_drinkinv("Coca Cola 375", 100)
        system_fixture.update_drinkinv("Coca Cola 600", 100)
        system_fixture.update_drinkinv("Orange Juice 250", 60)
        system_fixture.update_drinkinv("Orange Juice 450", 30)
        
        system_fixture.update_sideinv("Nuggets", 1000)
        system_fixture.update_sideinv("Strawberry Sundae", 10000)
        system_fixture.update_sideinv("Chocolate Sundae", 10000)


        # test main inventory after refilled
        for main in system_fixture.maininv:  
                if main.name == "Sesame Bun":
                        assert(main.quantity == 190)                 
                if main.name == "Muffin Buns":
                        assert(main.quantity == 150)  
                if main.name == "Chicken Patty":
                        assert(main.quantity == 146)
                if main.name == "Veg Patty":
                        assert(main.quantity == 149)
                if main.name == "Beef Patty":
                        assert(main.quantity == 150)
                if main.name == "Lettuce":
                        assert(main.quantity == 95)
                if main.name == "Tomato":
                        assert(main.quantity == 95)
                if main.name == "Tomato sauce":
                        assert(main.quantity == 100)
                if main.name == "Cheddar cheese":
                        assert(main.quantity == 100)
                if main.name == "Swiss cheese":
                        assert(main.quantity == 100)

        # test drink inventory after refilled
        for drink in system_fixture.drinkinv: 
                if drink.name == "Coca Cola 375":
                        assert(drink.quantity == 198)                 
                if drink.name == "Orange Juice 250":
                        assert(drink.quantity == 158)                 
                if drink.name == "Coca Cola 600":
                        assert(drink.quantity == 198)                     
                if drink.name == "Orange Juice 450":
                        assert(drink.quantity == 126)   
 
        # test side inventory system after refilled
        for side in system_fixture.sideinv: 
                if side.name == "Fries":
                        assert(side.weight == 49650)                                            
                if side.name == "Nuggets":
                        assert(side.weight == 51000)
                if side.name == "Strawberry Sundae":
                        assert(side.weight == 59225)
                if side.name == "Chocolate Sundae":
                        assert(side.weight == 59775)                            
                 
