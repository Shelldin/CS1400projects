import os.path
import sys
import argparse


def file_text_to_list(file):
    # Open file of female names  and load into a list
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


def convert_to_list_of_tuples(text_list):
    # separate the delimited items and put them into a list of tuples
    delimiter = "|"

    tuples_list = []
