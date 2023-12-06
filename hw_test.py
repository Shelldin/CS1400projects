longest_key = ""
longest_value = ""

test_dict = {"string key": "string value",
             "string key 1": "string value 1", "string key 2": "string value 2", "key 3": "value 3"}

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
