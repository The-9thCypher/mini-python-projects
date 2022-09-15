import requests
from bs4 import BeautifulSoup as bs

class Error (TypeError):
    pass

class NameNotFound (Error):
    pass

try:
   github_user = input('INPUT GITHUB USER: ')

   url  = 'https://github.com/'+github_user

   r = requests.get(url)

   soup = bs(r.content, 'html.parser')

   profile_image = soup.find('img', {'alt': 'Avatar'})['src']

   print(profile_image)
except NameNotFound:
    print("no github user found")
finally:
    print("Arigatéaux!")