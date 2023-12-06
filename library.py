import os.path
import sys
import argparse


def file_text_to_list(file):
    # Open file of book file and load into a list
    if os.path.isfile(file) is True:
        text_data_list = []
        text_data = open(file, "r", encoding="utf-8")
        for line in text_data:
            text_data_list.append(line.rstrip())
    else:
        print("The input file %s does not exist!", file)
        sys.exit(1)

    return text_data_list


def get_three_letter_code(file):
    # get three-letter code based on file name
    three_letter_code = os.path.split(file)

    return three_letter_code


def convert_to_dictionary(text_list):
    # separate the delimited items and put them into a list of tuples
    delimiter = "|"

    tuples_list = []

    for text in text_list:
        line_text = text.split(delimiter)[0]
        line_number = int(text.split(delimiter)[1])

        tuples_list.append((line_number, line_text))

    unsorted_dict = dict(tuples_list)

    return unsorted_dict


def sort_dictionary(unsorted_dict):
    # take dictionary and sort it
    sorted_list = sorted(unsorted_dict.items())

    sorted_dict = dict(sorted_list)

    return sorted_dict


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


def get_average_length(sorted_dict):
    # get the length of each line and average them
    total_length = 0
    number_of_lines = 0

    for number, text in sorted_dict.items():
        total_length += len(text)
        number_of_lines += 1

    average_length = round(total_length / number_of_lines)

    return average_length


def write_output_file(file, sorted_dict):
    # write a new file with required info and sorted lines
    three_letter_code = get_three_letter_code(file)

    output_file = open(f"{three_letter_code}_book.txt", "w")

    output_file.write(f"{three_letter_code}\n")
    output_file.write(f"Longest line ({get_longest_line(sorted_dict)[0]}): {get_longest_line(sorted_dict)[1]}\n")
    output_file.write(f"Average length: {get_average_length(sorted_dict)}\n")
    for number, text in sorted_dict.items():
        output_file.write(f"{text}\n")


def main():
    parser = argparse.ArgumentParser(
        description="Open scrambled book file")

    parser.add_argument('--file', type=str, required=True,
                        help="Please provide a file name on the command line")

    args = parser.parse_args()

    initial_book_file = args.file

    text_list = file_text_to_list(initial_book_file)
    unsorted_dict = convert_to_dictionary(text_list)
    sorted_dict = sort_dictionary(unsorted_dict)
    write_output_file(initial_book_file, sorted_dict)


# Execute main program
if __name__ == "__main__":
    main()
