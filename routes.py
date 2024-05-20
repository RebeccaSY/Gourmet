from flask import render_template, request, redirect, url_for, abort, session, make_response
from server import app, system, store_all_orders
from src.orders import Order
from src.mainorders import MainOrder
from src.drinkorders import DrinkOrder
from src.sideorders import SideOrder
from src.cart_mgr import Cart, CartManager


'''
Dedicated page for "page not found"
'''
@app.route('/404')
@app.errorhandler(404)
def page_not_found(e=None):
    return render_template('404.html'), 404

# Cookie CODE --------------------------------------------------

# sets up session base
# creates security 
# a key value pair is created in "session"
# session is similar to a dictionary of cookies 
def fetch_session_cart(num = 0):
    # CART ID ON CLIENT SIDE 
    # SHOPPING CART's CONTENTS ON SERVER SIDE

    if num == 1:
        print('deleting old cart')
        del store_all_orders[session['cart']]

        print('creating new cart')
        # creating cart object 
        cart = Cart()
        # assigning a cookie called 'cart' to the cart's id 
        # we just store the shopping cart's ID in the session
        session['cart'] = cart._id
        # on the server we have a list of orders which in turn stores the cart! 

        #               key, value 
        # customer 1 -> 1, shopping cart... 
        # customer 2 -> 2, shopping cart... 

        # cart._id = key 
        # cart = value 
        store_all_orders[cart._id] = cart

        # create Order Object that is unique to the client 
        Ord = Order(cart._id)
        # pass this order into the system 
        system.add_order(Ord)
        # to get this order we search the system by order id and return the order object from the system list 

    else:
        # Creates a new cart first if the cart never existed
        # if the cookie with key value cart does not exist in the dictionary,
        # they are a new customer so create a new cart for them 
        
        # cart created in cart_mgr 
        if 'cart' not in session:
            print('cart not in session')
            # creating cart object 
            cart = Cart()
            # assigning a cookie called 'cart' to the cart's id 
            # we just store the shopping cart's ID in the session
            session['cart'] = cart._id
            # on the server we have a list of orders which in turn stores the cart! 

            #               key, value 
            # customer 1 -> 1, shopping cart... 
            # customer 2 -> 2, shopping cart... 

            # cart._id = key 
            # cart = value 
            store_all_orders[cart._id] = cart

            # create Order Object that is unique to the client 
            Ord = Order(cart._id)
            # pass this order into the system 
            system.add_order(Ord)
            # to get this order we search the system by order id and return the order object from the system list 


        else:
            # Check the current cookie is valid

            # if the current cookie is valid, then since we have the 'cart' cookie locally
            # we then only need to return the order id that matches this specific cart with session['cart']
            print('cart in session')
            try:
                return store_all_orders[session['cart']]
            except KeyError: 
                # if there is no persistance in the serverside then we need to handle the case 
                # where there is a client side cookie but no serverside info 

                # here we create a new cookie for the server from the client 
                print('exception raised: cart not in session')
                cart = Cart()
                session['cart'] = cart._id
                store_all_orders[cart._id] = cart
                print(cart._id)
                print("session cookie from ex: " ,session['cart'])

                # create Order Object that is unique to the client 
                Ord = Order(cart._id)
                # pass this order into the system 
                system.add_order(Ord)

        # return the order id that matches this specific cookie with session['cart']
    return store_all_orders[session['cart']]


# end cookie CODE --------------------------------------------------





# START OF OUR CODE --------------------------------------------------
@app.route('/', methods=["GET", "POST"])
def homehtml():
    if request.method == 'POST':
        part = 'A'
        searchnum = request.form["search"]
        ordmsg = system.view_order(int(searchnum))
        return render_template('home.html', part = part, order = ordmsg)


    return render_template('home.html')

