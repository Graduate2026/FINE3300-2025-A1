# FINE 3300 - Assignment 1 (Part 2)
# Author: Dennis Jacob
# Description: Reads the latest USD/CAD rate from the Bank of Canada CSV
#              and converts amounts between CAD and USD using user input.

class ExchangeRates:
    def __init__(self, file_name):
        self.file_name = file_name
        self.date = ""
        self.rate = 0.0      
        self.load_latest()

    def load_latest(self):
        
        f = open(self.file_name, "r")
        lines = f.readlines()
        f.close()

        # header row (column names) and last data row (most recent)
        header = lines[0].strip().split(",")
        last = lines[-1].strip().split(",")

        
        i = 0
        while i < len(header):
            header[i] = header[i].strip()
            i = i + 1

        j = 0
        while j < len(last):
            last[j] = last[j].strip()
            j = j + 1

        # find the column index for "USD/CAD" in the header
        usd_index = 0
        k = 0
        while k < len(header):
            if header[k] == "USD/CAD":
                usd_index = k
                break
            k = k + 1

        
        self.date = last[0]
        self.rate = float(last[usd_index])

    def convert(self, amount, from_currency, to_currency):
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate            
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate            
        else:
            return amount

    def prompt_and_convert(self):
    
        print("Latest Date:", self.date)
        print("USD/CAD Rate:", self.rate)
        print("\nChoose conversion:")
        print("1) USD to CAD")
        print("2) CAD to USD")

        choice = input("Enter 1 or 2: ").strip()
        amt_text = input("Enter the amount: ").strip()
        amount = float(amt_text)

        if choice == "1":
            result = self.convert(amount, "USD", "CAD")
            print(amount, "USD in CAD =", round(result, 2))
        elif choice == "2":
            result = self.convert(amount, "CAD", "USD")
            print(amount, "CAD in USD =", round(result, 2))
        else:
            print("Invalid choice")
        

if __name__ == "__main__":
    ex = ExchangeRates("BankOfCanadaExchangeRates.csv")
    ex.prompt_and_convert()
