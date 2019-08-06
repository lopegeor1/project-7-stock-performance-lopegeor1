"""
Contains pytest configuration & fixtures.
"""
import pytest


@pytest.fixture
def portfolio_csv(tmp_path):
    """
    Creates a portfolio.csv in a temporary folder for the
    purposes of testing.
    """
    lines = [
        ('symbol,units,cost\r\n'),
        ('APPL,100,154.23\r\n'),
        ('AMZN,600,1223.43\r\n'),
    ]

    filename = tmp_path / 'portfolio.csv'
    with open(filename, 'w', newline='') as file:
        file.writelines(lines)

    return filename

@pytest.fixture
def write_csv(tmp_path):
    """
    Creates a report1.csv in a temporary folder for the
    purposes of testing.
    """
    lines = [
        ('NFLX,3,99.66,319,998.1,957,-41.1,-0.041\r\n'),
        ('XRX,40,33.94,30,1357.6,1200,-157.6,-0.116\r\n'),
    ]

    filename = tmp_path / 'report1.csv'
    with open(filename, 'w', newline='') as file:
        file.writelines(lines)

    return filename
