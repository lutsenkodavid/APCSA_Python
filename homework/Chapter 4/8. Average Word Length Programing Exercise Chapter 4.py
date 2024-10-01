word = 0
total_length = 0
number_of_word = 0

while word != '':
    word = input("Enter the word: ")
    number_of_word += 1
    for characters in (word):
        total_length += 1
    average_length = total_length / number_of_word
    
    print("The average length of the entered word is: ",average_length)