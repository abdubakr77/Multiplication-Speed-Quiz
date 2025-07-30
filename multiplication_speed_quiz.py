import time
import random

num_of_questions = 5

user_points = 0

review = []

all_time_score = 0

while num_of_questions > 0:



    
    digit1 = random.randint(0,12)
    digit2 = random.randint(0,12)

    question = f"{digit1} * {digit2}"
    question_result = digit1 * digit2

    start = time.time()

    user_result = int(input(f"{question} = "))

    end = time.time()
    
    all_time_score += (end - start)

    if user_result == question_result and (end - start) <= 5:
        user_points += 2
        review.append(f"{question} = {user_result} ✅")
        print("WOW, You Collect 2 Points!")

    elif user_result == question_result:
        user_points += 1
        review.append(f"{question} = {user_result} ✅")
        print("Good, You Collect 1 Point!")
        
    else:
        review.append(f"{question} = {user_result} ❌")
        print("Wrong Answer!")
        
    num_of_questions -= 1
    

print("Your Points: "+str(user_points))

for r in review:
    print(r)

print("Your All Time Score: "+str(all_time_score),"Seconds")
    
        






