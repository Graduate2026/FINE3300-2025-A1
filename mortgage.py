# FINE 3300 Assignment 1 ( PART 1)
# DENNIS JACOB
# Description : the following function, with user inputs, calculates the different payment on different time frames for
# a given mortgage, quoted annual rate and amortization period.

import math

class MortgagePayment:
    def __init__(self, quoted_rate, years):
        self.quoted_rate=quoted_rate/100
        self.years = years
    
    def payments(self, principal):
        j = self.quoted_rate  

        def pay_for(f):
            r = (1 + j/2) ** (2.0 / f) - 1
            n = self.years * f
            return principal * (r / (1 - (1 + r) ** (-n)))

        monthly       = pay_for(12)
        semi_monthly  = pay_for(24)
        bi_weekly     = pay_for(26)
        weekly        = pay_for(52)
        rapid_bi_weekly = monthly / 2
        rapid_weekly    = monthly / 4

        return (round(monthly, 2), round(semi_monthly, 2),
                round(bi_weekly, 2), round(weekly, 2),
                round(rapid_bi_weekly, 2), round(rapid_weekly, 2))

if __name__ == "__main__":
    principal = float(input("Enter mortgage principal: "))
    rate = float(input("Enter quoted annual rate: "))
    years = int(input("Enter amortization period in years: "))

    mortgage = MortgagePayment(rate, years)
    results = mortgage.payments(principal)

    print(f"\nMonthly Payment: ${results[0]}")
    print(f"Semi-monthly Payment: ${results[1]}")
    print(f"Bi-weekly Payment: ${results[2]}")
    print(f"Weekly Payment: ${results[3]}")
    print(f"Rapid Bi-weekly Payment: ${results[4]}")
    print(f"Rapid Weekly Payment: ${results[5]}")





