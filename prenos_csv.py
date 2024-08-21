import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

#definiramo povezavo na spletno stran, ki jo bomo uporabili za pridobivanje podatkov
url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'
#da nas spletna stran ne zavrne
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#}      ni treba 


#v spremenjivko shranimo vsebino spletne strani
stanje = requests.get(url) 

#definiramo spremenjivko, ki bo pregledala HTML kodo spletne strani
pregled_kode = BeautifulSoup(stanje.content, 'html.parser')

#vpisemo niz, ki ga zelimo poiskati v HTML kodi spletne strani
tabela = pregled_kode.find('table', id="totals_stats")

#za header
headers = [th.text for th in tabela.thead.find_all("th")]

#za vrstice
vrstice = []
for tr in tabela.tbody.find_all("tr"):
        celice = tr.find_all(["th", "td"])
        vrstica = [celica.text.strip() for celica in celice]
        if len(vrstica) == len(headers):        #da je vrstica tok dolga kt header
                vrstice.append(vrstica)

#naredimo DataFrame (s pomocjo knjiznice pandas)
df = pd.DataFrame(vrstice, columns=headers)

#shranimo v csv
df.to_csv("NBA.csv", index=False)

