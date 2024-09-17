user_month = int(input('Enter a month between 1 and 12: '))


if user_month < 1 or user_month > 12:
    print('Error. Month must be in between 1 and 12.' +
          ' Rerun Program and try again.')

else:
    if user_month >= 1 and user_month <= 3:
        print("The month is in the First Quarter")
    elif user_month >= 4 and user_month <= 6:
        print("The month is in the Second Quarter")
    elif user_month >= 7 and user_month <= 9:
        print("The month is in the Third Quarter")
    elif user_month >= 10 and user_month <= 12:
        print("The month is in the Fourth Quarter")
        