def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.

  Args:
    price: The original price of the item.
    discount_percent: The percentage of the discount.

  Returns:
    The final price after the discount, or the original price if
    the discount is less than 20%.
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Example
original_price = 100
discount_rate = 25
final_price_with_discount = calculate_discount(original_price, discount_rate)
print(f"Original price: ${original_price}")
print(f"Discount percentage: {discount_rate}%")
print(f"Final price: ${final_price_with_discount}")

print("\n---")

original_price_2 = 100
discount_rate_2 = 15
final_price_no_discount = calculate_discount(original_price_2, discount_rate_2)
print(f"Original price: ${original_price_2}")
print(f"Discount percentage: {discount_rate_2}%")
print(f"Final price (no discount applied): ${final_price_no_discount}")


def calculate_discount(price, discount_percent):
  """
  Calculates the final price after applying a discount.
  (This is the same function from Problem 1)
  """
  if discount_percent >= 20:
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price
  else:
    return price

# Main part of the program to get user input and print the result

  # Get the original price from the user
  original_price = float(input("Enter the original price of the item: "))

  # Get the discount percentage from the user
  discount_percentage = float(input("Enter the discount percentage: "))

  # Call the function with the user's input
  final_price = calculate_discount(original_price, discount_percentage)

  # Print the final price
  if final_price != original_price:
    print(f"\nThe final price after a {discount_percentage}% discount is: ${final_price:.2f}")
  else:
    print(f"\nNo discount was applied because the discount percentage was below 20%.")
    print(f"The original price is: ${original_price:.2f}")
