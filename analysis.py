"""
personality insights analysis demo.
"""
from os.path import join, dirname
import json
import sys
import argparse

from watson_developer_cloud import PersonalityInsightsV3


def init_service():
    """
    IBM cloud personality insights service instance provides API key authentication.
    """
    service = PersonalityInsightsV3(
        version='2017-10-13',
        # url is optional, and defaults to the URL below. Use the correct URL for your region.
        url='https://gateway.watsonplatform.net/personality-insights/api',
        iam_apikey=None)
    return service


def extract(file_name):
    with open(join(dirname(__file__), file_name)) as file:
        if file_name.endswith('.txt'):
            return file.read()

        if file_name.endswith('.json'):
            return json.load(file)

        raise NotImplementedError(f'Unsupported format, file name is {file_name}')


def write(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def driver(input_file_name, output_file_name):
    service = init_service()
    input_data = extract(input_file_name)
    output_data = service.profile(input_data, content_type='text/plain', raw_scores=True).get_result()
    write(output_data, output_file_name)


def main():
    parser = argparse.ArgumentParser(description="driver")
    parser.add_argument("--input_file_name", default="sample.txt")
    parser.add_argument("--output_file_name", default="output.txt")
    parsed_args = vars(parser.parse_args(sys.argv[1:]))
    driver(**parsed_args)


if __name__ == '__main__':
    main()
