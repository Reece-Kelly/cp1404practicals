"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(user_result)
    random_score = random.randint(0, 100)
    random_score_result = determine_result(random_score)
    print(f"Random score result: {random_score_result}")


def determine_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score < 50:
        result = "Bad"
    elif score < 90:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
