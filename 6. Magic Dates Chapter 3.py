month = int(input('Enter a month in numberic form: '))
date = int(input('Enter a day of the month: '))
year = int(input('Enter the year in two digits: '))

random = f"{month}/{date}/{year}"
if month * date == year:
    print('The date,',random, ',is magic.')
else:
    print('The date,',random, ', is not magic.')
