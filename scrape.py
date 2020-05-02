#Provide a list of articles that has at least 100 votes/points from the Hacker News website

import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')

#modifies the data from the website into HTML
soup = BeautifulSoup(res.text, 'html.parser')

#grabs a link that has a class of "storylink"
links = (soup.select('.storylink'))

#grabs the votes for each news/articles
subtext = soup.select('.subtext')

def sort_stories_by_votes(hnlist):
    # sorts the list by votes
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                # creates a dictionary with a title, link, and votes
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))