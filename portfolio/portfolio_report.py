"""
Generates performance reports for your stock portfolio.
"""
import csv
import argparse
import requests


def main():
    """
    Entrypoint into program.
    """
    args = get_args()
    source = args.source
    filename = '{0}/report1.csv'.format(args.filename)
    csv_source = read_portfolio(source)
    csv_target = save_portfolio(csv_source, filename)
    make_api_call(csv_target)


def get_args():
    """use argparse to get args directly from the command line"""
    parser = argparse.ArgumentParser()
    parser.add_argument('source', help="enter source file, i.e. portfolio.csv")
    parser.add_argument('filename', help="enter target file path in quotations")
    return parser.parse_args()


def read_portfolio(source):
    """Returns data from a CSV file"""
    with open(source, newline='') as myfile:
        csv_reader = csv.DictReader(myfile)
        csv_source = []
        for row in csv_reader:
            symbol = row['symbol']
            units = (row['units'])
            cost = (row['cost'])
            list_a = {'symbol': symbol, 'units': units, 'cost': cost}
            csv_source.append(list_a)

    return csv_source


def save_portfolio(csv_source, filename):
    """Saves data to a CSV file"""
    csv_target = csv_source
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, ['symbol', 'units', 'cost'])
        writer.writeheader()
        writer.writerows(csv_source)
    return csv_target


def make_api_call(csv_target):
    """Make http request to IEX Trading API and return useful dataset"""
    my_string = ','.join(str(row['symbol']) for row in csv_target)
    url = "https://api.iextrading.com/1.0/tops/last?symbols={0}".format(my_string)
    response = requests.get(url)
    data = response.json()
    api_data = [
        (item['symbol'], item['price'], item['size'], item['time'])
        for item in data
    ]
    return api_data

if __name__ == '__main__':
    main()
