"""Strukturierte Programmierung: Übung 3"""

from utils import test
from uebung02 import is_leap_year

def russische_bauernmultiplikation(m, n):
    """1. Russische Bauernmultiplikation

    Die „Russische Bauernmultiplikation“ ist ein Verfahren zur Multiplikation zweier Natürlicher Zahlen.
    Informationen dazu finden Sie z.B. unter https://de.wikipedia.org/wiki/Russische_Bauernmultiplikation.

    a) Erklären Sie das Verfahren
    b) Entwickeln Sie einen Algorithmus für das Verfahren als Struktogramm dar

    1. Man schreibt die beiden zu multiplizierenden Zahlen nebeneinander.
    2. Auf der linken Seite (Multiplikator) werden die Zahlen jeweils halbiert (Reste abgerundet) und die
       Ergebnisse untereinander geschrieben, bis man zur 1 gelangt.
    3. Auf der rechten Seite (Multiplikand) werden die Zahlen verdoppelt und untereinander geschrieben.
    4. Die rechts stehenden (verdoppelten) Zahlen werden gestrichen, wenn die links stehende Zahl gerade ist.
    5. Die Summe der nicht gestrichenen rechts stehenden Zahlen ergibt das gesuchte Produkt.
    """
    lcol = [m]
    rcol = [n]

    while m > 1:
        m = m // 2
        n *= 2

        lcol.append(m)

        if m % 2:
            rcol.append(n)

    return sum(rcol)

def tag_im_jahr(year, month, day):
    """2. Tag im Jahr

    Entwickeln Sie ein Python-Programm, der als Eingabe Jahr, Monat (Jan, Feb, …) und einen Tag erhält und
    daraus den Tag im Jahr berechnet und diesen als Ausgabewert zurückliefert. Berücksichtigen Sie auch
    Schaltjahre und prüfen Sie die Eingaben auch auf Korrektheit. Die Jahreszahl enthält das Jahrhundert,
    Monate sind auf drei Zeichen abgekürzt.
    """
    months = {
        'Jan': 31,
        'Feb': 29 if is_leap_year(year) else 28,
        'Mär': 31,
        'Apr': 30,
        'Mai': 31,
        'Jun': 30,
        'Jul': 31,
        'Aug': 31,
        'Sep': 30,
        'Okt': 31,
        'Nov': 30,
        'Dez': 31
    }
    days = day

    if day > months[month]:
        print('FEHLER')
        return

    for m, d in months.items():
        if m == month:
            break

        days += d

    return days

def calc_local_minima_maxima(zahlenreihe):
    """3. Bestimmung von lokalem Minima und Maxima

    Gegeben ist ein Feld von Ganzzahlen (z >= 0). Entwickeln Sie ein Python-Programm, der die
    Anzahl der lokalen Minima und Maxima in der Zahlenreihe bestimmt. Ein lokales Minimum bzw.
    Maximum liegt dann vor, wenn ein Wert in der Zahlenreihe kleiner bzw. größer als die beiden
    benachbarten Werte ist.
    """
    minima = 0
    maxima = 0

    for i, num in enumerate(zahlenreihe):

        # skip first and last number
        if i == 0 or i+1 > len(zahlenreihe) - 1:
            continue

        before = zahlenreihe[i-1]
        after = zahlenreihe[i+1]

        if before < num and after < num:
            maxima += 1

        elif before > num and after > num:
            minima += 1

    return minima, maxima

def average_min_max(values):
    """4. Arithmetisches Mittel + Ausreißer

    Erstellen Sie ein Python-Programm, das für eine vorgegebene Menge von Ganzzahlenwerten
    das arithmetische Mittel bestimmt. Die Werte werden hartkodiert in einem Feld festgelegt d.h.
    values = [ 3, 5, 7, 8, 1, -1, 4, 0 ]

    Neben dem arithmetischen Mittel soll auch der maximale und minimale Wert bestimmt werden
    Beachten Sie, dass Sie auch die Anzahl der Werte in einer eigenen Variable festlegen müssen!
    Testen Sie Ihr Programm mit unterschiedlichen Werten.
    """
    min = 0
    max = 0

    for i in values:
        if i < min:
            min = i
        if i > max:
            max = i

    return sum(values) / len(values), min, max


if __name__ == '__main__':
    print(__doc__)

    test(russische_bauernmultiplikation, 27, 82)
    test(tag_im_jahr, 2004, 'Feb', 14)
    test(calc_local_minima_maxima, [1, 3, 5, 4, 5, 6, 5, 1, 2, 1, 1])
    test(average_min_max, [3, 5, 7, 8, 1, -1, 4, 0])
