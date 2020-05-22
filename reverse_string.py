input_string = "I have come to 91 springboard for an interview today"
output_string = ''
for i in range(len(input_string)-1,-1,-1):
    output_string = output_string + input_string[i]

print(output_string)

#using extended slicing
print(input_string[:: -1])

#reversing words:
def revwordsSent(input_string):
    return " ".join(word[::-1] for word in input_string.split(" "))

print('Reversing words only: ' + revwordsSent(input_string))

#reversing the sentence:
def revwordsSent(input_string):
    return " ".join(word[:: -1] for word in input_string[::-1].split(" "))

print('Reversing Sentence only: ' + revwordsSent(input_string))
