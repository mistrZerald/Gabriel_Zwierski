import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import datetime
import time
import numpy as np
import random
import pandas as pd

def ex_1():
    for seq in range(101):
      if seq == 0:
        continue
      elif seq % 3 == 0 and seq % 5 == 0:
        print('fizzbuzz')
      elif seq % 3 == 0:
        print('fizz')
      elif seq % 5 == 0:
        print('buzz')
      else:
        print(seq)
    pass

def ex_2():
    n = int(input("Podaj długość: "))
    with open("losowe.txt", "w") as file:
        for i in range(n):
            file.write(str(random.randint(1, 100)) + "\n")
    pass

def ex_3():
    file_path = "losowe.txt"
    with open(file_path, 'r') as file:
        licz = [int(line.strip()) for line in file]
    print(licz)
    print(type(licz))
    srednia = sum(licz) / len(licz)
    odchylenie = (sum([((x - srednia) ** 2) for x in licz]) / len(licz)) ** 0.5
    mini = min(licz)
    maxi = max(licz)
    sort = sorted(licz, reverse=True)
    print(f"srednia:{srednia}  odchylenie:{odchylenie}  minimalna:{mini}  maxymalna:{maxi}  sortowanie:{sort}")
    return srednia, odchylenie, mini, maxi, sort

    pass

def ex_4():
    n = int(input("Podaj długość ciągu: "))
    fib = []
    lp = []
    for seq in range(n):
        if seq == 0:
            print(0)
            lp.append(1)
            fib.append(0)
        elif seq == 1:
            print(1)
            lp.append(2)
            fib.append(1)
        else:
            lp.append(seq + 1)
            fib.append(fib[seq - 2] + fib[seq - 1])
            print(fib[seq])
    return lp, fib

def ex_5():
    lp, fib = ex_4()
    plt.plot(lp, fib)
    plt.title('Fibonaci')
    plt.xlabel('Lp.')
    plt.ylabel('Liczby ciągu fibonacciego')
    plt.show()
    pass

def ex_6():
    n = int(input("Podaj długość: "))
    slownik = {}
    i = 1
    while n >= i:
        slownik[f'{i}'] = i ** 2
        print(slownik)
        i += 1
    return slownik
    pass

def ex_7():
    slownik = ex_6()
    suma = 0
    for wartosc in slownik.values():
        print(wartosc)
        suma = suma + wartosc
    print(f"suma: {suma}")
    pass

def ex_8():
    now = datetime.datetime.now()
    maketrans = str.maketrans
    nowstr = str(now)
    i = 1
    n = 11
    while n > i:
        now = datetime.datetime.now()
        nowstr = str(now)
        a = nowstr.translate(maketrans('.:', '--'))
        print(a)
        with open(f'{a}.txt', 'w') as file:
            file.write('nowy plik')
        time.sleep(0.2)
        i = i + 1
    pass

def ex_9():
    file_path = 'reference_trajectory.csv'

    zbior = pd.read_csv(file_path, header=None, skiprows=1)
    print(zbior)

    t = zbior[0]
    x = zbior[1]
    y = zbior[2]
    z = zbior[3]

    plt.show()

    fig, (ax1, ax2, ax3) = plt.subplots(3)
    fig.suptitle('pionowe wykresy pozycji x, y ,z dla czasu')
    ax1.plot(t, x)
    ax2.plot(t, y)
    ax3.plot(t, z)
    plt.show()

    print("średnia pozycja dla x:", np.average(zbior[1]))
    print("średnia pozycja dla y:", np.average(zbior[2]))
    print("średnia pozycja dla z:", np.average(zbior[3]))

    pass


def main():
    ex_1()
    ex_2()
    ex_3()
    ex_5()
    ex_6()
    ex_7()
    ex_8()
    ex_9()

if __name__ == '__main__':
    main()
