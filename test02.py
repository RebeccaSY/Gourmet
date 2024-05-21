from src.orders import Order
from src.drinkorders import DrinkOrder
from src.mainorders import MainOrder
from src.sideorders import SideOrder
from src.inventory import MainInv,DrinkInv,SideInv
from src.system import System
from src.cart_mgr import Cart, CartManager

import pytest

#----------------------------------------------------------------------------------------------
# test04
#       tests that staff member is able to update the inventory


@pytest.fixture(scope="module")
def system_fixture():
    Sys = System()
    return Sys


# test main inventory 
def test_main_inv(system_fixture):
    for main in system_fixture.maininv:  
        if main.name == "Sesame Bun":
                assert(main.quantity == 100)                 
        if main.name == "Muffin Buns":
                assert(main.quantity == 100)  
        if main.name == "Chicken Patty":
                assert(main.quantity == 100)
        if main.name == "Veg Patty":
                assert(main.quantity == 100)
        if main.name == "Beef Patty":
                assert(main.quantity == 100)             
 
# test drink inventory 
def test_drink_inv(system_fixture):
    for drink in system_fixture.drinkinv: 
        if drink.name == "Coca Cola 375":
                assert(drink.quantity == 100)                 
        if drink.name == "Orange Juice 250":
                assert(drink.quantity == 100)                 
        if drink.name == "Coca Cola 600":
                assert(drink.quantity == 100)                     
        if drink.name == "Orange Juice 450":
                assert(drink.quantity == 100)   
 
# test side inventory 
def test_side_inv(system_fixture):
    for side in system_fixture.sideinv: 
        if side.name == "Fries":
                assert(side.weight == 50000)                                            
        if side.name == "Nuggets":
                assert(side.weight == 50000)
        if side.name == "Strawberry Sundae":
                assert(side.weight == 50000)
        if side.name == "Chocolate Sundae":
                assert(side.weight == 50000) 



#test that staff can increase inventory quantitiies correctly     
def test_refill_inv(system_fixture):
        system_fixture.update_maininv("Sesame Bun", 100)
        system_fixture.update_maininv("Muffin Buns", 200)
        system_fixture.update_maininv("Chicken Patty", 50)
        system_fixture.update_maininv("Veg Patty", 50)
        system_fixture.update_maininv("Beef Patty", 50)
        system_fixture.update_maininv("Lettuce", 100)
        system_fixture.update_maininv("Tomato", 100)
        system_fixture.update_maininv("Tomato sauce", 100)
        system_fixture.update_maininv("Cheddar cheese", 100)
        system_fixture.update_maininv("Swiss cheese", 100)
        
        system_fixture.update_drinkinv("Coca Cola 375", 120)
        system_fixture.update_drinkinv("Coca Cola 600", 60)
        system_fixture.update_drinkinv("Orange Juice 250", 120)
        system_fixture.update_drinkinv("Orange Juice 450", 60)
        
        system_fixture.update_sideinv("Nuggets", 6000)
        system_fixture.update_sideinv("Fries", 6000)
        system_fixture.update_sideinv("Strawberry Sundae", 10000)
        system_fixture.update_sideinv("Chocolate Sundae", 10000)


        # test main inventory after refilled
        for main in system_fixture.maininv:  
                if main.name == "Sesame Bun":
                        assert(main.quantity == 200)                 
                if main.name == "Muffin Buns":
                        assert(main.quantity == 300)  
                if main.name == "Chicken Patty":
                        assert(main.quantity == 150)
                if main.name == "Veg Patty":
                        assert(main.quantity == 150)
                if main.name == "Beef Patty":
                        assert(main.quantity == 150)
                if main.name == "Lettuce":
                        assert(main.quantity == 200)
                if main.name == "Tomato":
                        assert(main.quantity == 200)
                if main.name == "Tomato sauce":
                        assert(main.quantity == 200)
                if main.name == "Cheddar cheese":
                        assert(main.quantity == 200)
                if main.name == "Swiss cheese":
                        assert(main.quantity == 200)

        # test drink inventory after refilled
        for drink in system_fixture.drinkinv: 
                if drink.name == "Coca Cola 375":
                        assert(drink.quantity == 220)                 
                if drink.name == "Orange Juice 250":
                        assert(drink.quantity == 220)                 
                if drink.name == "Coca Cola 600":
                        assert(drink.quantity == 160)                     
                if drink.name == "Orange Juice 450":
                        assert(drink.quantity == 160)   
 
        # test side inventory system after refilled
        for side in system_fixture.sideinv: 
                if side.name == "Fries":
                        assert(side.weight == 56000)                                            
                if side.name == "Nuggets":
                        assert(side.weight == 56000)
                if side.name == "Strawberry Sundae":
                        assert(side.weight == 60000)
                if side.name == "Chocolate Sundae":
                        assert(side.weight == 60000)  



# test inventory updates after order confirmed
def test_inventory_update(system_fixture):

        #create an order
        o = Order(10)

        main = MainOrder(10)
        main.addMain("Muffin Buns", 3)
        main.addMain("Beef Patty", 2)
        main.addMain("Swiss cheese", 2)
        main.addMain("Tomato sauce", 2)
        o.addMainOrder(main, system_fixture.maininv)

        drink = DrinkOrder(10)
        drink.addDrink('Orange Juice 450', 1)
        drink.addDrink('Coca Cola 375', 1)   
        o.addDrinkOrder(drink, system_fixture.drinkinv)

        side = SideOrder(10)
        side.addSide("6 pack nuggets", 1)
        side.addSide("Medium Fries", 1)
        side.addSide("Large Chocolate Sundae", 1)
        o.addSideOrder(side, system_fixture.sideinv)

        system_fixture.add_order(o)
        system_fixture.confirm_Order(10)
        system_fixture.complete_Order(10)

        # test main inventory after order
        for main in system_fixture.maininv:  
                if main.name == "Sesame Bun":
                        assert(main.quantity == 200)                 
                if main.name == "Muffin Buns":
                        assert(main.quantity == 297)  
                if main.name == "Chicken Patty":
                        assert(main.quantity == 150)
                if main.name == "Veg Patty":
                        assert(main.quantity == 150)
                if main.name == "Beef Patty":
                        assert(main.quantity == 148)
                if main.name == "Lettuce":
                        assert(main.quantity == 200)
                if main.name == "Tomato":
                        assert(main.quantity == 200)
                if main.name == "Tomato sauce":
                        assert(main.quantity == 198)
                if main.name == "Cheddar cheese":
                        assert(main.quantity == 200)
                if main.name == "Swiss cheese":
                        assert(main.quantity == 198)

        # test drink inventory after order
        for drink in system_fixture.drinkinv: 
                if drink.name == "Coca Cola 375":
                        assert(drink.quantity == 219)                 
                if drink.name == "Orange Juice 250":
                        assert(drink.quantity == 220)                 
                if drink.name == "Coca Cola 600":
                        assert(drink.quantity == 160)                     
                if drink.name == "Orange Juice 450":
                        assert(drink.quantity == 159)   
 
        # test side inventory system after order
        for side in system_fixture.sideinv: 
                if side.name == "Fries":
                        assert(side.weight == 55875)                                            
                if side.name == "Nuggets":
                        assert(side.weight == 55850)
                if side.name == "Strawberry Sundae":
                        assert(side.weight == 60000)
                if side.name == "Chocolate Sundae":
                        assert(side.weight == 59825)  

