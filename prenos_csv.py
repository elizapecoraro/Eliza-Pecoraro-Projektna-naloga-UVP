import requests
from bs4 import BeautifulSoup
import csv

# definiramo povezavo spletne strani, ki jo bomo uporabili za pridobivanje podatkov
url = 'https://www.basketball-reference.com/leagues/NBA_2024_totals.html'


# v spremenjivko shranimo vsebino spletne strani
stanje = requests.get(url) 

# definiramo spremenjivko, ki bo pregledala HTML kodo spletne strani
pregled_kode = BeautifulSoup(stanje.content, 'html.parser')

# vpisemo niz, ki ga zelimo poiskati v HTML kodi spletne strani
tabela = pregled_kode.find('table', id="totals_stats")

# za header
headers = [th.text for th in tabela.thead.find_all("th")]

# izberemo samo dolocene stolpce 
izbrani_stolpci = ["Player", "Pos", "Age", "Tm", "G", "MP", "3P", "2P", "FT", "AST", "STL", "BLK", "PF", "PTS"]
izbrani_indeksi = [headers.index(col) for col in izbrani_stolpci]

# za vrstice
vrstice = []
for tr in tabela.tbody.find_all("tr"):
        celice = tr.find_all(["th", "td"])
        vrstica = [celica.text.strip() for celica in celice]
        if len(vrstica) == len(headers):        #da je vrstica enako dolga kot header
                izbrana_vrstica = [vrstica[i] for i in izbrani_indeksi]
                vrstice.append(izbrana_vrstica)

# shranimo v CSV datoteko z uporabo knjiznice csv
with open("NBA.csv", mode="w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(izbrani_stolpci)  # zapisemo samo izbrane stolpce
    writer.writerows(vrstice)  # zapisemo samo izbrane vrstice