@app.route('/main', methods=["GET", "POST"])
def mainhtml():
    # somehow the user client needs to store an instance of thier order object O             
    # get cookie's order ID 
    cartnum = fetch_session_cart()
    print(str(cartnum))

    m = MainOrder(cartnum.id)    
    items = m.main_price #gets dictionary with names and prices from MainOrder class
    
    #This is to display proper prices of chicken and veg burgers
    chicken_price = items["Chicken Patty"]+2*items["Sesame Bun"]+items["Lettuce"]+items["Tomato"]
    veg_price = items["Veg Patty"]+2*items["Sesame Bun"]+items["Lettuce"]+items["Tomato"]
    
    if request.method == 'POST':   
        #for custom burgers  
        if 'customise' in request.form :            
            return render_template('main.html', items=items, main_page="customise")                         
        if 'submit_button' in request.form: 
            quantities = {}
            #finds out the quantity the customer entered in and stores it in a dictionary
            for name, price in items.items():
                quantities[name] = int(request.form[name])  
                       
            #adds it to main orders
            for name, amount in quantities.items():
                if amount > 0:
                    m.addMain(name, amount)                       
                
            msg = m.checkMainAval(system.maininv)
            if msg == "" and m.cal_price() > 0:
                msg = "Successfully addded to Cart" 
                
                # to add we get the client's unique order object from the system 
                # by searching by ID 
                Ord = system.view_order(cartnum.id)
                                
                err = Ord.addMainOrder(m,system.maininv)                 
            # print(err)
                print(Ord)
            return render_template('main.html', error_msg = msg, items=items, main_page="customise", cartnum = cartnum)
       
       #for ready-made burgers 
        if 'submit_bases' in request.form:
            base_quantities = {}
            base_price = 0
            #finds out the quantity the customer entered in and stores it in a dictionary
            base_quantities['chickenburger'] = int(request.form['chickenburger'])
            base_quantities['vegburger'] = int(request.form['vegburger'])  
            
            #add ingredients from base chicken burger to main orders
            if base_quantities['chickenburger'] > 0 or base_quantities['vegburger'] > 0:
                m.addMain("Sesame Bun", 2*(base_quantities['chickenburger'] + base_quantities['vegburger']))
                if base_quantities['chickenburger'] > 0: m.addMain("Chicken Patty", base_quantities['chickenburger'])
                if base_quantities['vegburger'] > 0: m.addMain("Veg Patty", base_quantities['vegburger'])
                m.addMain("Lettuce", base_quantities['chickenburger'] + base_quantities['vegburger'])
                m.addMain("Tomato", base_quantities['chickenburger'] + base_quantities['vegburger'])
                
                #base_price =  7.50*base_quantities['chickenburger'] + 5*base_quantities['vegburger']              
                                
                
            msg = m.checkMainAval(system.maininv,True) #The 'True' is indicating that the customer is ordering a base
            if msg == "" and m.cal_price() > 0:
                msg = "Successfully addded to Cart" 
                
                # to add we get the client's unique order object from the system 
                # by searching by ID 
                Ord = system.view_order(cartnum.id)
                if Ord.order_status == 'Pending':
                    err = Ord.addMainOrder(m,system.maininv,True)
                    Ord.setBase(True)                
                    print(err)
                    print(m)
                    print(Ord)
                    msg = "Successfully addded to Cart" 
                else: 
                    msg = "please wait for your original order to be completed before ordering more. If there is an error clear your cookies"
            return render_template('main.html', error_msg = msg, items=items, main_page="baseburgers", cartnum = cartnum)
            
    return render_template('main.html', error_msg = '', items=items, main_page="baseburgers", cartnum = cartnum, chicken_price=chicken_price, veg_price=veg_price)

@app.route('/drink', methods=["GET", "POST"])
def drinkhtml( ):
    # somehow the user client needs to store an instance of thier order object O             
    # get cookie's order ID 
    cartnum = fetch_session_cart()
    print(str(cartnum))

    d = DrinkOrder(cartnum.id)
    items = d.drink_price #gets dictionary with names and prices from DrinkOrder class
    
    if request.method == 'POST':
        quantities = {}
        #finds out the quantity the customer entered in and stores it in a dictionary
        for name, price in items.items():
            quantities[name] = int(request.form[name])  
                   
        #adds it to drink orders
        for name, amount in quantities.items():
            if amount > 0:
                d.addDrink(name, amount)                       
            
        msg = d.checkDrinkAval(system.drinkinv)
        if msg == "" and d.cal_price() > 0:

            # to add we get the client's unique order object from the system 
            # by searching by ID 
            Ord = system.view_order(cartnum.id)
            if Ord.order_status == 'Pending':
                err = Ord.addDrinkOrder(d,system.drinkinv)
                msg = "Successfully addded to Cart" 
            else: 
                msg = "please wait for your original order to be completed before ordering more. If there is an error clear your cookies"
            # print(err)
        print(d)
        return render_template('drink.html', error_msg = msg, items=items, cartnum = cartnum)
    return render_template('drink.html', items=items)
    

@app.route('/side', methods=["GET", "POST"])
def sidehtml():
    # somehow the user client needs to store an instance of thier order object O
    
    cartnum = fetch_session_cart()
    print(str(cartnum))

    s = SideOrder(cartnum.id)
    items = s.side_price #gets dictionary with names and prices from SideOrder class
    
    if request.method == 'POST':
        quantities = {}
        #finds out the quantity the customer entered in and stores it in a dictionary
        for name, price in items.items():
            quantities[name] = int(request.form[name])  
                   
        #adds it to side orders
        for name, amount in quantities.items():
            if amount > 0:
                s.addSide(name, amount)    
     
        msg = s.checkSideAval(system.sideinv)
        if msg == "" and s.cal_price() > 0:
            
            Ord = system.view_order(cartnum.id)
            # to stop more orders
            if Ord.order_status == 'Pending':
                err = Ord.addSideOrder(s,system.sideinv)
                msg = "Successfully addded to Cart" 
            else: 
                msg = "please wait for your original order to be completed before ordering more. If there is an error clear your cookies" 
            # print(err)
        print(s)    
        return render_template('side.html', error_msg = msg, items=items, cartnum = cartnum)

    return render_template('side.html', items=items)


