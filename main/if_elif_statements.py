"""
Program: if_elif_statments.py
Author: Kelly Klein
Last date modified: 6/9/2020
This program will test take user input for tier of subscription box
    and print the cost of the tier
"""
def signup_for_box():

    print("Choose your tier for Programmer's Toolkit Monthly Subscription Box.")

    print("You can choose one of the following: Platinum at $60, Gold at $50, Silver at $40, Bronze at $30 or free trial at $0")

    subscription_level = input("Enter the tier you'd like to subscribe to: ")
    return_string_cost_of_box(subscription_level)
    print(return_string_cost_of_box(subscription_level))

def return_string_cost_of_box(subscription_level):

    if subscription_level == "Platinum":
        return 60
    elif subscription_level == "Gold":
        return 50
    elif subscription_level == "Silver":
        return 40
    elif subscription_level == "Bronze":
        return 30
    elif subscription_level == "Free Trial":
        return 0

if __name__ == '__main__':
    signup_for_box()


