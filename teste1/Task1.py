import requests
from bs4 import BeautifulSoup
import zipfile
import os


file_links = []


def get_links(title_list,url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'xml')
    link_tags = soup.findAll('a')
    links = []

    for link_tag in link_tags:
        if link_tag.string:
            for title in title_list:
                if title in link_tag.string:
                    links.append(link_tag['href'])

    return links

def download_files(link_list):
    files = []
    for link in link_list:
        file_name = link.split("/")[-1]
        files.append (file_name)

        with open(file_name,'wb') as f:
            r = requests.get(link, stream=True)
            for chunk in r.iter_content(chunk_size=1024*1024*16):
                if chunk:
                    f.write(chunk)

    return files

def zip_files(file_list):
    with zipfile.ZipFile('Anexos.zip','w') as zip:
        for file in file_list:
            zip.write(file)

if __name__ == "__main__":

    url =   "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

    titles = [
    "Anexo I - Lista completa de procedimentos",
    "Anexo II - Diretrizes de utilização",
    "Anexo III - Diretrizes clínicas",
    "Anexo IV - Protocolo de utilização "
]
    links = get_links(titles,url)
    files = download_files(links)
    zip_files(files)

