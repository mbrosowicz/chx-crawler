import os


# Cada site é um projeto separado (pasta)
def create_project_dir(directory):
    if not os.path.exists(directory):
        print('\nCriando diretório {}\n'.format(directory))
        os.makedirs(directory)


# Cria arquivos de fila e rastreados (se não foram criadas)
def create_data_files(project_name):
    crawled = os.path.join(project_name, "crawled.txt")
    if not os.path.isfile(crawled):
        write_file(crawled, '')


# Cria um novo arquivo
def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# Adiciona dados em um arquivo existente
def append_to_file(path, data):
    with open(path, 'a') as file:
        file.write(data + '\n')


# Remove os dados de um arquivo existente
def delete_file_contents(path):
    open(path, 'w').close()


# Lê um arquivo e converte cada linha em itens list
def file_to_list(file_name):
    results = list()
    with open(file_name, 'rt') as f:
        for line in f:
            results.append(line.replace('\n', ''))
    return results


# Itera através de um conjunto, cada item será uma linha em um arquivo
def list_to_file(links, file_name):
    with open(file_name, "w") as f:
        for l in links:
            f.write(l + "\n")
