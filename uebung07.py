"""Strukturierte Programmierung: Übung 7"""

from utils import test

def prime_factorize(n):
    """1. Primfaktorenzerlegung

    Schreiben Sie eine Python-Funktion, die für eine gegebene Zahl eine Primfaktorenzerlegung
    durchführt und die Primfaktoren als Ergebnis zurückliefert. Überlegen Sie sich auch, wie Sie
    Funktion optimieren können.

    | 240 | 2 |
    | 120 | 2 |
    |  60 | 2 |
    |  30 | 2 |
    |  15 | 3 |
    |   5 | 5 |
    |   1 |   |
    
    """
    print(n)

def find_text(text, pattern, case_sensitive = False):
    """2. Suche nach einer Teilzeichenkette

    Entwickeln Sie eine Python-Funktion, die alle Positionen (d.h. den Anfangsindex) zurückliefert, an
    denen die Teilkette pattern in der Zeichenkette text vorkommt. Zusätzlich soll ein Parameter
    mitübergeben werden, der über die Berücksichtigung der Groß-/Kleinschreibung entscheidet.

    Beispiel:
    - text: Dieses da ist es
    - pattern: es

    Positionen sind: 2, 4, 14

    Für die Implementierung dürfen keine Bibliotheksfunktionen verwendet werden
    """
    for p in pattern:
        for t in text:
            pass
            
            

def build_team(players):
    """3. Teambildung

    Prof. Mayar steht vor folgendem Problem. Er ist Trainer eines Fußballteams mit 15 Spieler:innen.
    Jetzt ist es so, dass er auf ein Hallenturnier eingeladen wurde, bei dem er zwei Teams stellen
    möchte, die ungefähr die gleiche Spielstärke und Spieler:innenanzahl haben. Dazu hat er seine
    Spieler:innen wie folgt nach Spielstärke bzw. Position eingeteilt:

    | Spielstärke bzw. Position | Name                                              |
    |---------------------------+---------------------------------------------------|
    | Tor                       | Maria, Max                                        |
    | A+                        | Xaver, Lucia                                      |
    | A                         | Jenni, Hans, Otto, Franz                          |
    | B                         | Klaus, Monika, Gudrun, Oskar, Ryan, Ben, Herlinde |
    
    Entwickeln Sie einen Algorithmus, der es Prof. Mayar, ermöglicht, auf einfache Weise eine 
    Aufteilung in zwei zufällige Teams durchzuspielen. Alle möglichen Varianten sollen bei 
    wiederholtem Ausführen etwa gleich wahrscheinlich auftreten können!
    Bedenken Sie, dass jedes Team eine Torfrau bzw. einen Tormann braucht. Das Ergebnis d.h. die
    Zuteilung der Namen zu einem Team soll am Bildschirm ausgegeben werden.

    Die Lösung soll allgemein gültig sein und nicht nur für das obige Beispiel lösen.
    """
    team_a = []
    team_b = []

    for position in players:
        for p in position:
            pass
        

if __name__ == '__main__':
    print(__doc__)

    # test(prime_factorize, 240)
    # test(find_text, "Dieses da ist es", "es")
    test(build_team, [
        ['Maria', 'Max'],
        ['Xaver', 'Lucia'],
        ['Jenni', 'Hans', 'Otto', 'Franz'],
        ['Klaus', 'Monika', 'Gudrun', 'Oskar', 'Ryan', 'Ben', 'Herlinde']
    ])
