import requests
from bs4 import BeautifulSoup
import csv

#Definiramo povezavo na spletno stran, ki jo bomo uporabili za pridobivanje podatkov
url = 'https://www.basketball-reference.com/leagues/NBA_2024_per_game.html'

#V spremenjivko shranimo vsebino spletne strani
stanje = requests.get(url)
stanje.raise_for_status() 

#Definiramo spremenjivko, ki bo pregledala HTML kodo spletne strani
pregled_kode = BeautifulSoup(stanje.text, 'html.parser')

#Vpišemo "String", ki ga želimo poiskati v HTML kodi spletne strani
Tabela_na_spletni_strani = pregled_kode.find('table')

#Definiramo dva seznama v katere bomo  shranili podatke
glava = []
vrstice = []

#Poiščemo vrstice v tabeli
vrstice_na_vrhu = Tabela_na_spletni_strani.find('thead').find('tr')
vnosi = [th.get_text(strip=True) for th in vrstice_na_vrhu.find_all('th') if th.get_text(strip=True)]

#Pregledamo vse vrednosti v tabeli in jih shranimo v seznam
for vrstica in Tabela_na_spletni_strani.find('tbody').find_all('tr'):
        stolpci = vrstica.find_all('td')
        podatki = [stolp.get_text(strip=True) for stolp in stolpci]
        vrstice.append(podatki)

#Nakoncu definiramo CVS datoteko in shranimo podatke
izpis_podatkov = 'nba.csv'
with open(izpis_podatkov, mode='w', newline='', encoding='utf-8') as file:
        zapis = csv.writer(file)
        zapis.writerow(glava) 
        zapis.writerows(vrstice)