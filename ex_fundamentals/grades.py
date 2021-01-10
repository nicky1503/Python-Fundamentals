grade_data = float(input())


def grading(grade):
    if 2 <= grade < 3:
        return 'Fail'
    elif 3 <= grade < 3.5:
        return 'Poor'
    elif 3.5 <= grade < 4.5:
        return 'Good'
    elif 4.5 <= grade < 5.5:
        return 'Very Good'
    elif 5.5 <= grade <= 6:
        return 'Excellent'


print(grading(grade_data))
