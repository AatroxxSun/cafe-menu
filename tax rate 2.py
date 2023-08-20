def calculate_tax(income):
    brackets = [(14000, 0.105), (48000, 0.175), (70000, 0.30), (180000, 0.33)]
    tax = 0
    prev_bracket_limit = 0
    
    for bracket_limit, rate in brackets:
        if income > bracket_limit:
            tax += (bracket_limit - prev_bracket_limit) * rate
        else:
            tax += (income - prev_bracket_limit) * rate
            return round(tax, 2)
        prev_bracket_limit = bracket_limit

    # If the income is higher than the last bracket
    tax += (income - prev_bracket_limit) * 0.39
    return round(tax, 2)

income = float(input("Enter your income in NZD: "))
tax_amount = calculate_tax(income)
print(f"You owe ${tax_amount:,.2f} in taxes based on New Zealand tax rates.")
