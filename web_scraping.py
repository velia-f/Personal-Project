import requests, bs4, webbrowser
cost_link = 'https://www.staseraintv.com/programmi_stasera_'
possibili_canali = ['canale5.html#pal', 'italia1.html#pal', 'canale20mediaset.html#pal', 'rai4.html#pal', 'iris.html#pal']
canali_numero = ['CANALE 5', 'CANALE 6', 'CANALE 20', 'CANALE 21', 'CANALE 22']

for i in range(0,5):
    attuale_possibili_canali = possibili_canali[i]
    link = cost_link+attuale_possibili_canali
    response = requests.get(link)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    sotto_sezione = soup.find('div', class_='leftcolbox')
    a_sezione = sotto_sezione.find_all('a')
    link_sezione = []
    for a_sezione_new in a_sezione:
        link_sezione_new = str(a_sezione_new.get('href'))
        if link_sezione_new not in link_sezione:
            link_sezione.append(link_sezione_new)
    penultimo = link_sezione[-2]
    penultimo_splittato = penultimo.split('/')
    ultimo = penultimo_splittato[-1]
    penultimo_splittato = ultimo.split('.html')
    penultimo_splittato.pop()
    valore_finale = penultimo_splittato[0]
    print(canali_numero[i]+'\n')
    print(valore_finale)
    print('############################################\n')
