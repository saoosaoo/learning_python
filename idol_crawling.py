import requests
from bs4 import BeautifulSoup
from google_images_download import google_images_download


res = requests.get('https://ko.wikipedia.org/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD%EC%9D%98_%EC%95%84%EC%9D%B4%EB%8F%8C')
html = res.text     

soup = BeautifulSoup(html, 'html.parser')

for n in range(5,13):
    names = soup.select(f'#mw-pages > div > div > div:nth-child({n}) > ul > li')
# type(names) == list
# type(name) == bs4.element.Tag 이므로 스트링을 얻기 위해서는 name.text를 사용
# ",".join() 함수를 이용해 리스트를 스트링으로 바꾸어주기
# arguments = {"keywords":"Polar bears,balloons,Beaches","limit":20} 에서 Ploar bears, balloons, Beaches는 각각 따로 검색됨. (,를 기준으로 스트링이 split됨)

    arguments = {"keywords":",".join([name.text for name in names]),"limit":2}

    response = google_images_download.googleimagesdownload()

    response.download(arguments)
    