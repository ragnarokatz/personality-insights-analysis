"""
extract bodies of texts from outlook email extracts.
"""
import json
import sys
import argparse

import pandas as pd


def write(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def driver(input_file_name, output_file_name):
    df = pd.read_csv(input_file_name, encoding='ansi')
    texts = df["Body"].fillna("").tolist()
    write(texts, output_file_name)


def main():
    parser = argparse.ArgumentParser(description="driver")
    parser.add_argument("--input_file_name", default="sent.csv")
    parser.add_argument("--output_file_name", default="sample.json")
    parsed_args = vars(parser.parse_args(sys.argv[1:]))
    driver(**parsed_args)


if __name__ == '__main__':
    main()
