# enter price, cash coupon, and percent off coupon, return total
# price, cash_coupon, percent_coupon
def calculate_price(price, cash_coupon, percent_coupon):
    price = float(input("Please enter the cost of purchase: "))
    cash_coupon = float(input("Please enter the cash coupon amount: "))
    price_minus_cash_coupon = (price - cash_coupon)
    percent_coupon = input("Please enter the percent off coupon: ")
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

"""
    if pre_total >= 50:
        shipping = 0.00
        return shipping
    if pre_total >= 30:
        if pre_total < 50:
            shipping = 11.95
            return shipping
        if pre_total >= 10:
            if pre_total < 30:
                shipping = 7.95
                return shipping
            if pre_total < 10:
                shipping = 5.95
                return shipping
"""

# calculate sales tax
def sales_tax(pre_total, shipping):
    price_with_tax = pre_total + shipping + ((pre_total + shipping) * 1.06)

    return price_with_tax


def main():
    print('This will calculate price, discounts tax and shipping for your purchase')
    tax = .06
    subtotal = calculate_price()
    shipping = calculate_shipping(subtotal)

    print('subtotal: ', '${:,.2f}'.format(subtotal))
    print('shipping: ', '${:,.2f}'.format(shipping))
    print('tax: ', '${:,.2f}'.format(((subtotal + shipping) * tax)))
    print('total: ', '${:,.2f}'.format(subtotal + shipping + ((subtotal + shipping) * tax)))


if __name__ == '__main__':
    main()

# '${:,.2f}'.format(subtotal + shipping + ((subtotal + shipping) * tax)))
