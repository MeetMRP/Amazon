import bs4
import requests
import csv

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
    num = 1
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