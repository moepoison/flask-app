import requests
import csv


def get_data():
    url = 'http://www.nasdaq.com/quotes/nasdaq-100-stocks.aspx?render=download'
    r = requests.get(url)
    print r
    data = r.text
    results = {'children': []}
    for line in csv.DictReader(data.splitlines(), skipinitialspace=True):
        if float(line['Nasdaq100_points']) > .01:
            results['children'].append({
                'name': line['Name'],
                'symbol': line['Symbol'],
                'symbol': line['Symbol'],
                'price': line['lastsale'],
                'net_change': line['netchange'],
                'percent_change': line['pctchange'],
                'volume': line['share_volume'],
                'value': line['Nasdaq100_points']
            })
    return results