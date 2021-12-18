annual_salary = input("Enter your annual income: ")
if len(annual_salary) < 1 : annual_salary = 150000
annual_salary = float(annual_salary)

total_cost = 1000000.00
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
down_payment = total_cost * portion_down_payment

portion_saved = 0
portion_percent = 0.0
portion_range = range(10000)
count = 0

while True :
    portion_saved = portion_range[int(len(portion_range)/2)]
    portion_percent = portion_saved / 10000
    if portion_saved >= 9999 :
        print("Can't save enough in 36 months to pay the down payment")
        break
    count += 1
    months = 0
    current_savings = 0.0
    monthly_salary = annual_salary/12
    while months < 36 :
        current_savings += current_savings*(r/12)
        current_savings += monthly_salary*portion_percent
        months += 1
        if (months % 6) == 0 :
            monthly_salary += int(monthly_salary) * semi_annual_raise
    if (down_payment - 100) < current_savings and current_savings < (down_payment + 100) :
        print("Saving", portion_saved/100, "% of your monthly salary will amount to", int(current_savings), "in 36 months")
        print("Found in", count, "bisections")
        break
    if current_savings < down_payment :
        portion_range = range(portion_saved, portion_range[-1] + 1)
        continue
    if current_savings > down_payment :
        portion_range = range(portion_range[0], portion_saved)
        continue