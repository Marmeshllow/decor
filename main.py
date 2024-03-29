import requests
from bs4 import BeautifulSoup
from decor import logs_decor
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
path = 'C:/ESD/'


@logs_decor(path)
def get_habr_art(keywords):
    url = 'https://habr.com'
    art_list = []

    response = requests.get(f'{url}/ru/all/')
    response.raise_for_status()
    soup = BeautifulSoup(response.text, features='html.parser')
    articles = soup.find_all(class_='tm-article-snippet__title-link')

    for key in articles:
        cool = False
        response = requests.get(f'{url}{key["href"]}')
        soup = BeautifulSoup(response.text, features='html.parser')
        title = soup.find(class_='tm-article-snippet__title tm-article-snippet__title_h1').span.text
        title = str(title).lower()

        pub_data = soup.find('time')['title']

        hubs = soup.find_all(class_='tm-article-snippet__hubs-item-link')
        for el in hubs:
            hub = el.find('span').text
            hub = str(hub).lower()
            if hub in keywords:
                cool = True
                break

        body = soup.find(id='post-content-body')
        s = body.find_all(text=True)
        s = ''.join(s)
        s.lower()
        for keyword in keywords:
            if keyword in s:
                cool = True
                break

        if cool:
            art_list.append(f'[{pub_data},{title.capitalize()},{url + key["href"]}]')
    return art_list


res = get_habr_art(KEYWORDS)

