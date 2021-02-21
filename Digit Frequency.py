#Digit Frequency

input_string = input()
frequency = []
#Checking for frequency of digits(0-9) in the given string
for i in range(10):
    frequency.append(input_string.count(str(i)))
#Printing the frequency
for i in range(10):
    print(frequency[i], end=' ')