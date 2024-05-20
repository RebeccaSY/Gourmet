from routes import app,system

if __name__ == '__main__':
    # SIGINT to stop (Ctrl + C)
    app.run(debug=True, port=5001, use_reloader=False)

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

    print ("From System's orders load")
    print(len(system.orders))
    for mitem in system.orders: 
        print(str(mitem))

    # # Saves the data
    print('Saving')
    system.savemaininventory()
    system.savesideinventory()
    system.savedrinkinventory()
    system.saveallorders()
    print('Save complete')

    system.loadmaininventory()
    system.loadsideinventory()
    system.loaddrinkinventory()
    system.loadallorders()
    
