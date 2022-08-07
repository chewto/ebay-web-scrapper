from bs4 import BeautifulSoup
import urllib.request


def main():
    url_input = input('please, enter an ebay url: ')

    file_name_input = input('please, enter the file name that will be created: ')
    
    ebay_scrapper(url_input, file_name_input)

# opening the url


def ebay_scrapper(url_arg, file_name_arg):

    open_url = urllib.request.urlopen(url_arg)

    # now analize the website with bs

    # parsing the html

    soup = BeautifulSoup(open_url, 'html.parser')

    article_title_list = []

    article_price_list = []

    article_link_list = []

    for element in soup.find_all('div', 's-item__info clearfix'):
        article_title = element.find('h3', 's-item__title')
        article_price = element.find('span', 's-item__price')
        article_link = element.find('a', {'class': 's-item__link'}).get('href')
        article_title_list.append(article_title)
        article_price_list.append(article_price)
        article_link_list.append(article_link)

    new_articles_title_list = []

    new_articles_price_list = []

    for title, price in zip(article_title_list, article_price_list):

        new_article_title = str(title).replace('</h3>', '')
        new_article_title = new_article_title[26:]

        if '</span>' in new_article_title and '<span class="LIGHT_HIGHLIGHT">' in new_article_title:
            new_article_title = new_article_title.replace('</span>', '')
            new_article_title = new_article_title.replace(
                '<span class="LIGHT_HIGHLIGHT">', '')

        if '</span>' in new_article_title and '<span class="BOLD">' in new_article_title:
            new_article_title = new_article_title.replace('</span>', '')
            new_article_title = new_article_title.replace(
                '<span class="BOLD">', '')

        new_article_price = str(price).replace('</span>', '')
        new_article_price = new_article_price[28:]

        new_articles_title_list.append(new_article_title)
        new_articles_price_list.append(new_article_price)

        print(
            f'title: {new_article_title} \nprice: {new_article_price} \nlink: {article_link}')

    with open(f'{file_name_arg}.txt', 'w', encoding="utf-8") as file:

        for title, price, link in zip(new_articles_title_list, new_articles_price_list, article_link_list):

            file.write('-product title: ' + title + '\n')
            file.write('-product price: ' + price + '\n')
            file.write('-prduct link: ' + link + '\n')


if __name__ == '__main__':
    main()
