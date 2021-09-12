import requests
from bs4 import BeautifulSoup
 

URL='https://www.amazon.ca/gp/product/B086XCGMN7/ref=ewc_pr_img_3?smid=A3DWYIK6Y9EEQB&psc=1'

headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content,'lxml')



title = soup.find(id="productTitle")

print(title)