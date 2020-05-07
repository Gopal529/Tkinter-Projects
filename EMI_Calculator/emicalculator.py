import math

class emicalculator:

    def __init__(self, amount,r, mons):
	    
        self.amount=amount
        self.r=r
        self.apr=self.r/12/100
        self.mons=mons
        self.emi=(self.amount*self.apr*math.pow((1+self.apr),self.mons))/(math.pow((1+self.apr),self.mons)-1)
        self.total_amount=self.emi*self.mons
        self.interest_amount=self.total_amount-self.amount
		
    def emi_value(self):
        """This function returns Monthly EMI amount"""
        return round(self.emi,2)
		
    def total_amount_value(self):
	    """This function returns Total payable amount"""
		
	    return round(self.total_amount,2)
		
    def total_interest_value(self):
	    """This function returns Total intrest amount"""
		
	    return round(self.interest_amount,2)
