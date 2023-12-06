longest_key = ""
longest_value = ""

test_dict = {3: "string value", 5: "string value 1", 4: "string value 2", 1: "value 3", 2: "ranasdasdasdasdasddom stuff"}

for key, value in test_dict.items():
    if len(value) >= len(longest_value):
        longest_key = key
        longest_value = value

print(longest_key, longest_value)

for key, value in test_dict.items():
    print(value)


def get_average_length(sorted_dict):
    # get the length of each line and average them
    total_length = 0
    number_of_lines = 0

    for number, text in sorted_dict.items():
        total_length += len(text)
        number_of_lines += 1

    average_length = round(total_length / number_of_lines)

    return average_length


print(f"average length: {get_average_length(test_dict)}")

test_output = open("test_output.txt", "w")
test_output.write("writing some stuff 1\n")
test_output.write("writing some stuff 2\n")


def get_longest_line(sorted_dict):
    # find the longest line and its line number
    longest_line = ""
    longest_line_number = 0

    for number, text in sorted_dict.items():
        if len(text) >= len(longest_line):
            longest_line = text
            longest_line_number = number

    longest_line_and_number = (longest_line_number, longest_line)

    return longest_line_and_number


test_output.write(f"Longest line ({get_longest_line(test_dict)[0]}): {get_longest_line(test_dict)[1]}\n")
test_output.write(f"Longest line ({get_longest_line(test_dict)[0]}): {get_longest_line(test_dict)[1]}\n")
for number, text in test_dict.items():
    test_output.write(f"{text}\n")


def sort_dictionary(unsorted_dict):
    # take dictionary and sort it
    sorted_list = sorted(unsorted_dict.items())

    sorted_dict = dict(sorted_list)

    return sorted_dict

print(sort_dictionary(test_dict))
