#enter price, cash coupon, and percent off coupon, return total
def calculate_price(price, cash_coupon, percent_coupon):
    price = input("Please enter the cost of purchase: ")
    price = float(price)
    cash_coupon = input("Please enter the cash coupon amount: ")
    cash_coupon = float(cash_coupon)
    percent_coupon = input("Please enter the percent off coupon: ")
    percent_coupon = float(percent_coupon / 100)
    percent_off_calc = (price - cash_coupon) - ((1 - percent_coupon) * price)
    pre_total = price - cash_coupon - percent_off_calc

    return pre_total


#calculate shipping, this will be the nested if's
def calculate_shipping(pre_total):
    if pre_total < 10:
        shipping = 5.95
        return shipping


#calculate sales tax
def sales_tax(pre_total, shipping):
    price_with_tax = pre_total + shipping + ((pre_total + shipping) * 1.06)

    return price_with_tax


#display all the totals
def display_totals(pre_total, shipping, price_with_tax):
    print("Original Price: ", pre_total)
    print("Shipping: ", shipping)
    print("Sales tax: ", (pre_total + shipping) * .06)
    print ("Total Price: ", pre_total + shipping + price_with_tax)


if __name__ == '__main__':

    calculate_price()
    display_totals()
