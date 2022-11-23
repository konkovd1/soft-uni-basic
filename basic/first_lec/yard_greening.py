price_per_square_meter = 7.61
discount = 0.18
yard_square_meters = float(input())

final_price = price_per_square_meter * yard_square_meters
final_price_with_discount = final_price - (final_price * discount)
the_discount = final_price * discount

print(f"The final price is: {final_price_with_discount} lv.")
print(f"The discount is: {the_discount} lv.")
