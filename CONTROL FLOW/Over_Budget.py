# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  result = food_bill + electricity_bill + internet_bill + rent
  if budget >= result:
    return False
  else:
    return True
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True