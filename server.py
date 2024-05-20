from flask import Flask
from init import master_system

app = Flask(__name__)
app.secret_key = 'very-secret-123'  # Used to add entropy

system = master_system()

store_all_orders = {}

# # see what is inside 
print ("From System's Main inventory before load")
print(len(system.maininv))
for mitem in system.maininv: 
    print(str(mitem))

print ("From System's side inventory before load")
print(len(system.sideinv))
for mitem in system.sideinv: 
    print(str(mitem))

print ("From System's drink inventory before load")
print(len(system.drinkinv))
for mitem in system.drinkinv: 
    print(str(mitem))

print ("From System's orders before load")
print(len(system.orders))
for mitem in system.orders: 
    print(str(mitem))

# load data 
print ("----------------------------------------")
print('Loading')
system.loadmaininventory()
system.loadsideinventory()
system.loaddrinkinventory()
print("only loading confirmed orders")
system.loadallorders()
print('Load complete')


# see what is inside 
print ("----------------------------------------")
print ("From the System's Main inventory after load")
print(len(system.maininv))
for mitem in system.maininv: 
    print(str(mitem))

print ("From System's side inventory before load")
print(len(system.sideinv))
for mitem in system.sideinv: 
    print(str(mitem))

print ("From System's drink inventory before load")
print(len(system.drinkinv))
for mitem in system.drinkinv: 
    print(str(mitem))

print ("From System's orders after load")
print(len(system.orders))
for mitem in system.orders: 
    print(str(mitem))