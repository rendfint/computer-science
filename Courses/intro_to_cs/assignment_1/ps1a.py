total_cost = input("Enter the cost of your dream house: ")
total_cost = float(total_cost)

annual_salary = input("Enter your annual income: ")
annual_salary = float(annual_salary)

portion_saved = input("Enter the percent of your income you will save: ")
if portion_saved.find("%") or portion_saved.startswith("%") :
    portion_saved = portion_saved.replace("%", "")
if float(portion_saved) >= 1 :
    portion_saved = float(portion_saved)
    portion_saved /= 100

portion_down_payment = 0.25
r = 0.04
current_savings = 0.0
down_payment = total_cost * portion_down_payment
monthly_salary = annual_salary/12

months = 0
while current_savings < down_payment :
    current_savings += current_savings*(r/12)
    current_savings += monthly_salary*portion_saved
    months += 1

print("It will take", months, "months to save enough money for the down payment.")