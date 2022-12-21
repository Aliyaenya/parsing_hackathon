
import requests
from bs4 import BeautifulSoup as BS
import csv


def get_html(url):
    resp = requests.get(url)
    return resp.text

def get_soup(html):
    soup = BS(html, 'lxml')
    return soup

def get_models(soup):
    models = soup.find_all('div', class_='list-item list-label')
    # print(models)

    for model in models:
        try:
            title = model.find('div', class_='block title').text.strip()
        except AttributeError:
            title = 'пусто'
        
        try:
            price = model.find('div', class_='block price').get_text(strip=True)
        except AttributeError:
            price = 'нет ценника'

        try:
            image = model.find('div', class_='thumb-item-carousel').find('img', class_='lazy-image').get('data-src')
        except AttributeError:
            image = 'нет фото'

        try:
            des = model.find('div', class_='info-wrapper').get_text(strip=True)
        except AttributeError:
            des = 'нет описания'


        # print(title)
        # print(price)
        # print(image)
        # print(des)




        write_csv({
        'title': title,
        'price': price,
        'image': image,
        'des': des
    })


def write_csv(data):
    with open('models.csv', 'a') as file:
        names = ['title', 'price', 'image', 'des']
        write = csv.DictWriter(file, delimiter=',', fieldnames=names)
        write.writerow(data)



def main():
    for i in range(1,30):
        url = f"https://www.mashina.kg/search/all/ - {i}"
        html = get_html(url)
        soup = get_soup(html)
        mo = get_models(soup)

        if mo == 'end':
            break

        print(f'спарсили {i} страницу')


main()



