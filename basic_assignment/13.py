input_data = raw_input(">")

letter = []
digit = []

for x in input_data:
    if str(x).isalpha():
        letter.append(str(x))
    elif str(x).isdigit():
        digit.append(int(x))

print("Digit: " + str(len(digit)))
print("Letter: " + str(len(letter)))
