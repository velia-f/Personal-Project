#trovare i divisori di N, esempio func(30) : 1,2,3,5.6,10.15.30
import webbrowser
import time
number = int(input('Scrivi un Numero : '))
for i in range(1, number+1):
    if number%i==0:
        print(i)
print('\nSuppongo che tutto sia corretto. Giusto?\n\nGoditi il seguente Masterpiece, non arrenderti motherfucker !!!')
print('\nConto alla rovescia per il caricamento di Evangelion (5sec)')
timecount = 5
while timecount>0:
    print(timecount)
    timecount-=1
    time.sleep(1)
webbrowser.open('https://www.youtube.com/watch?v=TdV0Cr3d5Hk&list=PLUnpILH4MVhnj667V4ERsqjL0trX-BrMi&index=32&t=167s')
