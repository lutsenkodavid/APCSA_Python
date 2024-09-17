test1 = int(input('Enter the score of your first test out of 25 points: '))
test2 = int(input("Enter the score of your second test out of 25 points: "))
main = int(input("Enter the score of your Main Exam out of 50 points: "))
total = test1 + test2 + main
main
if test1 < 0 or test1 > 25 or test2 < 0 or test2 > 25 or main <0 or main > 50:
    print('Error. The points must be in between 0 and 25.' +
          ' Rerun Program and try again.')
    
elif main < 25 or total < 50:
    print("Better luck next time, you are a disapointment. Fail!")
elif total >= 80:
    print("Distinction. Good Job! Your parents won't beat you!")
elif total >=60 and total < 80:
    print("Credit. Be better")
elif total <= 59 and total >= 50:
    print("Pass. Your parents probobaly regret having you.")
    