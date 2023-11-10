"""Strukturierte Programmierung: Übung 1"""

from utils import test

def factorio(n):
    """1. Berechnen der Faktoriellen

    Entwickeln ein Python-Programm (Skript), das die Faktorielle einer Zahl n berechnet.
    Verwenden Sie dazu keine speziellen Bibliotheken.
    """
    f = 1

    for i in range(1, n+1):
        f *= i

    return f

def bog2grad(rad):
    """2. Umwandeln von Bogenmaß in Grad

    Entwickeln Sie eine Python-Funktion, die einen Winkel in Bogenmaß in einen Winkel in Grad
    umrechnet.
    """
    return rad * 57.3

def missing_element(liste):
    """3. „Das fehlende Element“

    Gegeben ist eine Liste der Länge n, das eine Folge von ganzen Zahlen aus dem Wertebereich 0
    bis n enthält. Bis auf eine Zahl kommen alle Zahlen aus diesem Wertebereich genau einmal vor,
    z.B. n = 4: (2,1,3,4), es fehlt also die Zahl 0. Gesucht ist eine Python-Funktion, der die fehlende
    Zahl als Ergebnis liefert.
    """
    n = len(liste)

    for i in range(0, n):
        if i not in liste:
            return i

def is_palindrom(n):
    """4. Palindromprüfung

    Entwickeln Sie eine Python-Funktion, die prüft, ob es sich bei einer gegebenen, positiven
    Ganzzahl um ein „Palindrom“ handelt d.h. die Zahl von vorne und von hinten gelesen den
    gleichen Zahlenwert hat. Als Ergebnis soll die Funktion wahr bzw. falsch zurückliefern.

    Bsp.: 12021 ist ein Palindrom, 1231 ist kein Palindrom

    Anmerkung: Die Prüfung soll auf der Basis des zeichenweisen Vergleichens erfolgen!
    """
    p = str(n)

    if p == p[::-1]:
        return True

def invert_number(n):
    """5. Invertieren einer Zahl

    Entwickeln Sie eine Python-Funktion, die eine gegebene, positive Ganzzahl invertiert.

    Bsp.: 123 => 321
    """
    return str(n)[::-1]


if __name__ == '__main__':
    print(__doc__)

    test(factorio, 5)
    test(bog2grad, 6)
    test(missing_element, [0, 1, 3, 4])
    test(is_palindrom, 12021)
    test(invert_number, 456)
