

class OrderError(Exception):
	def __init__(self, Message):
		self._Message = Message
	def __str__(self):
		return self._Message

def addMainOrderError(mainorder,inv_main, base=False):
    errorlist = []
    try: 
        m = mainorder.checkMainAval(inv_main, base)
        if m != "":
            raise OrderError(m)
    except OrderError as err:
        errorlist.append(err)
    return errorlist

def addDrinkOrderError(drinkorder,inv_drink):
    errorlist = []
    try: 
        d = drinkorder.checkDrinkAval(inv_drink)
        if d != "":
            raise OrderError(d)
    except OrderError as err:
        errorlist.append(err)
    return errorlist

def addSideOrderError(sideorder,inv_side):
    errorlist = []
    try: 
        s = sideorder.checkSideAval(inv_side)
        if s != "":
            raise OrderError(s)
    except OrderError as err:
        errorlist.append(err)
    return errorlist
