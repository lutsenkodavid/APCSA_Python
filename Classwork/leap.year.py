def leapyear():
    i = int(input("Do you want to a game? \n (0=Yes, 1=No)"))
    
    #redundancy to avoid having incorrect choice as input; input validation
    while i!=0 and i!=1:
        i = int(input("Do you want to a game? \n (0=Yes, 1=No)"))
    
    while i!=1:
        print("Type in a year and the program will determine")
        year = int(input("If the year is a leap year:"))
        
        if (year % 400 == 0) or (year % 4 ==0 and year % 100 !=0):
            print("Leap year")
            print("You won the ")
        else:
            print("Not a leap year")
        i = int(input("Again? (0=Yes, 1=No)"))
leapyear()
    
    
        
