from selenium import webdriver
import csv

MAIN_PAGE = 'https://realty.yandex.ru/kurgan/kupit/kvartira/'
ADS = []
links = []


def main():
    my_driver = webdriver.Firefox()
    my_driver.get(MAIN_PAGE)
    ads_link = my_driver.find_elements_by_xpath('//a[contains(@class, "serp-item__offer-link")]')
    for i in ads_link:
        links.append(i.get_attribute('href'))  # Получаем список ссылок с первой страницы
    for i in links:
        my_driver.get(i)
        button = my_driver.find_elements_by_xpath('//button[contains(@class, "phones__button")]')
        button[1].click()
        title = my_driver.find_element_by_xpath('//h1[contains(@class, "offer-card__header-text")]').text[0:-1]
        cost = my_driver.find_element_by_xpath('//h3[contains(@class, "offer-card__price")]').text[0:-2]
        name = my_driver.find_element_by_xpath('//div[contains(@class, "offer-card__author-name")]').get_attribute(
            'innerHTML')
        author = my_driver.find_element_by_xpath('//div[contains(@class, "offer-card__author-note")]').get_attribute(
            'innerHTML')
        tel = my_driver.find_element_by_xpath('//span[contains(@class, "phones__phone")]').get_attribute('innerHTML')
        dict_ads = {
            'Заголовок': title,
            'Цена': cost,
            'Имя': name,
            'Агенство': author,
            'Телефон': tel
        }
        ADS.append(dict_ads)
    dialect_params = dict(delimiter=';')
    with open('out_file.csv', 'w', newline='') as csvfile:
        fieldnames = ['Заголовок', 'Цена', 'Имя', 'Агенство', 'Телефон']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, **dialect_params)
        writer.writeheader()
        for i in ADS:
            writer.writerow(i)


if __name__ == '__main__':
    main()
