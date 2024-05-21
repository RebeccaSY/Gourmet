class Ingredients:

   def __init__(self, name, price, quantity):
      self._name = name
      self._price = price
      self._quantity = quantity
   
   @property
   def name(self):
      return self._name
     
   @property
   def price(self):
      return self._price

   @property
   def quantity(self):
      return self._quantity
      
   @quantity.setter
   def quantity(self, new_quantity):
      self._quantity = new_quantity
      


sesame_bun = Ingredients("Sesame bun", 0, 100)
muffin_buns = Ingredients("Muffin Buns", 0, 100)
chicken_patty = Ingredients("Chicken Patty", 0, 100)
veg_patty = Ingredients("Veg Patty", 0, 100)
beef_patty = Ingredients("Beef Patty", 0, 100)
tomato = Ingredients("Tomato", 0, 100)
lettuce = Ingredients("Lettuce", 0, 100)
tomato_sauce = Ingredients("Tomato sauce", 0, 100)
cheddar_cheese = Ingredients("Cheddar cheese", 0, 100)
swiss_cheese = Ingredients("Swiss cheese", 0, 100)
 
coca_cola_375 = Ingredients("Coca Cola 375", 0, 100)
coca_cola_600 = Ingredients("Coca Cola 600", 0, 100)
orange_juice_250 = Ingredients("Orange Juice 250", 0, 100)
orange_juice_450 = Ingredients("Orange Juice 450", 0, 100)
