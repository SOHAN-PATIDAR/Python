import requests
from bs4 import BeautifulSoup
import re


def strip_tags(url):

    r = requests.get(url)    #  fetching the html content of the url
    html_content = r.content


    soup = BeautifulSoup(html_content,features='html.parser')
    
    st = soup.decode()     #conerting beautiful soup object into string

    res = re.compile(r'<[^>]+>+').sub('', st)
    print(res)

strip_tags("https://www.codewithharry.com/")