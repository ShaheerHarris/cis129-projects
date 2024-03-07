print("My Coffee and Muffin Shop")

def calculate_total_cost(coffee_amount, muffin_amount, boba_amount, tea_amount):
    # Prices
    coffee_price = 5
    muffin_price = 4
    donut_price = 2
    tea_price = 3
    tax_rate = 0.06

    # Subtotal
    subtotal = (coffee_price * coffee_amount) + (muffin_price * muffin_amount) + (donut_price * donut_amount) + (tea_price * tea_amount)

    # Taxes
    tax_amount = (subtotal * tax_rate)

    # Total Cost
    total_cost = (subtotal + tax_amount)

    return total_cost

# Order
coffee_amount = int(input("Enter the number of coffees: "))
muffin_amount = int(input("Enter the number of muffins: "))
donuts_amount = int(input("Enter the number of donuts: "))
tea_amount = int(input("Enter the number of teas: "))
# Total cost 
total_cost = calculate_total_cost(coffee_amount, muffin_amount, donut_amount, tea_price)

# Results
print("\nTotal Cost: $", total_cost, "\n\nThank you for shopping with us!")

