from bs4 import BeautifulSoup
import requests
#import urllib2

redditFile = "http://www.reddit.com"
redditHtml = requests.get(redditFile)


soup = BeautifulSoup(redditHtml)
redditAll = soup.find_all("a")
for links in soup.find_all('a'):
    print (links.get('href'))