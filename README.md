# Projektna naloga
Pri projektni nalogi za UVP bom analizirala podatke o košarkaših v NBA ligi (sezona 2023/2024). Podatki so objavljeni na spletni strani [basketball-reference.com](https://www.basketball-reference.com/leagues/NBA_2024_totals.html). 

Za vsakega igralca sem zajela: 
- ime, 
- ekipo, 
- pozicijo, 
- starost, 
- št. odigranih iger, 
- št. odigranih minut,
- št. zadetkov za 3 točke,
- št. zadetkov za 2 točke,
- št. zadetih prostih metov,
- asistence,
- ukradene žoge,
- bloki,
- osebne napake in
- skupne točke.

## Navodila za uporabo
Najprej moramo pognati datoteko *prenos_csv.py*, ki bo iz zgornje spletne strani zbrala podatke in jih zapisala v datoteko *nba.csv*. Potem moramo le še pognati datoteko *analiza.ipynb*, v kateri so podatki natančneje analizirani.

Uporabljene knjižnice: requests, bs4, csv, pandas, matplotlib.pyplot, numpy.

