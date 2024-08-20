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