# Every shopping cart has a unique ID, and a list of items from the customer. 


class CartManager:

    __id = -1
    # every customer has a shopping cart 
    @classmethod
    def generate_id(cls):
        CartManager.__id += 1
        return CartManager.__id

class Cart:
    def __init__(self):
        # every customer has a unique cart ID 
        self._id = CartManager.generate_id()
        # and a list of items in the cart 
        self._items = []

    def __str__(self): 
        return "cart number is " + str(self._id)
        
    @property
    def id(self):
        return self._id
