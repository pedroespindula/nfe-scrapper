from bs4 import BeautifulSoup as bs

import csv

def get_header(soup):
    HEADER_QUERY = 'tr:nth-of-type(2) > .tdCabecalho'

    return [c.text.strip() for c in soup.select(HEADER_QUERY)]

def get_values(soup):
    VALUES_QUERY = 'div#prod > table > tbody > tr > .tdPadrao > input'

    return [i['value'].strip() for i in soup.select(VALUES_QUERY)]

def get_soup(file_path):
    with open(file_path, 'r+') as f:
        return bs(f, 'html.parser')

def main():
    soup = get_soup('../data/in.html')

    with open('../out/data.csv', 'w+') as f:
        header = get_header(soup)
        values = get_values(soup)

        wr = csv.writer(f, quoting=csv.QUOTE_ALL)

        wr.writerow(header)

        for c in range(0, len(values), 5):
            wr.writerow(values[c: c + 5])


if __name__ == "__main__":
    main()
