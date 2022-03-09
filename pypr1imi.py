#login system

import time

anti = 420
pas = {'boss' : 'car2', 'care' : '234'}
va = 10
def tim():
    global va
    for i in range(0,va):
        print(va)
        time.sleep(1)
        va = va - 1
    print('Kaboom')
def auto():
    global va
    print('Accesso negato, auto-distruzione fra ' + str(va))
    tim()

for a in range(1,4):
    ut = str(input('Utente : '))
    if ut == '7837':
        print('\n\nAccesso Confermato, Signor 42\n\nAutorizzazione 1')
        break
    else:
        ps = str(input('Password : '))
        if ut in pas:
            if ps == pas[ut]:
                print('\n\nAccesso Confermato, Signor 42\n\nAutorizzazione 2')
                break
            else:
                print('\nErrore\n##### Riprova per la ' + str(a+1) + '° volta #####\n')
                continue
        else:
            print('\nUtente sbagliato\n\n')
if a == 4:
    auto()
    tre = int(input('Codice di disattivazione : \n'))
    if tre != anti:
        quit()
