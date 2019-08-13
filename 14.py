input_data = raw_input(">")

upper_case_letters = []
lower_case_letter = []

for x in input_data:
    if str(x).isalpha() and str(x).isupper():
        upper_case_letters.append(str(x))
    elif str(x).isalpha() and str(x).islower():
        lower_case_letter.append(str(x))

print("Upper case: " + str(len(upper_case_letters)))
print("Lower case: " + str(len(lower_case_letter)))
