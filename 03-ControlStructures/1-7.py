basic_salary = 5000
total_salary = 0
bonus = 0.3
is_bonus = input('Does the employee receive a bonus? (Y/N):') 
if is_bonus == 'Y' or is_bonus == 'y':
    total_salary = basic_salary+(basic_salary*bonus)
else:
    total_salary = basic_salary
print(f'Basic salary: {basic_salary}')
print(f'Bonus included? {is_bonus}')
print(f'Total salary: {total_salary}')