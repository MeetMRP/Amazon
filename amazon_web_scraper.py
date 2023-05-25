import bs4
import requests
import csv
import pandas as pd

def Find_products():
    file = open('amazon.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['Product url', 'Product name', 'Product price', 'Rating', 'Number of reviews'])

    for i in range(1, 21):
        print(i)
        url = f'https://www.amazon.in/s?k=bags&page={str(i)}&crid=2M096C61O4MLT&qid=1685027738&sprefix=ba%2Caps%2C283&ref=sr_pg_{str(i)}'
        user_agent = {
            'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/webkit-version (KHTML, like Gecko) Silk/browser-version like Chrome/chrome-version Safari/webkit-version'}
        response = requests.get(url, headers=user_agent)
        soup = bs4.BeautifulSoup(response.content, features="html.parser")

        cards = soup.findAll('div', {'class': 'a-section a-spacing-small a-spacing-top-small'})

        for card in cards:
            try:
                product_url = card.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).get('href')
                product_name = card.find('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'}).text.strip()
                product_price = card.find('span', {'class': 'a-price-whole'}).text.strip()
                rating = card.find('span', {'class': 'a-icon-alt'}).text.strip()
                number_of_reviews = card.find('span', {'class': 'a-size-base s-underline-text'}).text.strip()

                writer.writerow([
                    'https://www.amazon.in'+product_url,
                    product_name,
                    product_price,
                    rating,
                    number_of_reviews
                ])
            except:
                continue

def Find_Product_description():
    data=pd.read_csv("amazon.csv")
    Product_url = list(data['Product url'])

    file = open('product.csv', 'w', newline='', encoding='utf-8')
    writer = csv.writer(file)
    writer.writerow(['Product url', 'Description'])
    count = 1
    for url in Product_url:
        try:
            user_agent = {
                    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/webkit-version (KHTML, like Gecko) Silk/browser-version like Chrome/chrome-version Safari/webkit-version'}
            response = requests.get(url, headers=user_agent)
            soup = bs4.BeautifulSoup(response.content, features="html.parser")

            desc = soup.find('ul', {'class': 'a-unordered-list a-vertical a-spacing-mini'}).findChildren('span', {'class': 'a-list-item'})
            Description = [x.text.replace('<br>', '').strip() for x in desc]

            writer.writerow([
                url,
                Description
            ])
            print(count)
            count+=1
            # prod = soup.find('ul', {'class': 'a-unordered-list a-nostyle a-vertical a-spacing-none detail-bullet-list'}).findChildren('span', {'class': 'a-list-item'})

            # Product_Description = prod[0].text.replace(':', '').replace('\n', '').replace(' ', '').replace('ProductDimensions', '')
            # Date_First_Available = prod[1].text.replace(':', '').replace('\n', '').replace(' ', '').replace('DateFirstAvailable', '')
            # Manufacturer = prod[2].text.replace(':', '').replace('\n', '').replace(' ', '').replace('Manufacturer', '')
            # Asin = prod[3].text.replace(':', '').replace('\n', '').replace(' ', '').replace('ASIN', '')

            # print("****"+Product_Description)
            # print(Date_First_Available)
            # print(Manufacturer)
            # print(Asin)
        except:
            continue

Find_products()
Find_Product_description()