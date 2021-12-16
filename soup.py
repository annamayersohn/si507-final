from bs4 import BeautifulSoup
import requests
import json

base_url = 'https://www.behindthename.com'
path = '/name/anna/tree'

full_url = base_url + path

response = requests.get(full_url)
anna_soup = BeautifulSoup(response.text, 'html.parser')

tree_links = anna_soup.find_all('a', class_='nlc')
ratings = {}
for tree_link in tree_links:
    href = tree_link['href']
    if href.split('/')[1] == 'name':
        name_url = base_url + href
        response = requests.get(name_url)
        soup = BeautifulSoup(response.text, 'html.parser')
        rating_div = soup.find(class_='ratenumber')
        if rating_div:
            rating = rating_div.text.split('%')[0]
            ratings[href] = int(rating)
        else:
            ratings[href] = None
    else:
        pass

with open('anna_ratings.json', 'w') as filepath:
    json.dump(ratings, filepath)

with open('anna_soup.html', 'w') as filepath:
    filepath.write(str(anna_soup))