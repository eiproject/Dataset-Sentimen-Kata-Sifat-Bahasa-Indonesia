import requests
from bs4 import BeautifulSoup
from .global_var import URL

def get_spelling(article):
    row = article.find('dl')
    explanation = row.find('dd')
    spellings = [spell.text for spell in explanation.find_all('strong') if spell]
    spelling = ''
    if len(spellings) == 1:
        spelling = spellings[0]
    if len(spellings) > 1 and len(spellings) % 2 == 0:
        for i in range(len(spellings)):
            spell = spellings[i]
            if i%2 == 0: spelling += spell+'-'
            elif i%2 == 1: spelling += spell+', '
        spelling = spelling[:-2]
        
    else:
        pass
    
    return spelling

def get_adjective_explanation(article, spelling):
    row = article.find('dl')
    full_explanation = row.find('dd')
    if spelling: 
        explanation = full_explanation.text.replace(spelling, '')
    else:
        explanation = full_explanation.text
    
    key = 'Adjektiva (kata sifat)'
    if key in explanation:
        explanation = explanation.split(key)[-1]
        
    explanation = explanation.replace('\n', '').replace('\t', '').replace('   ', ' ').replace('  ', ' ')
    return explanation

def get_word(article):
    row = article.find('dl')
    a_in_dt = row.find('dt').find('a')
    word = a_in_dt.text
    return word

def get_url(article):
    row = article.find('dl')
    a_in_dt = row.find('dt').find('a')
    url = a_in_dt['href']
    return url

def Start():
    # URL = "https://kbbi.kata.web.id/kelas-kata/kata-sifat/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.text, "html.parser")
    main = soup.find(id='main')
    for article in main.find_all('article'):
        word = get_word(article)
        url = get_url(article)
        spelling = get_spelling(article)
        explanation = get_adjective_explanation(article, spelling)

        print(word, url)
        print(spelling)
        print(explanation)
        
    return 0