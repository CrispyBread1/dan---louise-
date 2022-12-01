class CompoundInterest:
    
    def __init__(self, amount, interest_rate, years):
        self.p = amount
        self.r = interest_rate
        self.t = years

    def compound_interest(self):
        return round(self.p * ((1 + (self.r/12)) **(12 * self.t)), 2)

