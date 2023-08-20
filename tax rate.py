def calculate_tax(income):
    if income <= 14000:
        return income * 0.105
    elif income <= 48000:
        return 14000 * 0.105 + (income - 14000) * 0.175
    elif income <= 70000:
        return 14000 * 0.105 + (48000 - 14000) * 0.175 + (income - 48000) * 0.30
    elif income <= 180000:
        return 14000 * 0.105 + (48000 - 14000) * 0.175 + (70000 - 48000) * 0.30 + (income - 70000) * 0.33
    else:
        return (14000 * 0.105 + 
                (48000 - 14000) * 0.175 + 
                (70000 - 48000) * 0.30 + 
                (180000 - 70000) * 0.33 + 
                (income - 180000) * 0.39)

income = float(input("Enter your income: "))
tax = calculate_tax(income)
print(f"You owe ${tax:,.2f} in taxes.")


