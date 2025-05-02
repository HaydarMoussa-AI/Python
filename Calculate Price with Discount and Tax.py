def calculate_final_price(price, discount_rate, tax_rate):
    
    # Calculate discount ammount
    discout_amount = (discount_rate * price) / 100
    price_after_discount = price - discout_amount
    
    # Calculate the tax 
    tax_amount = (tax_rate * price) / 100
    final_price = price_after_discount + tax_amount
    
    return final_price 

# Calling the function 
A = calculate_final_price(200, 10, 8)
print(f"The final price is :) : ${A :.2f}")
