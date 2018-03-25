import requests
import urllib
from bs4 import BeautifulSoup
from os import path, makedirs
import wget



class Crawler:
    """
    Class for crawl by page ulr-like 'http(s)://page_path/page_name_{number}/ and download pictures
    """
    def __init__(self, url_pattern, page_number, css_alt=None):
        self.url_pattern = url_pattern
        self.page_number = page_number
        self.image_urls = []
        self.css_alt = css_alt
        self.local_path = path.join(path.dirname(path.realpath(__file__)))
        self.drop_folder = path.join(self.local_path, self.url_pattern.strip().split('/')[-3])

    def get_images_url_list(self):
        for num, image_url in enumerate(self.image_urls):
            print("Number: {}\t Url: {}\n".format(num, image_url))

    def images_urls(self, url_):
        r = requests.get(url_)
        soup = BeautifulSoup(r.content.decode(), "html.parser")
        if self.css_alt:
            allfind = ("img", {"alt": self.css_alt})
        else:
            allfind = ("img")
        for img in soup.findAll(allfind):
            self.image_urls.append(img.get('src'))

    def images(self, url_, drop_name):
        if not path.isdir(self.drop_folder):
            makedirs(self.drop_folder, mode=0o777, exist_ok=True)
        drop_path = path.join(self.drop_folder, drop_name)

        try:
            wget.download(url_.strip(), drop_path)
        except (ValueError, urllib.error.HTTPError) as e:
            print("Can't get url {} on page {} because errors {}".format(url_, self.page_number, e))
            pass

    def main(self):
        page_url = self.url_pattern.format(num=self.page_number)
        self.images_urls(page_url)
        self.get_images_url_list()

        if int(self.page_number) < 10:
            self.page_number = '0{}'.format(self.page_number)

        for num, image_url in enumerate(self.image_urls):
            drop_name = '{}.{}.jpg'.format(self.page_number, num)
            self.images(image_url, drop_name)


if __name__ == '__main__':
    url_p= 'http://site_name_{num}/'
    n = 'num'
    print("Downloading from page {}\n".format(n))
    crawler = Crawler(url_pattern=url_p, page_number=n)
    crawler.main()
