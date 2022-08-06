import requests
from bs4 import BeautifulSoup
url = 'https://www.bis.gov.in/index.php/product-certification/products-under-compulsory-certification/scheme-i-mark-scheme/'

r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')
h = s.find_all('strong')

K=[]
for i in h:
 K.append(i.text)
m=[]
for j in K:
 if j==K[0]:
  continue
 else:
  m.append(j)

m.remove(m[4])

p=1
for k in m[0:39]:
 print(p,  k)
 p=p+1

