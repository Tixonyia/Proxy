import sys
from selenium import webdriver
import re


# проверка на валтдность URL
def valid_url(url):
    # check url on not
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    if re.match(regex, url):
        return True
    else:
        return False


#  Замена строк
def change_data(data):
    # change to "BlackHub Games"
    req = re.sub(r'\S?(B|b)(l|L)(a|A)(c|C)(k|K)\s*\S*\s*(R|r)(u|U)(s|S)(s|S)(i|I)(a|A)\S?', 'BlackHub Games', data)
    return req


# прогрузка страницы с выгрузкой
def driver_chrom_respons_after_load(url):
    # waiting for the page to fully load
    url_s = url.decode('UTF-8')

    if valid_url(url_s):
        print('Url is valid.')
        driver = webdriver.Chrome()
        driver.set_window_size(800, 600)
        driver.set_window_rect(width=100, height=200)
        driver.get(url_s)
        req = driver.page_source
        driver.close()
    else:
        req = 'Url is not valid.'
        print(req)
    req = change_data(req)
    req = req.encode('UTF-8')
    len_r = sys.getsizeof(req)
    req = str(len_r).encode('UTF-8') + req  # добавление длины в байтах для дискретной передачи
    return req
