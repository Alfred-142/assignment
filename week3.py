#creating a function to calculate discounts 
def calculate_discount(price, discount_percentage):
    """
    calculate_discount calculates the final price after applying a discount.
    the function the original price (price) and the discount percentage (discount_percentage).
    as parameters. 
    if discount is 20% or higher, apply the discount.
    otherwise, return the original price.
    """
    if discount_percentage >= 20:
        discount_amount = price * (discount_percentage / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
price = input("Enter the price: ")
discount_percentage = input("Enter the discount percentage: ")

print (f"final price:, {calculate_discount(float(price), float(discount_percentage))}")






