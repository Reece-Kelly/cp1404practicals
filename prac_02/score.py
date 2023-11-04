"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

LOWER_SCORE_LIMIT = 0
UPPER_SCORE_LIMIT = 100
PASSING_SCORE_THRESHOLD = 50
EXCELLENT_SCORE_THRESHOLD = 90


def main():
    """Get user score and print result and get random score and print result."""
    user_score = float(input("Enter score: "))
    user_result = determine_result(user_score)
    print(user_result)
    random_score = random.randint(LOWER_SCORE_LIMIT, UPPER_SCORE_LIMIT)
    random_score_result = determine_result(random_score)
    print(f"Random score result: {random_score_result}")


def determine_result(score):
    """Determine result based off score."""
    if score < LOWER_SCORE_LIMIT or score > UPPER_SCORE_LIMIT:
        result = "Invalid score"
    elif score < PASSING_SCORE_THRESHOLD:
        result = "Bad"
    elif score < EXCELLENT_SCORE_THRESHOLD:
        result = "Passable"
    else:
        result = "Excellent"
    return result


main()
