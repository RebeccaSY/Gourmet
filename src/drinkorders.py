# these classes only put together what the customer wants 
class DrinkOrder():
    def __init__(self,client_ID ):

        self._id = client_ID

        self._drinks = {"Coca Cola 375":0,
                        "Coca Cola 600":0,
                        "Orange Juice 250":0,
                        "Orange Juice 450":0}

        self._drink_price = {"Coca Cola 375": 5,
                        "Coca Cola 600": 5,
                        "Orange Juice 250": 5,
                        "Orange Juice 450": 5}

    # drinks inventory object should be a dictionary or list of objects? 
    def checkDrinkAval(self,drink_inventory_list):
        # To traverse a list of drink objects 
        error = ""
        for d in drink_inventory_list:
            if self.drinks[d.name] > d.quantity:
                error = error + "Insufficient quantity " + d.name + ". There are only " + str(d.quantity) + " avaliable. You requested " + str(self.drinks[d.name]) + "\n"
                break

        # # To traverse an object with inventory as dictionary data 
        # error = 0
        # for d,number in drink_inventory_list.inv_drinks.items(): 
        #     if self.drinks[d] > number:
        #         error = 1
        #         break
        return error 

    def cal_price(self):
        price = 0
        for d,number in self.drink_price.items():
            price = price + self.drinks[d]*number
        return price


    def addDrink(self, drinkname, quantity):
        self.drinks[drinkname] = quantity

    @property
    def id(self):
        return self._id

    @property
    def drinks(self):
        return self._drinks

    @property
    def drink_price(self):
        return self._drink_price

    def __str__(self):
        drinksINorder = ''
        for d,number in self.drinks.items():
            if number != 0:
                drinksINorder = drinksINorder + d + ": " + str(number) + " "
        return '\n Drink Order: ' + drinksINorder





