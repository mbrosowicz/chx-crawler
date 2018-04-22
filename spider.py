from urllib.request import urlopen
from general import *
from bs4 import BeautifulSoup
import requests


class Spider:
    project_name = ''
    url = ''
    crawled_file = ''
    crawled = list()

    def __init__(self, project_name, url):
        Spider.project_name = project_name
        Spider.url = url
        Spider.crawled_file = Spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page(Spider.url)

    # Cria diretório e arquivos para o projeto na primeira execução e inicia a spider
    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name)
        Spider.crawled = file_to_list(Spider.crawled_file)

    # Atualiza a exibição do usuário e atualiza os arquivos
    @staticmethod
    def crawl_page(url):
        print('Agora rastreando {}\n'.format(url))

        try:
            link_request = requests.get(url)
        except Exception as e:
            print(str(e))
            return list()
        soup = BeautifulSoup(link_request.text, 'html.parser')
        views = soup.find_all(id='test')
        order_number = 0

        videos = soup.find_all("a", attrs={"class",
                                           "yt-uix-tile-link yt-ui-ellipsis yt-ui-ellipsis-2 yt-uix-sessionlink spf-link "})

        video_info = soup.find_all("ul", attrs={"class", "yt-lockup-meta-info"})

        video_titles = [video.text for video in videos]

        for view_info in video_info:
            if len(view_info.contents) >= 2:
                views += view_info.contents[1]

        views_text = [view for view in views]

        for title in video_titles:
            order_number += 1
            Spider.crawled.append('{} ) {}'.format(order_number, title))
            Spider.crawled.append('{} ) {}\n'.format(order_number, views_text[order_number - 1]))
        Spider.crawled.sort(key=lambda x: int(x.split(')')[0]))
        Spider.update_files()

    @staticmethod
    def update_files():
        list_to_file(Spider.crawled, Spider.crawled_file)
