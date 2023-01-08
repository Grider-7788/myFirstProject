import requests
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/List_of_highest-paid_film_actors"
url_txt = requests.get(url).text
s = BeautifulSoup(url_txt, "html.parser")

my_table = s.find('table', class_='wikitable sortable plainrowheaders')
table_links = my_table.find
print(table_links)