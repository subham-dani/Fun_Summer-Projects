import requests
from bs4 import BeautifulSoup

url = 'https://www.google.co.in/search?q=Madhubani+Painting+Drawing&sa=X&hl=en&biw=1536&bih=754&sxsrf=ALiCzsZ1alv5ZFNFkc_TqpkGVQumesXA:1651946526036&tbm=isch&source=iu&ictx=1&vet=1&fir=Vl7wO43u9KzeJM%252CTP9V-URbF6lL9M%252C_%253B1y-GMbJbpiVEYM%252Cd_mbQvDObpBz5M%252C_%253BuVI-XwEH6iVtLM%252CXbrEtWGlMUjI4M%252C_%253BFb7wAn7bhWsfDM%252CF9UU8XjkmSDj4M%252C_%253BrLBTRh-OqdVIrM%252CyeuSAFcLVfVYFM%252C_%253Bq2q5_uBpcDGDzM%252CBH4JMHVaXEolXM%252C_%253B6i0fgIejiGz7YM%252CQdJ5XIDHQB35VM%252C_%253Bh-c3olAQXc28mM%252Cde0YWxALVgYquM%252C_%253BjIH7ms4V0CpoJM%252CTZubz3N3abDNkM%252C_%253BEx8NHPYPxcosxM%252CiSLg9M0R1D1x-M%252C_%253BlVL1R5HdIJTQXM%252C7KS4AqAR0cYkcM%252C_%253B-yZDn8nZyNq4uM%252Co3wuTaHEq6aGUM%252C_%253Be-hGa3FJTgIDyM%252CEouKYHt9XDu-rM%252C_%253B-QyzUBVP13aJZM%252C7gvXM-UIcXSsRM%252C_%253BnWtW5A-4w-sG3M%252CamGyJg3NhCZQrM%252C_%253B543OcR7fCEs-aM%252CQIeE6vey2BbqyM%252C_%253BcpAF3U7HP04HxM%252CwP0d32f2OWuCvM%252C_%253B6883LEbb7ip1EM%252CP9NLefh3lI4ZUM%252C_%253B0lmqw5iZv-xe7M%252CiSLg9M0R1D1x-M%252C_&usg=AI4_-kT3P8-zjNkBl5p2odQPpWp6-AK2zA&ved=2ahUKEwjQ_Pyu_M33AhUb82EKHSiNA_oQ9QF6BAgtEAE'

r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')

h = s.find_all('img')
i = 483
for j in h[1:]:
    temp = requests.get(j['src'])
    f = open(f'img-{i}.png', 'wb')
    f.write(temp.content)
    f.close()
    i = i + 1


