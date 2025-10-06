import math

class MortgagePayment:
    def __init__(self, quoted_rate, years):
        self.quoted_rate=quoted_rate/100
        self.years = years
    
    def payments(self, principal):
        monthly_rate = (1 + self.quoted_rate / 2) ** (1/6) - 1
        n_months = self.years * 12
        monthly = principal * (monthly_rate / (1-(1+monthly_rate) ** -n_months))
        semi_monthly = monthly /2
        bi_weekly = monthly * 12/26
        weekly = monthly * 12/52
        rapid_bi_weekly = monthly /2
        rapid_weekly = monthly /4 
    
        return (round(monthly,2), round(semi_monthly, 2), 
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





