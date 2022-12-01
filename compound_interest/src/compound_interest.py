class CompoundInterest:
    
    def __init__(self, amount, interest_rate, years):
        self.p = amount
        self.r = interest_rate
        self.t = years

    def compound_interest(self, p, r, t):
        return p * ((1 + (r/12)) **(12 * t))

