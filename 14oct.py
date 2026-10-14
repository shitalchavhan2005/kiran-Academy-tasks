
a = 100
b = 100
c = 100
d = 100
e = 100

# Electronics: 18% GST
electronics_total = a + b
electronics_gst = electronics_total * 18 / 100
electronics = electronics_total + electronics_gst

# Fashion: 13% GST
fashion_total = c + d
fashion_gst = fashion_total * 13 / 100
fashion = fashion_total + fashion_gst

# Food: 7% GST
food_gst = e * 7 / 100
food = e + food_gst

# Total after GST
total = electronics + fashion + food

# 20% discount
discount = total * 20 / 100

# Final payable amount
final_amount = total - discount

# Display bill
print(f"Electronics after GST: Rs. {electronics:.2f}")
print(f"Fashion after GST: Rs. {fashion:.2f}")
print(f"Food after GST: Rs. {food:.2f}")
print(f"Total after GST: Rs. {total:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Final payable amount: Rs. {final_amount:.2f}")
