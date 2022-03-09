#primo programma dove uso i principi imparati dal libro Clean Code
mieRisposteimmagazinate = []
pcRisposteimmagazinate = []
risposteSbagliateNum = []
correzioneSbagliateLet = []
numDomanda = 1
punteggio = 0
print('##### Scrivi le TUE risposte #####\n')
while True:
    inputMieRisposte = str(input(f'Che lettera {numDomanda}: '))
    numDomanda+=1
    if len(inputMieRisposte)>1:
        numDomanda = 1
        break
    else:
        mieRisposteimmagazinate.append(inputMieRisposte)
lunghezzaMieRisposte = len(mieRisposteimmagazinate)

print('\n##### Inizio procedura di CORREZZIONE (scrivi le risposte CORRETTE) #####\n')
for i in range(0,lunghezzaMieRisposte):
    inputPcRisposte = str(input(f'Che lettera CORRETTA {numDomanda}: '))
    numDomanda+= 1
    if len(inputPcRisposte)>1:
        break
    else:
        pcRisposteimmagazinate.append(inputPcRisposte)
lunghezzaPcRisposte = len(pcRisposteimmagazinate)
print('\n##### Visione RISULTATI #####\n')
print('\nLe TUE risposte :')
print(mieRisposteimmagazinate)
print('\nLe PC risposte :')
print(pcRisposteimmagazinate)

if lunghezzaMieRisposte==lunghezzaPcRisposte:
    for a in range(0,lunghezzaMieRisposte):
        if str(mieRisposteimmagazinate[a])==str(pcRisposteimmagazinate[a]):
            punteggio+=1
        elif str(mieRisposteimmagazinate[a])=='':
            risposteSbagliateNum.append((a+1))
        else:
            punteggio-=0.25
            risposteSbagliateNum.append((a+1))
    tuttoCorretto = True
else:
    print('ERRORE arancio [lunghezza delle due liste diverse]')
    tuttoCorretto = False

print('\nLe risposte SBAGLIATE :')
print(risposteSbagliateNum)
print('\nLe correzzioni CORRETTE :')
for i in range(0,len(risposteSbagliateNum)):
    correzioneSbagliateLet.append(pcRisposteimmagazinate[risposteSbagliateNum[i]-1])
print(correzioneSbagliateLet)
print(f'\nPunteggio : {punteggio}/{lunghezzaMieRisposte}')

if tuttoCorretto:
    percentuale = ((lunghezzaMieRisposte-len(risposteSbagliateNum))*100)/lunghezzaMieRisposte
    print(f'Percentuale di Correttezza : {percentuale}%')
else:
    print('Errore Gintama connesso al errore arancio [se le liste  sono diverse allora non è possibile calcolare la percentuale]')
