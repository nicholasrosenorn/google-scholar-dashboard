from bs4 import BeautifulSoup
import requests
import pandas as pd


def concat_data(URL):
    soup = instantiate_soup(URL)
    name, sub_header, labels = get_profile_header(soup)
    table_dict = get_publications(soup)
    pubs = pd.DataFrame(table_dict)
    return pubs.to_html()

def instantiate_soup(URL):
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')
    return soup

def get_profile_header(soup):
    name = soup.find('div', attrs = {'id': 'gsc_prf_inw'}).text
    sub_header = soup.find('div', attrs = {'class':'gsc_prf_il'}).text
    labels = [i.text for i in soup.find_all('a', attrs={'class':'gsc_prf_inta gs_ibl'})]
    return name, sub_header, labels

def get_publications(soup):
    table = soup.find('tbody', attrs={'id':'gsc_a_b'})
    titles = [row.text for row in table.findAll('a', attrs={'class': 'gsc_a_at'})]
    titles_urls = [row['href'] for row in table.findAll('a', attrs={'class': 'gsc_a_at'})]
    temp = [row.text for row in table.findAll('div', attrs={'class': 'gs_gray'})]
    authors = [temp[i] for i in range(0, len(temp), 2)]
    journal = [temp[i] for i in range(1, len(temp), 2)]
    cited_by = [row.text for row in table.findAll('td', attrs={'class': "gsc_a_c"})]
    year = [row.text for row in table.findAll('td', attrs={'class': "gsc_a_y"})]

    table_dict = {"title": titles, "url": titles_urls, "author": authors, "journal": journal, "cited_by_number": cited_by, "year": year}

    return table_dict