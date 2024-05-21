from orders import Order
from drinkorders import DrinkOrder
from mainorders import MainOrder
from sideorders import SideOrder
from drinkinv import DrinkInv
from sideinv import SideInv
from maininv import MainInv

import pytest

class IdGenerator():
    def __init__(self):
        self._id = 0

    def next(self):
        self._id += 1
        return self._id
order_num_gen = IdGenerator()

@pytest.fixture(scope="module")
def order_fixture():
    order_1 = Order(1)
    
    return order_1 
