from bs4 import BeautifulSoup
import requests, pprint
import csv

source = requests.get('https://www.offmenupodcast.co.uk/restaurants').text
soup = BeautifulSoup(source, 'lxml')

csv_file = open('Off Menu.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['URL', 'Name', 'Attended', 'Score'])

for main in soup.find('ul'):
    link = main.find('a')
    url = link.get('href')
    pprint.pprint(url)

    restaurants = main.p.text
    pprint.pprint(restaurants)

    csv_writer.writerow([url, restaurants])

csv_file.close()
