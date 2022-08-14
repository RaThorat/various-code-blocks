# method 1 beautifulsoup to extract information from a website
import requests
from bs4 import BeautifulSoup

url = 'your-link'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)

output = ''
blacklist = [
    '[document]',
    'noscript',
    'header',
    'html',
    'meta',
    'head', 
    'input',
    'script',
    # there may be more elements you don't want, such as "style", etc.
]

for t in text:
    if t.parent.name not in blacklist:
        output += '{} '.format(t)

print(output)

# method 2 extract tables from wikipedia
from pandas.io.html import read_html
page = 'https://en.wikipedia.org/wiki/List_of_Asian_countries_by_area'

wikitables = read_html(page,  attrs={"class":"wikitable"})

print ("Extracted {num} wikitables".format(num=len(wikitables)))

