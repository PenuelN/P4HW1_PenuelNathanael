# Nathanael Penuel
# Date: 11/10/2024
# Assignment: P4HW1
# This program assigns grades

# Pseudocode:
# 1. Prompt the user for the number of scores they want to enter.
# 2. Initialize an empty list to store the valid scores.
# 3. Use a loop to collect the number of scores specified by the user.
#    - For each score entry:
#        a. Prompt the user to enter a score.
#        b. Check if the score is between 0 and 100.
#        c. If the score is invalid, display an error message and prompt the user again until a valid score is entered.
#        d. If the score is valid, add it to the list.
# 4. Once all scores are collected, find the lowest score and remove it from the list.
# 5. Calculate the average of the modified list (after removing the lowest score).
# 6. Determine the letter grade based on the average score.
# 7. Display the results:
#    - Lowest score
#    - Modified score list (after dropping the lowest score)
#    - Average of modified list
#    - Letter grade

# Get the number of scores
num_scores = int(input("How many scores do you want to enter? "))

# Initialize an empty list for storing
scores = []

# Loop to collect scores
for i in range(num_scores):
    # Prompt the user for a score
    score = float(input(f"Enter score #{i + 1}: "))
    
    # Check if the score is within the valid range
    while score < 0 or score > 100:
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{i + 1} again: "))

    # Add the valid score
    scores.append(score)

# Find the lowest score
lowest_score = scores[0]
for s in scores:
    if s < lowest_score:
        lowest_score = s

# Remove the lowest score 
scores.remove(lowest_score)

# Calculate the average
total = 0
for s in scores:
    total += s
average_score = total / len(scores)

# Determine the grade
if average_score >= 90:
    grade = "A"
elif average_score >= 80:
    grade = "B"
elif average_score >= 70:
    grade = "C"
elif average_score >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n------------Results------------")
print(f"Lowest Score   : {lowest_score}")
print(f"Modified List  : {scores}")
print(f"Scores Average : {average_score:.2f}")
print(f"Grade          : {grade}")
print("-------------------------------")
