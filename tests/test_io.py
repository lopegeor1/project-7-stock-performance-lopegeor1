"""
Tests I/O disk operations.
"""
from collections import OrderedDict


from portfolio import portfolio_report
from portfolio.portfolio_report import make_api_call


# Note: the portfolio_csv argument found in the tests below
#       is a pytest "fixture". It is defined in conftest.py

# DO NOT edit the provided tests. Make them pass.

def test_read_portfolio(portfolio_csv):
    """
    Given that the read_portfolio is called, assert that
    the data the expected data is returned.
    """
    expected = [
        OrderedDict([
            ('symbol', 'APPL'),
            ('units', '100'),
            ('cost', '154.23'),
        ]),
        OrderedDict([
            ('symbol', 'AMZN'),
            ('units', '600'),
            ('cost', '1223.43')
        ])
    ]

    assert portfolio_report.read_portfolio(portfolio_csv) == expected, (
        'Expecting to get the data stored in the portfolio_csv '
        'fixture as a Python data structure.'
    )


def test_save_portfolio(portfolio_csv):
    """
    Given that the save portfolio method is called with the following
    data, assert that a CSV file is written in the expected format.

    The portfolio
    """
    data = [{'symbol': 'MSFT', 'units': 10, 'cost': 99.66}]
    portfolio_report.save_portfolio(data, filename=portfolio_csv)

    expected = 'symbol,units,cost\r\nMSFT,10,99.66\r\n'
    with open(portfolio_csv, 'r', newline='') as file:
        result = file.read()
        assert result == expected, (
            f'Expecting the file to contain: \n{result}'
        )

# tests below have been added to test remaining methods of portfolio_report module
def test_make_api_call(requests_mock):
    """
    Given that the make_api_call method is called with the following
    data, assert that a dataset is created in the expected format.
    """
    url = (
        'https://api.iextrading.com/1.0/tops/last?symbols=ABEO,COKE,PEP'
    )

    requests_mock.get(
        url,
        json=[
            {'symbol': 'ABEO', 'price': 3, 'size': 100, 'time': 1564775999355},
            {'symbol': 'COKE', 'price': 292.72, 'size': 8, 'time': 1564775994014},
            {'symbol': 'PEP', 'price': 131.53, 'size': 100, 'time': 1564775998908}
            ]
    )

    expected = [
        ('ABEO', 3, 100, 1564775999355),
        ('COKE', 292.72, 8, 1564775994014),
        ('PEP', 131.53, 100, 1564775998908)
    ]

    my_stocks = [
                {'symbol': 'ABEO', 'units': '167', 'cost': '3'},
                {'symbol': 'COKE', 'units': '5', 'cost': '292.72'},
                {'symbol': 'PEP', 'units': '11', 'cost': '131.53'}
                ]
    assert make_api_call(my_stocks) == expected
