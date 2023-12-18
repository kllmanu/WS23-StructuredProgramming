"""Strukturierte Programmierung: Übung 2"""

from utils import test

def zahlenfolge(n):
    """1. Zahlenfolge

    Schreiben Sie eine Python-Funktion, die die Zahlenfolge nach den untenstehend Vorgaben am Bildschirm ausgibt.

    Gegeben die Zahl n aus den natürlichen Zahlen.

    Es gelten die folgenden Regeln:
    • Falls n durch 3 ganzzahlig teilbar ist, wird n um 4 erhöht
    • Falls n nicht durch 3 ganzzahlig teilbar ist, aber durch 4 ganzzahlig teilbar ist, wird n halbiert
    • Falls n weder durch 3 noch durch 4 ganzzahlig teilbar ist, wird n um 1 verkleinert.

    Diese Regeln werden solange angewendet, bis n == 0 ist.
    """
    if not n % 3:
        n += 4
    elif not n % 4:
        n /= 2
    else:
        n -= 1

    return n

def is_leap_year(year):
    """2. Schaltjahr

    In unserem Kalender sind in regelmäßigen Abständen Schaltjahre eingefügt. Zur exakten
    Feststellung, ob ein Jahr ein Schaltjahr ist, dienen folgende Regeln:

    a) Ist die Jahreszahl durch 4 teilbar, so ist das Jahr ein Schaltjahr.

    b) Regel a) hat allerdings die Ausnahme, dass ein Jahr das durch 100 teilbar ist, kein Schaltjahr ist.
    c) Regel b) hat allerdings die Ausnahme, dass ein Jahr das durch 400 teilbar ist, doch ein Schaltjahr ist.

    Entwickeln Sie dafür eine Python-Funktion
    """
    leap_year = False

    if not year % 4:
        leap_year = True

        if not year % 100:
            leap_year = False

            if not year % 400:
                leap_year = True

    return leap_year

def nimm_spiel():
    """3. Nimm-Spiel

    Das Nimm-Spiel ist ein einfaches Zweipersonen-Spiel, bei dem 12 Münzen so auf drei Reihen
    aufgeteilt werden, dass die erste Reihe 5, die zweite Reihe 4 und die dritte Reihe 3 Münzen
    enthält.

          O O O
         O O O O
        O O O O O  1. Reihe

    Die Spieler:innen entfernen abwechselnd aus einer der drei Reihen eine beliebige Anzahl von
    Münzen. Sieger:in ist derjenige, der die letzte Münze nimmt.

    Entwickeln Sie ein Python-Programm, das dieses Spiel als Konsolen-Applikation umsetzt.

    Sie können davon ausgehen, dass alle Eingaben immer korrekt sind.
    """
    rows = [
        ['0', '0', '0'],
        ['0', '0', '0', '0'],
        ['0', '0', '0', '0', '0']
    ]

    while True:
        for idx, row in enumerate(rows):
            print(' '.join(row).center(15))

        step = input()
        row, *cols = step.split()
        row = int(row) - 1

        for col in cols:
            rows[row][int(col)-1] = ' '

        if not any('0' in cols for cols in rows):
            print('GEWONNEN!')
            break

if __name__ == '__main__':
    print(__doc__)

    test(zahlenfolge, 15)
    test(is_leap_year, 2008)
    test(nimm_spiel)
