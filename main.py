from spider import Spider
import time

start_time = time.time()
PROJECT_NAME = 'YouTube'
URL = 'https://www.youtube.com/results?search_query=Chitãozinho+e+Chororó&sp=EgIQAUICCAE%253D'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'


# Executa a Spider e o rastreamento da página
def main():
    Spider(PROJECT_NAME, URL)


# Executa método main
if __name__ == '__main__':
    main()
    print("Os dados acima foram salvos no diretório {} no arquivo crawled.txt\n".format(PROJECT_NAME))
    print("O programa foi executado em exatos {} segundos".format(str((time.time() - start_time))))
