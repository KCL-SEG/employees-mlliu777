"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary="", hour_rate = "", hour_worked ="", commission = ""):
        self.name = name
        self.salary = salary
        self.hour_rate = hour_rate
        self.hour_worked = hour_worked
        self.commission = commission
        self.totalPay = 0

    def get_pay(self):
        total = 0
        if self.salary:
            total += self.salary
        elif self.hour_rate and self.hour_worked:
            total += self.hour_rate * self.hour_worked

        if self.commission:
            total += int(self.commission.getCommission())
        self.totalPay = total
        return total

    def __str__(self):
        payInfo = f"{self.name} works on a "
        if self.salary:
            payInfo += f"monthly salary of {self.salary}"
        elif self.hour_rate and self.hour_worked:
            payInfo += f"contract of {self.hour_worked} hours at {self.hour_rate}/hour"

        if self.commission:
            if self.commission.getBonus():
                payInfo += f" and receives a bonus commission of {self.commission.getBonus()}"
            elif self.commission.getContract():
                payInfo += f" and receives a commission for {self.commission.getContract()[1]} contract(s) at {self.commission.getContract()[0]}/contract"

        payInfo += f".  Their total pay is {self.totalPay}."
        return payInfo

class Commission:
    def __init__(self, bonus = "", contract_number = "", contract_rate = ""):
        self.bonus = bonus
        self.contract_number = contract_number
        self.contract_rate = contract_rate

    def getCommission(self):
        if self.bonus:
            return self.bonus
        else:
            return int(self.contract_rate) * int(self.contract_number)

    def getBonus(self):
        return self.bonus

    def getContract(self):
        return (self.contract_rate, self.contract_number)

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hour_rate = 25, hour_worked = 100 )

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, commission = Commission(contract_number = "4", contract_rate = "200"))


# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hour_rate = 25, hour_worked = 150, commission = Commission(contract_number = "3", contract_rate = "220") )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000,commission = Commission(bonus = "1500"))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hour_rate = 30, hour_worked = 120, commission = Commission(bonus = "600"))
