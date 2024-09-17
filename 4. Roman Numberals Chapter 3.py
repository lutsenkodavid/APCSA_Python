user_number = int(input('Enter a number in between 1 and 10: '))

if user_number < 1 or user_number > 12:
    print('Error. The number must be in between 1 and 12.' +
          ' Rerun Program and try again.')
message = ('The roman numeral number for')
    
if user_number == 1:
    print(message, user_number,'is I')
elif user_number == 2:
    print(message, user_number,'is II')
elif user_number == 3:
    print(message, user_number,'is III')
elif user_number == 4:
    print(message, user_number,'is IV')
elif user_number == 5:
    print(message, user_number,'is V')
elif user_number == 6:
    print(message, user_number,'is VI')
elif user_number == 7:
    print(message, user_number,'is VII')
elif user_number == 8:
    print(message, user_number,'is VIII')
elif user_number == 9:
    print(message, user_number,'is IX')
elif user_number == 10:
    print(message, user_number,'is X')

