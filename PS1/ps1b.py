annual_salary = float(input("Enter your annual salary: "))
saving_percent = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = int(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi­annual raise, as a decimal: "))
portion_down_payment = 0.25 * total_cost
portion_saved = (annual_salary / 12) * saving_percent
current_savings = 0 
months = 0
r = 0.04
while(current_savings <= portion_down_payment):
    if months % 6 == 0 and months != 0:
        annual_salary += annual_salary * semi_annual_raise
        portion_saved = (annual_salary / 12) * saving_percent
    current_savings += portion_saved
    current_savings += current_savings*(r/12)
    print(current_savings)
    months += 1

print("Number of months : ", months)
