import requests
from bs4 import BeautifulSoup
# Make a request to https://www.teamonepanama.com

page = requests.get("https://www.teamonepanama.com")
soup = BeautifulSoup(page.content, 'html.parser')
# Extract title of page
page_title = soup.title.text
page_body = soup.body.text
page_head = soup.head.text
# print the result
print('Este es el titulo')
print(page_title)
print('Este es el body')
print(page_body)
print('Este es el head')
print(page_head)

#A list for h1

all_h1_tags = []
# Set all_h1_tags to all h1 tags of the soup
for n in soup.select('p'):
    all_h1_tags.append(n.text)
# Create seventh_p_text and set it to 7th p element text of the page
seventh_p_text = soup.select('p')[6].text

print(all_h1_tags,seventh_p_text)