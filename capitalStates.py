import random
from string import punctuation
import time
from threading import Thread, Timer, Event

StatesCapital = {
    "Italia": "Roma",
    "Francia": "Parigi",
    "Germania": "Berlino",
    "Lussemburgo": "Lussemburgo",
    "Belgio": "Bruxelles",
    "Paesi Bassi": "Amsterdam",
    "Irlanda": "Dublino",
    "Regno Unito": "Londra",
    "Danimarca": "Copenaghen",
    "Grecia": "Atene",
    "Spagna": "Madrid",
    "Portogallo": "Lisbona",
    "Austria": "Vienna",
    "Svizzera": "Zurigo",
    "Svezia": "Stoccolma",
    "Finlandia": "Helsinki",
    "Norvegia": "Oslo",
    "Islanda": "Reykjavik",
    "Estonia": "Tallin",
    "Lettonia": "Riga",
    "Lituania": "Vilnius",
    "Polonia": "Varsavia",
    "Repubblica Ceca": "Praga",
    "Slovacchia": "Bratislava",
    "Ungheria": "Budapest",
    "Slovenia": "Lubiana",
    "Cipro": "Nicosia",
    "Malta": "La Valetta",
    "Romania": "Bucarest",
    "Bulgaria": "Sofia",
    "Croazia": "Zagabria",
    "Bosnia-Erzegovina": "Sarajevo",
    "Serbia": "Belgrado", 
    "Montenegro": "Podgorica",
    "Kosovo": "Pristina",
    "Macedonia d. Nord": "Skopje",
    "Bielorussia": "Minsk",
    "Ucraina": "Kiev",
    "Russia": "Mosca",
    "Lichtenstein": "Vaduz",
    "Andorra": "Andorra la Vella",
    "Albania": "Tirana",
    "Moldavia": "Chisinau",
    "Turchia": "Ankara"
}
keyList = list(StatesCapital)
random.shuffle(keyList)
NewStatesCapital = {}
evaluation = 0
index = 1
wrongResults = []
correctResults = []
beforeProgramTime = time.time()
for nameState in keyList:
    nameCapital = StatesCapital[nameState]
    NewStatesCapital[nameState] = nameCapital
    yourChoice = str(input(f'{index}) {nameState} : '))
    if (yourChoice==nameCapital):
        evaluation+=1
        print("\nCorret +1\n------------------------------------\n")
    elif(yourChoice!=nameCapital):
        print(f'\nNOT corret, è {nameCapital}\n')
        wrongResults.append(yourChoice)
        correctResults.append(nameCapital)
    else:
        print('Error Verdi')
    index+=1
afterProgramTime = time.time()
finalTime = (afterProgramTime-beforeProgramTime)/60
print(f'\nFinised in {finalTime} minutes')
print(f'\nYour evaluation : {evaluation}/44')

len_wrongResults = len(wrongResults)
for i in range(0,len_wrongResults):
    wrongName = wrongResults[i]
    rightName = correctResults[i]
    print(f'\nWrong : {wrongName} , Right : {rightName}')