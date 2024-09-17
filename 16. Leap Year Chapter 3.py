def leapyear():
    i = int(input("Do you want to a game? \n (0=Yes, 1=No)"))
    
    #redundancy to avoid having incorrect choice as input; input validation
    while i!=0 and i!=1:
        i = int(input("Do you want to a game? \n (0=Yes, 1=No)"))
    
    while i!=1:
        print("Type in a year and the program will determine")
        year = int(input("If the year is a leap year:"))
        
        if (year % 400 == 0) or (year % 4 ==0 and year % 100 !=0):
            print("In",year,", February has 29 days.")
            print("You won the game ")
        else:
            print("In",year,", February does not have 29 days.")
        i = int(input("Again? (0=Yes, 1=No)"))
leapyear()
    