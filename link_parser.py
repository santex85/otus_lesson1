import time

import requests
from bs4 import BeautifulSoup


def get_links(target_url: str) -> list:
    """
    Получить все ссылки с заданного URL
    """
    # получить чистый домен
    try:
        base_url = target_url.split('https://')[1].rstrip('/')
    except IndexError:
        print('Ошибка url, проверь правильность ввода ссылки')
        exit()

    # подготовить заготовку для ответа и сразу внести базовый url
    result = []

    # парсим страницу
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    all_links = soup.find_all('a')

    for link in all_links:
        if 'https' in link['href']:
            if base_url not in link['href']:
                result.append(link['href'])  # добавить найденные ссылки в ответ
    return result


def others_links(links: list) -> None:
    for link in links:
        print(f'В ссылке    {link} есть дополнительные ссылки:')
        links_ = get_links(link)
        for link_ in links_:
            print(f'{link_}')
        print('----------------------------------------------------------------')


if __name__ == '__main__':

    print('Парсер ссылок')
    url = input('Введите url включая https.По умолчанию https://github.com/: ')

    if not url:
        url = 'https://github.com/'

    print(f'Url для парсинга: {url}')

    links = get_links(url)

    save = int(input('Введите 1 если хотите сохранить в файл, 2 если вывести в консоль ответ:'))

    if save == 1:
        with open('result.txt', 'w') as file:
            for link in links:
                file.write(f'{link}\n')
            print('Ваш результат сохранен!')

    if save == 2:
        print('Ваш результат:')
        for link in links:
            print(link)

    print('------------------------------------------------')
    print('Вывод ссылок из результата:')
    time.sleep(2)
    others_links(links)
