annual_salary = int(input("Enter your annual salary : "))
salary = annual_salary
lower = 0
upper = 10000
saving_percent = 5000
down_payment = 250000
steps = 0

while True:
    savings = 0
    salary = annual_salary
    portion = (annual_salary / 12) * (saving_percent / 10000)

    for r in range(1, 37):
        savings += portion
        savings += savings * (0.04 / 12)

        if r % 6 == 0:
            salary += salary * 0.07
            portion = (salary / 12) * (saving_percent / 10000)

    if abs(down_payment - savings) <= 10000:
        break
    
    if down_payment < savings:
        upper = saving_percent
    else:
        lower = saving_percent

    saving_percent = (upper + lower) // 2
    steps += 1

print("Percent : ", saving_percent / 10000)
print("Steps : ", steps)
