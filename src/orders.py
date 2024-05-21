from src.ordererror import OrderError, addMainOrderError, addSideOrderError, addDrinkOrderError

class Order():
    def __init__(self, order_id, order_status = 'Pending'):
        self._order_id = order_id 
        self._order_status = order_status
        self._mainorder = [] 
        self._drinkorder = []
        self._sideorder = []
        self._totalprice = 0 
        self._base = False

    # methods
    
    def calc_fee(self): 
        TP = 0
        for m in self._mainorder:
            TP = TP + int(m.cal_price())
        for s in self._sideorder:
            TP = TP + int(s.cal_price())
        for d in self._drinkorder:
            TP = TP + int(d.cal_price())
        self._totalprice = TP
        print(TP)
        return self._totalprice

        
    def getOrderID(self):
        return self._order_id

    def getOrderStatus(self):
        return self._order_status

    def setOrderStatus(self,status):    # can be Completed, Confirmed, Pending, 
        self._order_status = status

    def set_New_Order_Completed_ID(self,new_id):    # can be Completed, Confirmed, Pending, 
        self._order_id = new_id
    
    def setBase(self,b):         #this is to see whether the customer has ordered a base burger or not
        self._base = b
    
    # add objects to the order 

    def addMainOrder(self,mainorder,inv_main, base=False):
        error = addMainOrderError(mainorder,inv_main, base)
        if error == []:
            self._mainorder.append(mainorder)
        else: 
            error.insert(0, "Error 'Adding Main': Mains not added")
            return error


    def addDrinkOrder(self,drinkorder,inv_drink):
        error = addDrinkOrderError(drinkorder,inv_drink)
        if error == []:
            self._drinkorder.append(drinkorder)
        else: 
            # append at start of list 
            error.insert(0, "Error 'Adding Drink': Drinks not added")
            return error

    def addSideOrder(self,sideorder,inv_side):
        error = addSideOrderError(sideorder,inv_side)
        if error == []:
            self._sideorder.append(sideorder)
        else: 
            error.insert(0, "Error 'Adding Side': Sides not added")
            return error
    


    # properties

    @property
    def order_id(self):
        return self._order_id

    @property
    def order_status(self):
        return self._order_status

    @property
    def mainorder(self):
        return self._mainorder

    @property
    def drinkorder(self):
        return self._drinkorder
    
    @property
    def sideorder(self):
        return self._sideorder

    @property
    def totalprice(self):
        return self._totalprice
        
    @property
    def base(self):
        return self._base    

    # output 

    def __str__(self):
        drinksStr = ''
        if len(self.drinkorder) != 0: 
            for d in self.drinkorder:
                drinksStr = drinksStr + str(d)

        mainStr = ''
        if len(self.mainorder) != 0: 
            for m in self.mainorder:
                mainStr = mainStr + str(m)

        sideStr = ''
        if len(self.sideorder) != 0: 
            for s in self.sideorder:
                sideStr = sideStr + str(s)
        

        return "Order ID: " + str(self.order_id) + ". \nOrder Status: " + self.order_status + " " + "\n" + drinksStr + "\n" + mainStr + "\n" + sideStr