@app.route('/myorder')
def myorderhtml():
    cartnum = fetch_session_cart()
    print(str(cartnum))
    Ord = system.view_order(cartnum.id)
    returnSTR_ORD = str(Ord)
    if returnSTR_ORD == "":
        returnSTR_ORD = "Order is Empty"
    return render_template('myorder.html',  cartnum = cartnum, order = returnSTR_ORD )


@app.route('/checkout', methods=["GET", "POST"])
def checkouthtml():
    Part = 'A'
    cartnum = fetch_session_cart()
    if request.method == 'POST':
        Part = 'B'
        Ord = system.view_order(cartnum.id)
        price = 0
        if Ord.order_status == 'Pending':
            price = Ord.calc_fee()
            if price == 0:
                returnSTR_ORD = "Order is Empty"
                errmsg = "Nothing has been checked out"
            else: 
                errmsg = system.confirm_Order(cartnum.id, Ord.base)
                print("system.confirm order output   " + errmsg)
                returnSTR_ORD = str(Ord)
                if errmsg == "": 
                    errmsg = "Success: Your Order Number is " + str(Ord.order_id)

            # # testing only 
            # print("order is in the system")
            # for ordd in system.view_all_orders():
            #     print(ordd)

            # # print out inventory 
            # for mitem in system.maininv: 
            #     print(str(mitem))
        elif Ord.order_status == 'Confirmed':
            returnSTR_ORD = "your order has already been confirmed: please wait"
            errmsg = ""
        else: 
            returnSTR_ORD = ""
            errmsg = ""
        return render_template('checkout.html', order = returnSTR_ORD, cartnum = cartnum, part = Part, msg = errmsg)


    cartnum = fetch_session_cart()
    print(str(cartnum))
    Ord = system.view_order(cartnum.id)
    price = 0
    if Ord.order_status == 'Pending':
        returnSTR_ORD = str(Ord)
        price = Ord.calc_fee()
        if price == 0:
            returnSTR_ORD = "Order is Empty"
    elif Ord.order_status == 'Confirmed':
        returnSTR_ORD = "your order has already been confirmed: please wait"
        Part = 'B'
    else: 
        returnSTR_ORD = ""
    return render_template('checkout.html', order = returnSTR_ORD, cartnum = cartnum, part = Part, price = price)



@app.route('/staff', methods=["GET", "POST"])
def homestaffhtml():    
    Orders = system.view_all_orders()
    if request.method == 'POST':    
        if "complete" in request.form:
            print("complete button pressed yay")               
            # create a new cookie for the customer 
            oid = int(request.form["order_num"])
            print("The value inputted was:"+str(oid))
            complete = system.complete_Order(oid)
            #print(o)
            if complete == 1:
                cartnum = fetch_session_cart(complete)
                print("---------------Created new Cart? -------------------" + str(cartnum))
            Orders = system.view_all_orders()
            return render_template('home_staff.html', orders=Orders)
    return render_template('home_staff.html', orders=Orders)

@app.route('/maininventory', methods=["GET", "POST"])
def maininvhtml():
    maininv = system.maininv
    if request.method == 'POST':
        if 'Refill' in request.form:
            quantities = {}
            #finds out the quantity the staff entered in and stores it in a dictionary
            for ingredient in maininv:
                quantities[ingredient.name] = int(request.form[ingredient.name])  
                     
            #refills inventory
            for name, refill in quantities.items():
                if refill > 0:
                    system.update_maininv(name, refill) 
                    
            newmaininv = system.maininv                        
            return render_template('maininventory.html', inventory=newmaininv)
    return render_template('maininventory.html', inventory=maininv)

@app.route('/sideinventory', methods=["GET", "POST"])
def sideinvhtml():
    sideinv = system.sideinv
    if request.method == 'POST':
        if 'Refill' in request.form:
            quantities = {}
            #finds out the quantity the staff entered in and stores it in a dictionary
            for ingredient in sideinv:
                print(ingredient.name + str(ingredient.weight))
                quantities[ingredient.name] = int(request.form[ingredient.name])  
                     
            #refills inventory
            for name, refill in quantities.items():
                if refill > 0:
                    system.update_sideinv(name, refill) 
                    
            newsideinv = system.sideinv                        
            return render_template('sideinventory.html', inventory=newsideinv)
    return render_template('sideinventory.html', inventory=sideinv)

@app.route('/drinkinventory', methods=["GET", "POST"])
def drinkinvhtml():
    drinkinv = system.drinkinv
    if request.method == 'POST':
        if 'Refill' in request.form:
            quantities = {}
            #finds out the quantity the staff entered in and stores it in a dictionary
            for ingredient in drinkinv:
                quantities[ingredient.name] = int(request.form[ingredient.name])  
                     
            #refills inventory
            for name, refill in quantities.items():
                if refill > 0:
                    system.update_drinkinv(name, refill) 
                    
            newdrinkinv = system.drinkinv                        
            return render_template('drinkinventory.html', inventory=newdrinkinv)
    return render_template('drinkinventory.html', inventory=drinkinv)
   
        

# end OF OUR CODE --------------------------------------------------
