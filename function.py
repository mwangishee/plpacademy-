# Function to calculate the final price after discount
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

price = float(input("Enter the original price of the item: "))

# Ask user for discount percentage
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print result
print(f"The final price is: {final_price}")
