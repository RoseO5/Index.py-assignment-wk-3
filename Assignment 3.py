def calculate_discount(price, discount_percent):
    """Calculate the final price after applying discount if discount >= 20%"""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # No discount applied
        return price

# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after applying {discount_percent}% discount is: {final_price:.2f}")
else:
    print(f"No discount applied. The original price is: {final_price:.2f}")

