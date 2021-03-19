numbers_dictionary = {}


while True:
    number_as_string = input()
    if number_as_string == "Search":
        break
    try:
        number = int(input())
        numbers_dictionary[number_as_string] = number
    except ValueError:
        print("The variable number must be an integer")


try:
    while True:
        searched = input()
        if searched == "Remove":
            break

        print(numbers_dictionary[searched])

    while True:
        searched = input()
        if searched == "End":
            break

        del numbers_dictionary[searched]

except KeyError:
    print("Number does not exist in dictionary")

print(numbers_dictionary)
