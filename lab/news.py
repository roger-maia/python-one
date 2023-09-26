import requests
from bs4 import BeautifulSoup

try :
    url = "https://news.ycombinator.cdom/"
    response = requests.get(url)
except NameError:
    print('A requisição falou.' + NameError)    

soup = BeautifulSoup(response.text, "html.parser")
headings = soup.select(".titleline a")

for heading in headings:
    print(heading.text)    
    
    
    

