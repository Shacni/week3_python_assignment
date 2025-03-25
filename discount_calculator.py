def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount."""
    if discount_percent >= 20:
        final_price = price - (price * (discount_percent / 100))
        return final_price
    else:
        return price  # No discount applied

# Get user input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate the final price
final_price = calculate_discount(price, discount_percent)

# Print the result
if final_price == price:
    print(f"No discount applied. The final price is: ${price:.2f}")
else:
    print(f"The final price after {discount_percent}% discount is: ${final_price:.2f}")
