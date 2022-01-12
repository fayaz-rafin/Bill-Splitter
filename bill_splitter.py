#Bill Splitter in Python

total_bill = float(input("Please input your total bill? "))
tip_amount = int(input("What percentage of tip would you like to leave? "))
number_of_people = int(input("How many people do you want to split the bill with? "))

payment_per_person = (
    round(float(((tip_amount / 100 + 1) * total_bill) / number_of_people), 2))
print(f"Each person should pay ${payment_per_person}")
