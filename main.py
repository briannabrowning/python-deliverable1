print("Welcome to GC mini golf! What is your name? ")
my_name = input("")
print("Hi " + my_name + "!")
print("Would you like to play 3 or 6 holes? ")
num_holes = int(input())
total_score = 0
par = 3 * num_holes
if num_holes == 3:
    for hole in range(1, num_holes + 1):
        print(f"How many putts for hole {hole}? (par:3). ")
        putts = int(input())
        total_score += putts
if num_holes == 6:
    for hole in range(1, num_holes + 1):
        print(f"How many putts for hole {hole}? (par:3). ")
        putts = int(input())
        total_score += putts

score_difference = total_score - par

if score_difference == 0:
    print(f"Good game, {my_name}. Your total score was: 0.")
elif score_difference <= 0:
    print(f"Great job, {my_name}! Your total score was: {score_difference}")
elif score_difference >= 0:
    print(f"Nice try, {my_name}. Your total score was: {score_difference}")
