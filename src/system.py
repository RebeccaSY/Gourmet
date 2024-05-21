from src.inventory import MainInv,DrinkInv,SideInv
from src.orders import Order
import pickle


class System():
    def __init__(self):
        self._orders = []
        self._sideinv = []
        self._maininv = []
        self._drinkinv = []


        # Initialise the types of food items we will have in the database:
        # Quantities will be replaced by the pickle file! 

        # sides by weight 
        fries = SideInv("Fries" , 0, 50000)
        nuggets = SideInv("Nuggets", 0, 50000)
        SSundae = SideInv("Strawberry Sundae", 0, 50000)
        CSundae = SideInv("Chocolate Sundae", 0,50000)

        self.sideinv.append(fries)
        self.sideinv.append(nuggets)
        self.sideinv.append(SSundae)
        self.sideinv.append(CSundae)

            
        sesame_bun = MainInv("Sesame Bun", 0, 100)
        muffin_buns = MainInv("Muffin Buns", 0, 100)
        chicken_patty = MainInv("Chicken Patty", 0, 100)
        veg_patty = MainInv("Veg Patty", 0, 100)
        beef_patty = MainInv("Beef Patty", 0, 100)
        tomato = MainInv("Tomato", 0, 100)
        lettuce = MainInv("Lettuce", 0, 100)
        tomato_sauce = MainInv("Tomato sauce", 0, 100)
        cheddar_cheese = MainInv("Cheddar cheese", 0, 100)
        swiss_cheese = MainInv("Swiss cheese", 0, 100)

        self.maininv.append(sesame_bun)
        self.maininv.append(muffin_buns)
        self.maininv.append(chicken_patty)
        self.maininv.append(veg_patty)
        self.maininv.append(beef_patty)
        self.maininv.append(tomato)
        self.maininv.append(lettuce)
        self.maininv.append(tomato_sauce)
        self.maininv.append(cheddar_cheese)
        self.maininv.append(swiss_cheese)
        
        coca_cola_375 = DrinkInv("Coca Cola 375", 0, 100)
        coca_cola_600 = DrinkInv("Coca Cola 600", 0, 100)
        orange_juice_250 = DrinkInv("Orange Juice 250", 0, 100)
        orange_juice_450 = DrinkInv("Orange Juice 450", 0, 100)

        self.drinkinv.append(coca_cola_375)
        self.drinkinv.append(coca_cola_600)
        self.drinkinv.append(orange_juice_250)
        self.drinkinv.append(orange_juice_450)
    
    # Methods
    
    # calculate the price of an order with orderID
    def calculate_price(self,ord_ID):
        for order in self.orders:
            if order.orderID == ord_ID:
                order.calc_fee()
                return order.totalprice
        
    def add_order(self, order_obj):
        self.orders.append(order_obj)

    def confirm_Order(self, ord_ID, base=False):
        success = ""
        for order in self.orders:
            if order.order_id == ord_ID:
                print("order check loop"+ str(order.order_id))
                # check ingredient quantity 
                ingredient_Quantity_Error = 0
                for m in order.mainorder:
                    if m.checkMainAval(self.maininv, base) != '':
                        # print(m.checkMainAval(self.maininv))
                        success = success + m.checkMainAval(self.maininv, base)

                        ingredient_Quantity_Error = 1
                for s in order.sideorder:
                    if s.checkSideAval(self.sideinv) != '':
                        # print(s.checkSideAval(self.sideinv))
                        success = success + s.checkSideAval(self.sideinv)

                        ingredient_Quantity_Error = 1
                for d in order.drinkorder:
                    if d.checkDrinkAval(self.drinkinv) != '':
                        # print(d.checkDrinkAval(self.drinkinv))
                        success = success + d.checkDrinkAval(self.drinkinv) 
                        ingredient_Quantity_Error = 1

                print("ingredient_Quantity_Error" + str(ingredient_Quantity_Error))

                if ingredient_Quantity_Error == 0:
                    self.update_OrderStatus(order,"Confirmed")
                    # decrement inventory 
                    for m in self.maininv:
                        for om in order.mainorder:
                            m.quantity = m.quantity - om.mains[m.name]

                    # decrement the weight 
                    for s in self.sideinv:
                        for os in order.sideorder:
                            if s.name == "Fries":
                                s.weight = s.weight - os.cal_fry_weight()
                            if s.name == "Nuggets":
                                s.weight = s.weight - os.cal_nugget_weight()
                            if s.name == "Strawberry Sundae":
                                s.weight = s.weight - os.cal_Ssundae_weight()
                            if s.name == "Chocolate Sundae":
                                s.weight = s.weight - os.cal_Csundae_weight()
                            
                
                    for d in self.drinkinv:
                        for od in order.drinkorder:
                            d.quantity = d.quantity - od.drinks[d.name]
                else: 
                    print("Error confirming order")
                    success = success + "Error confirming order"
        return success


    def complete_Order(self, ord_ID):
        success = 0
        for order in self.orders:
            if order.order_id == ord_ID:
                # print("Completed: Temporary Completed orders are 'deleted'")
                # new_ord = Order(ord_ID)
                self.update_OrderStatus(order,"Complete")
                success = 1
                # # create a new cart 
                # cartnum = fetch_session_cart(1)
                # # order.set_New_Order_Completed_ID((ord_ID+1000)*-1)
                # # # order.order_status = "Complete"
                # # success = 1
                # # # create an add a new order object for the same old cookie 
                # # new_ord = Order(ord_ID)
                # # self.add_order(new_ord)

        return success
    
    # to view a specific order with orderID or to view all the orders  
    def view_order(self, orderID):
        for o in self.orders:
            if o.order_id == orderID:
                return o
        return "Order Not Found"

    #view all confirmed orders
    def view_all_orders(self):
        confirmed_orders = []
        for o in self.orders:
            if o.order_status == "Confirmed":
                confirmed_orders.append(o)
        return confirmed_orders          
    
    # to update an order status
    def update_OrderStatus(self, Order, new_Status):
        for o in self.orders:
            if o.order_id == Order.order_id:
                Order.setOrderStatus(new_Status)
    
    # to update the inventory. "amount" must be a positive or negative number depending on if you're increasing or decreasing quantity
    def update_maininv(self, name, amount):
        for i in self._maininv:
            if i.name == name:
                i.quantity += amount

    def update_sideinv(self, name, amount):
        for i in self._sideinv:
            if i.name == name:
                i.weight += amount

    def update_drinkinv(self, name, amount):
        for i in self._drinkinv:
            if i.name == name:
                i.quantity += amount
    #------------------------------

    def saveallorders(self):
        filename = 'allorders.dat'
        with open(filename,'wb') as file:
            pickle.dump(self.orders,file)

    def loadallorders(self):
            filename = 'allorders.dat'
            try: 
                with open(filename,'rb') as file:
                    data = pickle.load(file)
                    # # testing 
                    print("from load main inventory function: ")
                    for loadord in data: 
                        # add to database if its a confirmed order, otherwise discard 
                        if loadord.order_status == "Confirmed":
                            self.add_order(loadord)
                            print("order added" + str(loadord))

            except EOFError:
                print("load orders EOF ERROR")
                self.saveallorders()
            except FileNotFoundError: 
                print("load orders FileNotFoundError")
                self.saveallorders()


    # to load inventory from pickle 
    def load_maininv(self, name, amount):
        for i in self._maininv:
            if i.name == name:
                i.quantity = amount

    def load_sideinv(self, name, amount):
        for i in self._sideinv:
            if i.name == name:
                i.weight = amount

    def load_drinkinv(self, name, amount):
        for i in self._drinkinv:
            if i.name == name:
                i.quantity = amount

    def savemaininventory(self):
        filename = 'maininventory.dat'
        with open(filename,'wb') as file:
            pickle.dump(self.maininv,file)

    def loadmaininventory(self):
        filename = 'maininventory.dat'
        try: 
            with open(filename,'rb') as file:
                data = pickle.load(file)
                # # testing 
                print("from load main inventory function: ")
                for mitem in data: 
                    print(str(mitem))
                
                # update the system's inventory with the correct quantities 
                for d in data: 
                    if d.name == "Sesame Bun":
                        self.load_maininv("Sesame Bun", d.quantity)
                    if d.name == "Muffin Buns":
                        self.load_maininv("Muffin Buns", d.quantity)
                    if d.name == "Chicken Patty":
                        self.load_maininv("Chicken Patty", d.quantity) 
                    if d.name == "Veg Patty":
                        self.load_maininv("Veg Patty", d.quantity)
                    if d.name == "Beef Patty":
                        self.load_maininv("Beef Patty", d.quantity)
                    if d.name == "Tomato":
                        self.load_maininv("Tomato", d.quantity)
                    if d.name == "Lettuce":
                        self.load_maininv("Lettuce", d.quantity)
                    if d.name == "Tomato sauce":
                        self.load_maininv("Tomato sauce", d.quantity)
                    if d.name == "Cheddar cheese":
                        self.load_maininv("Cheddar cheese", d.quantity)
                    if d.name == "Swiss cheese":
                        self.load_maininv("Swiss cheese", d.quantity)
        except EOFError:
            print("main inv EOF ERROR")
            self.savemaininventory()
        except FileNotFoundError: 
            print("main inv FileNotFoundError")
            self.savemaininventory()

    def savesideinventory(self):
        filename = 'sideinventory.dat'
        with open(filename,'wb') as file:
            pickle.dump(self.sideinv,file)

    def loadsideinventory(self):
        filename = 'sideinventory.dat'
        try: 
            with open(filename,'rb') as file:
                data = pickle.load(file)
                # testing 
                print("from load side inventory function: ")
                for mitem in data: 
                    print(str(mitem))

                # update the system's inventory with the correct quantities 
                for d in data: 
                    if d.name == "Fries":
                        self.load_sideinv("Fries", d.weight)
                    if d.name == "Nuggets":
                        self.load_sideinv("Nuggets", d.weight)
                    if d.name == "Strawberry Sundae":
                        self.load_sideinv("Strawberry Sundae", d.weight)
                    if d.name == "Chocolate Sundae":
                        self.load_sideinv("Chocolate Sundae", d.weight)
                    
        except EOFError:
            print("side inv EOF ERROR")
            self.savesideinventory()
        except FileNotFoundError: 
            print("side inv FileNotFoundError")
            self.savesideinventory()

    def savedrinkinventory(self):
        filename = 'drinkinventory.dat'
        with open(filename,'wb') as file:
            pickle.dump(self.drinkinv,file)

    def loaddrinkinventory(self):
        filename = 'drinkinventory.dat'
        try: 
            with open(filename,'rb') as file:
                data = pickle.load(file)
                # testing 
                print("from load drink inventory function: ")
                for mitem in data: 
                    print(str(mitem))

                # update the system's inventory with the correct quantities 
                for d in data: 
                    if d.name == "Coca Cola 375":
                        self.load_drinkinv("Coca Cola 375", d.quantity)
                    if d.name == "Coca Cola 600":
                        self.load_drinkinv("Coca Cola 600", d.quantity)
                    if d.name == "Orange Juice 250":
                        self.load_drinkinv("Orange Juice 250", d.quantity)
                    if d.name == "Orange Juice 450":
                        self.load_drinkinv("Orange Juice 450", d.quantity)
        except EOFError:
            print("drink inv EOF ERROR")
            self.savedrinkinventory()
        except FileNotFoundError: 
            print("drink inv FileNotFoundError")
            self.savedrinkinventory()


    #------------------------------















    # Properties
    @property
    def orders(self):
        return self._orders

    @property
    def sideinv(self):
        return self._sideinv

    @property
    def maininv(self):
        return self._maininv

    @property
    def drinkinv(self):
        return self._drinkinv  
