print("                 Hello in 'HAZEM PROGRAM'                ")
while True:
 year = int(input("please enter your birth year:\n" ))
 answer = input("are you need your age by year or month or week or day or hour?\n")

 years = 2023-year
 if answer == "year":
    print(f'you have {years} years.')
 elif answer == "month":
    print(f"you have {years*12} months.")
 elif answer == "week":
    print(f"you have {years*12*4} weeks.")
 elif answer == "day":
    print(f"you have {years*12*4*7} days.")
 elif answer == "hour":
    print(f"you have {years*12*4*7*24} hours.")
 else:
    print("you have an error, please enter a correct answer.")
 choice = input("do you want to continue in hazem progrm (yes or no):\n").strip().lower()
 if choice == "no":
    break
print("program is exited")