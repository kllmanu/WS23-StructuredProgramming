"""Strukturierte Programmierung: Übung 6"""

import re

from random import randint
from utils import test

def justify_text(text, width):
    return '-'

def randausgleich():
    """1. Schrittweise Verfeinerung: Randausgleich

    In der Vorlesung wurde auf der Basis der Schrittweisen Verfeinerung das „Randausgleich“

    Beispiel erarbeitet. Implementieren Sie dieses in Python, wobei der Text und die gewünschte
    Breite an die erste Verfeinerungsstufe justify_text übergeben werden.
    """
    text = "heute ist ein schoener tag es regnet nicht und alles ist gut$"
    text = justify_text(text, 15)

    return text

def reverse_words(text, n = 0):
    words = text.split()
    reversed_words = []

    # TODO: Position von Satzzeichen beibehalten

    for i, word in enumerate(words):
        if n == 0 or (n > 0 and i % n > 0 or i == 0):
            reversed_words.append(word[::-1])
        else:
            reversed_words.append(word)

    return " ".join(reversed_words)

def replace_keywords(text):
    keywords = {
        "heute": "nretsO",
        "etueh": "nretsO",
        "Bahnhof": "402U",
        "fohnhaB": "402U",
        "alle": "hci",
        "ella": "hci"
    }

    for word, code in keywords.items():
        text = text.replace(word, code)

    return text

def encode_delimiter(text):
    encoded_spaces = '?%&'
    i = randint(0, 2)

    text = text.replace(',', '@')
    text = text.replace('.', '#')
    text = text.replace(' ', encoded_spaces[i])

    return text

def remove_chars(text):
    chars = '.,;-!?%&$#@'

    for c in chars:
        text = re.sub(f"\{c}{{2,}}", c, text)

    return text

def encrypt(text):
    """2. Schrittweise Verfeinerung: Verschlüsselung

    Entwickeln Sie nach dem Prinzip der schrittweisen Verfeinerung einen Algorithmus zur
    Verschlüsselung eines beliebigen Textes. Der Text besteht aus Worten, die durch beliebig viele
    Trennzeichen (Leerzeichen, Komma und Punkt) getrennt sind.

    Das Verschlüsselungsverfahren verschlüsselt den Text nach folgenden Regeln:

    1. Worte werden dadurch verschlüsselt, dass die Buchstaben in umgekehrter
    Reihenfolge (unter Beachtung von Groß- und Kleinschreibung) als „Code“
    verwendet werden.

        d.h. Hugo -> oguH

    2. Jedes 5.te Wort bleibt allerdings unverschlüsselt und wird einfach direkt in den
    chiffrierten Text übernommen.

    3. Es gibt eine Reihe von speziellen Worten, die einen festgelegten Code haben,
    der direkt in den chiffrierten Text übernommen wird.

    | Wort    | Code   |
    |---------+--------|
    | heute   | nretsO |
    | Bahnhof | 402U   |
    | alle    | hci    |

    4. Überflüssige Trennzeichen werden entfernt d.h. mehrfach vorkommende
    Leerzeichen, Kommas, …

    5. Trennzeichen werden speziell verschlüsselt

    | Zeichen     | Kodierungszeichen                               |
    |-------------+-------------------------------------------------|
    | ,           | @                                               |
    | .           | #                                               |
    | Leerzeichen | ? oder % oder &, wobei die Auswahl des Zeichens |
    |             | nach dem Zufallsprinzip erfolgt                 |
    
    """
    text = reverse_words(text, 5)
    text = replace_keywords(text)
    text = encode_delimiter(text)
    text = remove_chars(text)

    return text

if __name__ == '__main__':
    print(__doc__)

    # test(randausgleich)
    test(encrypt, "Ich bin heute am Bahnhof,,,, alle sind da!!!!")
