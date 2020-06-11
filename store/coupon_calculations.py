"""
Program: coupon_calculations.py
Author: Kelly Klein
Last date modified: 6/10/2020
This program will take user input for price, a cash coupon, and a percent coupon
    and output those totals plus tax, shipping and a grand total
"""

# enter price, cash coupon, and percent off coupon, return total
# price, cash_coupon, percent_coupon


def calculate_price(price, cash_coupon, percent_coupon):
    price_minus_cash_coupon = (price - cash_coupon)
    percent_coupon = float(int(percent_coupon) / 100)
    percent_off_calc = price_minus_cash_coupon - ((1 - percent_coupon) * (price_minus_cash_coupon))
    pre_total = price_minus_cash_coupon - percent_off_calc

    return pre_total


# calculate shipping, this will be the nested if's
def calculate_shipping(pre_total):
    if pre_total < 10:
        shipping = 5.95
        return shipping
    elif 10 <= pre_total < 30:
        shipping = 7.95
        return shipping
    elif 30 <= pre_total < 50:
        shipping = 11.95
        return shipping
    elif pre_total >= 50:
        shipping = 0.0
        return shipping


if __name__ == '__main__':
    tax = .06
    price = float(input("Please enter the cost of purchase: "))
    cash_coupon = float(input("Please enter the cash coupon amount: "))
    percent_coupon = input("Please enter the percent off coupon: ")
    pre_total = calculate_price(price, cash_coupon, percent_coupon)
    shipping = calculate_shipping(pre_total)
    print('subtotal: ', '${:,.2f}'.format(pre_total))
    print('shipping: ', '${:,.2f}'.format(shipping))
    print('tax: ', '${:,.2f}'.format(((pre_total + shipping) * tax)))
    print('total: ', '${:,.2f}'.format(pre_total + shipping + ((pre_total + shipping) * tax)))

