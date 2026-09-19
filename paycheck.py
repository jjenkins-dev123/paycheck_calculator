# Name: Madison Jones
# Date: 9/18/26
# Course: COMP 163
# Project 1: Paycheck Calculator

# Put your name after "# Name:" above. The grader checks that it is filled in.

# Read four values from the user, in this order:
name = input('Enter Employee Name: ')
hrs_work = float(input('Enter Hours Worked: '))
hr_rate = float(input('Enter Hourly Rate: '))
tax_rate = float(input('Enter Tax Rate: '))

#
# Hours worked and the hourly rate can have a fraction in them, like 37.5
# hours or 10.25 hours. Use float() for all three numbers, not int().
# int("37.5") crashes.
#
# Then calculate:
gross_pay = hrs_work * hr_rate
tax_held = gross_pay * (tax_rate / 100)
net_pay = gross_pay - tax_held

#
# Then print the four required output lines.
# The exact format is in README.md. Match it exactly or the tests will fail.
print(f'Employee: {name}')
print(f'Gross pay: ${gross_pay:.2f}')
print(f'Tax withheld: ${tax_held:.2f}')
print(f'Net pay: ${net_pay:.2f}')

