print("Wellcome to the tip calculator")

bill = float(input("What was the total bill? $"))
percentualTip = int(input("What percentage tip would you like to give? 10, 12 ou 15? "))
people = int(input("How many people to split the bill? "))

total = (bill + ((bill * percentualTip) / 100)) / people

print(f"Each person should pay: ${round(total, 2)}")