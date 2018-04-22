from spider import Spider
import time

start_time = time.time()
PROJECT_NAME = 'YouTube'
URL = 'https://www.youtube.com/results?search_query=Chitãozinho+e+Chororó&sp=EgIQAUICCAE%253D'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'


# Executa o rastreamento de página
def main():
    Spider(PROJECT_NAME, URL)


# Executa método main
if __name__ == '__main__':
    main()
    print("O programa foi executado em exatos {} segundos".format(str((time.time() - start_time))))
