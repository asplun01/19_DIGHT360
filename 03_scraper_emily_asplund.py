import requests as r
import re

url = 'https://www.crazyforcrust.com/best-chocolate-chip-cookie-recipe/'
h = {'user-agent': 'Emily Asplund (asplund.emily@gmail.com)' }
page = (r.get(url, headers = h))
f = open('WebPage1.html', 'w+')
f.write(page.text)
f.close()

f = open('WebPage1.html', 'r')
text = f.read()

ingredients = re.findall(r'<span class=\"wprm-recipe-ingredient-name\">(.*?)</span>', text, flags=re.S)
f = open('ingredients_parsed.txt', 'w+')
f.write(str(ingredients))
f.close()

with open('ingredients_parsed.txt', 'r') as f:
    print (f.read())

