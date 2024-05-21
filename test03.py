from src.orders import Order
from src.drinkorders import DrinkOrder
from src.mainorders import MainOrder
from src.sideorders import SideOrder
from src.inventory import MainInv,DrinkInv,SideInv
from src.system import System
from src.cart_mgr import Cart, CartManager

import pytest

#----------------------------------------------------------------------------------------------
# test03
#       tests that the status can be correctly displayed to customer and staff

@pytest.fixture(scope="module")
def system_fixture():
    Sys = System()
    return Sys


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


