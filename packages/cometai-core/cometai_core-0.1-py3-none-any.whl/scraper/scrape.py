from bs4 import BeautifulSoup


if __name__ == "__main__":
    html = ''
    with open('search.html', 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')

    divs = soup.find_all('div', attrs={'data-scroll-into-view': True})

    # List to hold the extracted URNs
    urns = []

    for div in divs:
        # Extract the value of 'data-scroll-into-view'
        urn = div['data-scroll-into-view']
        # Assuming the format always includes the URN inside parentheses
        urn = urn.split('(')[1].rstrip(')')
        urns.append(urn)

    # Output the list of URNs
    for urn in urns:
        print(urn)