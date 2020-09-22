from bs4 import BeautifulSoup as soup
import requests
import re 


def getQuote():

    page = requests.get("https://everydaypower.com/uncle-iroh-quotes/")
    Soup = soup(page.content,'html.parser')

    for i in range(6,57):
        if i == 29:
            continue
        else:
        
            quote = Soup.find_all('p')[i].get_text()

            print(quote)
if __name__ == "__main__":

    getQuote()