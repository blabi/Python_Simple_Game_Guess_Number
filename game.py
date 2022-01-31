import random

number_comp = random.randint(1, 100)
win = "You win!"
lose_tb = "It's to big!"
lose_ts = "It's to small!"

while win:
    try:
        number_user = int(input("Guess the number: "))
    except:
        print("It's not a number!")
        continue
    if number_user == number_comp:
        print(f"{win}")
        break
    elif number_user > number_comp:
        print(f"{lose_tb}")
    elif number_user < number_comp:
        print(f"{lose_ts}")
