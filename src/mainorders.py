# these classes only put together what the customer wants 
class MainOrder():
    def __init__(self, client_ID ):
        
        self._id = client_ID

        self._mains = {"Sesame Bun":0,
                        "Muffin Buns":0,
                        "Chicken Patty":0,
                        "Veg Patty":0,
                        "Beef Patty":0,
                        "Tomato":0,
                        "Lettuce":0,
                        "Tomato sauce":0,
                        "Cheddar cheese":0, 
                        "Swiss cheese":0}
                    
        self._main_price = {"Sesame Bun":5,
                        "Muffin Buns":5,
                        "Chicken Patty":5,
                        "Veg Patty":5,
                        "Beef Patty":5,
                        "Tomato":5,
                        "Lettuce":5,
                        "Tomato sauce":5,
                        "Cheddar cheese":5, 
                        "Swiss cheese":5}

    def addMain(self, foodname, quantity):
        self.mains[foodname] = quantity

    def checkMainAval(self,main_inventory_list, base=False):
        # To traverse a list of main objects 
        error = ""
        for m in main_inventory_list:
            if self.mains[m.name] > m.quantity:
                error = error + "Insufficient quantity " + m.name + ". There are only " + str(m.quantity) + " avaliable. You requested " +  str(self.mains[m.name]) + "\n"
        # # traverse a dictionary
        # error = 0
        # for m,number in main_inventory_list.inv_mains.items(): 
        #     if self.mains[m] > number:
        #         error = 1
        #         break


        #if the customer is ordering a ready-made burger (ie a base) then no need to check bun and patty quantity
        if base==True:
            return error

        # error handling for mny buns or patties 
        if self.mains["Sesame Bun"] + self.mains["Muffin Buns"] > 4:
            error = error + "Invalid Quantity of Buns, please select fewer \n"
        if (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] == 4) and (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] != 3):
            error = error + "Invalid Quantity of Patties, for a triple burger please select 4 buns \n"
        if (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] == 3) and (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] != 2):
            error = error + "Invalid Quantity of Patties, for a double burger please select 3 buns \n"
        if (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] == 2) and (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] != 1):
            error = error + "Invalid Quantity of Patties, for a single burger please select 2 buns \n"
        #if self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"]  > 3:
           # error = error + "Invalid Quantity of patties, please select fewer \n"
           
        # patty test cases 
        if (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] > 3):
             error = error + "Invalid Quantity of Patties, please select fewer \n"
        if (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] == 3) and (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] != 4):
            error = error + "Invalid Quantity of buns, for a triple burger please select 4 buns \n"
        if (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] == 2) and (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] != 3):
            error = error + "Invalid Quantity of buns, for a double burger please select 3 buns \n"
        if (self.mains["Chicken Patty"] + self.mains["Veg Patty"] + self.mains["Beef Patty"] == 1) and (self.mains["Sesame Bun"] + self.mains["Muffin Buns"] != 2):
            error = error + "Invalid Quantity of buns, for a single burger please select 2 buns \n"
        return error 

    def cal_price(self):
        price = 0
        for m,number in self.main_price.items():
            price = price + self.mains[m]*number
        return price

    @property
    def id(self):
        return self._id

    @property
    def mains(self):
        return self._mains

    @property 
    def main_price(self):
        return self._main_price

    def __str__(self):
        mainINorder = ''
        for main,number in self.mains.items():
            if number != 0:
                mainINorder = mainINorder + main + ": " + str(number) + " "
        return '\n Main Order: ' + mainINorder
