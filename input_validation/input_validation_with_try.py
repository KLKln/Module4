"""
Program: input_validation_with_try.py
Author: Kelly Klein
Last date modified: 6/11/2020
This program will take user input and output a string
    including the inputs and the average of test scores
    using a try/catch
"""


def average(score1, score2, score3):
    # get input for scores

    # declare variables, use score1, score2, score3 in calc
    try:
        average_scores = (score1 + score2 + score3) / 3
        if score1 < 0:
            raise ValueError('Please enter a positive number')
        elif score2 < 0:
            raise ValueError('Please enter a positive number')
            return average_scores

    except ValueError:
        raise ValueError

# average_scores = (score1 + score2 + score3) / 3


if __name__ == '__main__':
    first_name = input("Enter students first name: ")
    last_name = input('Enter students last name: ')
    age = input('Enter students age: ')
    test1 = input('Enter first test score: ')
    test2 = input('Enter second test score: ')
    test3 = input('Enter third test score: ')
    avg = average(int(test1), int(test2), int(test3))
    print(last_name, ',', first_name, 'age:', age, '|', 'average grade: ', avg)
