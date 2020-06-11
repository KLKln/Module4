"""
Program: average_scores.py
Author: Kelly Klein
Last date modified: 5/30/2020
This program will take user input and output a string
    including the inputs and the average of test scores
"""


def average():
    # get input for scores

    # declare variables, use score1, score2, score3 in calc
    score1 = int(score1_raw)
    score2 = int(score2_raw)
    score3 = int(score3_raw)

    average_scores = (score1 + score2 + score3) / 3

    return average_scores


if __name__ == '__main__':

    first_name = input("Enter students first name: ")
    last_name = input('Enter students last name: ')
    age = input('Enter students age: ')
    score1_raw = input('Enter first test score: ')
    score2_raw = input('Enter second test score: ')
    score3_raw = input('Enter third test score: ')
    print(last_name, ',', first_name, 'age:', age, '|', 'average grade: ', average())
