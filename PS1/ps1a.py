annual_salary = float(input("Enter your annual salary: "))
saving_percent = float(input("Enter the percent of your salary to save, as a decimal: "))
portion_saved = (annual_salary / 12) * saving_percent
total_cost = int(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_savings = 0 
months = 0
r = 0.04
while(current_savings <= portion_down_payment):
    current_savings += portion_saved
    current_savings += current_savings*(r/12)
    months += 1

print("Number of months : ", months)
