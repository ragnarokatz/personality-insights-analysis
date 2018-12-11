"""
personality insights analysis demo.
"""
from os.path import join, dirname
import json
import csv

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


def driver(file_name):
    service = init_service()
    input_data = extract(file_name)
    output_data = service.profile(input_data, content_type='text/plain', raw_scores=True).get_result()
    json.dumps(output_data, indent=2)


def main():
    parser = argparse.ArgumentParser(description="driver")
    parser.add_argument("--file_name", default="sample.txt")
    parsed_args = vars(parser.parse_args(sys.argv[1:]))
    driver(**parsed_args)


if __name__ == '__main__':
    main()
