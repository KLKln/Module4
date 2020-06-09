def calculate_price(price, cash_coupon, percent_coupon):
    price = input("Please enter the cost of purchase: ")
    cash_coupon = input("Please enter the cash coupon amount: ")
    percent_coupon = input("Please enter the percent off coupon: ")
    percent_off_calc = price - (1-percent_coupon * price)
    sales_tax = .06
    sales_tax_total =


    if price < 10:
        shipping = 5.95

    total = ((price - cash_coupon) - percent_off_calc) + shipping + 
    return


if __name__ == '__main__':

    calculate_price()
