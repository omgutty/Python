"""
# ✅ Grade Calculator:

# Write a program that calculates and displays the letter grade

# for a given numerical score (e.g., A, B, C, D, or F)

# based on the following grading scale

# A: 90-100

# B: 80-89

# C: 70-79

# D: 60-69

# F: 0-59


# 1 -> User Inputs - score -> int

# 2 ->  O/p -> str -> A, B
"""
# This program is a GRADE CALCULATOR: it turns a score (0-100)
# into a letter grade (A, B, C, D or F) using if/else.

score= int(input("Enter your score : "))

if score>=90 and score<=100:     # A: score between 90 and 100
    print("Grade: A")
else:
    if score>=80 and score <=89: # B: score between 80 and 89
        print("Grade: B")
    else:
        if score>=70 and score<=79:  # C: score between 70 and 79
            print("Grade: C")
        else:
            if score>=60 and score<=69:  # D: score between 60 and 69
                print("Grade: D")
            else:
                if score>=0 and score<=59:  # F: score between 0 and 59
                    print("Grade: F")
                else:
                    if score<0 and score >=100:  # never True (impossible)
                        print("Enter valid score range from 0-100 ")

#solution 2:
# Same logic, but using elif - much easier to read than nested if/else.

score2= int(input("enter your score: "))

if score2 >= 90 and score2 <= 100:
    print("Grade: A")
elif score2 >= 80:
     print("Grade: B")
elif score2 >= 70:
    print("Grade: C")
elif score2 >= 60:
    print("Grade: D")
elif score2 >= 0:
    print("Grade: F")
else:
    print("Enter a valid score (0-100)")
