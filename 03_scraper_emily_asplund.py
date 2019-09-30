import requests as r
import re

url = 'https://www.crazyforcrust.com/best-chocolate-chip-cookie-recipe/'
h = {'user-agent': 'Emily Asplund (asplund.emily@gmail.com)' }
page = (r.get(url, headers = h))
f = open('WebPage1.html', 'w+')
f.write(page.text)
f.close()

parser = __import__('03_parser_emilyasplund')
