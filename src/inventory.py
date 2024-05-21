from abc import ABC, abstractmethod


class Inventory(ABC):

   def __init__(self, name, price):
      self._name = name
      self._price = price
   
   @property
   def name(self):
      return self._name
     
   @property
   def price(self):
      return self._price

   def __str__(self):
      return 'Inv Item: ' + self.name
      
class MainInv(Inventory):
   def __init__(self, name, price, quantity):
      super().__init__(name,price)
      self._quantity = quantity

   def __str__(self):
      return ' ' + super().__str__() + '. quantity: ' + str(self.quantity)
      
   @property
   def quantity(self):
      return self._quantity
      
   @quantity.setter
   def quantity(self, new_quantity):
      self._quantity = new_quantity
      
class SideInv(Inventory):
   def __init__(self, name, price, weight):
      super().__init__(name,price)
      self._weight = weight

   def __str__(self):
      return ' ' + super().__str__() + '. weight: ' + str(self.weight)

   @property
   def weight(self):
      return self._weight
      
   @weight.setter
   def weight(self, new_weight):
      self._weight = new_weight

class DrinkInv(Inventory):
   def __init__(self, name, price, quantity):
      super().__init__(name,price)
      self._quantity = quantity

   def __str__(self):
      return ' ' + super().__str__() + '. quantity: ' + str(self.quantity)

   @property
   def quantity(self):
      return self._quantity
      
   @quantity.setter
   def quantity(self, new_quantity):
      self._quantity = new_quantity

