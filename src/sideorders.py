# these classes only put together what the customer wants 
class SideOrder():
    def __init__(self, client_ID ):
        
        self._id = client_ID

        self._sides = {"Small Fries":0,
                        "Medium Fries":0,
                        "Large Fries":0,
                        "6 pack nuggets":0,
                        "3 pack nuggets":0,
                        "Small Strawberry Sundae": 0,
                        "Medium Strawberry Sundae": 0,
                        "Large Strawberry Sundae": 0,
                        "Small Chocolate Sundae": 0,
                        "Medium Chocolate Sundae": 0,
                        "Large Chocolate Sundae": 0 }

        self._side_price = {"Small Fries":5,
                        "Medium Fries":5,
                        "Large Fries":5,
                        "6 pack nuggets":5,
                        "3 pack nuggets":5,
                         "Small Strawberry Sundae": 5,
                        "Medium Strawberry Sundae": 5,
                        "Large Strawberry Sundae": 5,
                        "Small Chocolate Sundae": 5,
                        "Medium Chocolate Sundae": 5,
                        "Large Chocolate Sundae": 5 }
                        

    def checkSideAval(self,side_inventory_list):
        # To traverse a list of sides objects 
        error = ""
        for s in side_inventory_list:
            if s.name == "Fries" and self.cal_fry_weight() > s.weight:
                error = error + "Insufficient quantity " + s.name + ". There are only " + str(s.weight) + " grams avaliable. You requested " +  str(self.cal_fry_weight()) + "g\n"
                break
            if s.name == "Nuggets" and self.cal_nugget_weight() > s.weight:
                error = error + "Insufficient quantity " + s.name + ". There are only " + str(s.weight) + " avaliable. You requested " +  str(self.cal_nugget_weight()) + "g\n"
                break
            if s.name == "Strawberry Sundae" and self.cal_Ssundae_weight() > s.weight:
                error = error + "Insufficient quantity " + s.name + ". There are only " + str(s.weight) + " avaliable. You requested " +  str(self.cal_Ssundae_weight()) + "g\n"
                break
            if s.name == "Chocolate Sundae" and self.cal_Csundae_weight() > s.weight:
                error = error + "Insufficient quantity " + s.name + ". There are only " + str(s.weight) + " avaliable. You requested " +  str(self.cal_Csundae_weight()) + "g\n"
                break

        # error = 0
        # for s,number in side_inventory_list.inv_sides.items(): 
        #     if self.sides[s] > number:
        #         error = 1
        #         break
        return error 

    def cal_nugget_weight(self):
        weight = 0
        for s,number in self.sides.items():
            if s == "3 pack nuggets":
                weight = weight + number*75
            if s == "6 pack nuggets":
                weight = weight + number*150
        return weight 

    def cal_fry_weight(self):
        weight = 0
        for s,number in self.sides.items():
            if s == "Small Fries":
                weight = weight + number*75
            if s == "Medium Fries":
                weight = weight + number*125
            if s == "Large Fries":
                weight = weight + number*175
        return weight
        
    def cal_Ssundae_weight(self):
        weight = 0
        for s,number in self.sides.items():
            if s == "Small Strawberry Sundae":
                weight = weight + number*75
            if s == "Medium Strawberry Sundae":
                weight = weight + number*125
            if s == "Large Strawberry Sundae":
                weight = weight + number*175
        return weight
        
    def cal_Csundae_weight(self):
        weight = 0
        for s,number in self.sides.items():
            if s == "Small Chocolate Sundae":
                weight = weight + number*75
            if s == "Medium Chocolate Sundae":
                weight = weight + number*125
            if s == "Large Chocolate Sundae":
                weight = weight + number*175
        return weight                

    def cal_price(self):
        price = 0
        for s,number in self.side_price.items():
            price = price + self.sides[s]*number
        return price

    def addSide(self, sidename, quantity):
        self.sides[sidename] = quantity

    @property
    def id(self):
        return self._id

    @property
    def sides(self):
        return self._sides

    @property
    def side_price(self):
        return self._side_price

    def __str__(self):
        sideINorder = ''
        for side,number in self.sides.items():
            if number != 0:
                sideINorder = sideINorder + side + ": " + str(number) + " "
        return '\n Side Order: ' + sideINorder

