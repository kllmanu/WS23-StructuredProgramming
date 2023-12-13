"""Strukturierte Programmierung: Übung 8"""

from utils import test

def add_item_to_backpack(item, loaded_items, backpack_size):
    """Add a single item with its max amount to the backpack"""

    quantity = 0

    for q in range(0, item['quantity']):
        loaded_items_size = sum(item['quantity'] for item in loaded_items)
        print(loaded_items_size)

        if loaded_items_size < backpack_size:
            quantity += 1

    if quantity > 0:
        item['quantity'] = quantity
        loaded_items.append(item)

def load_backpack(backpack_size, items):
    """1. Bepacken eines Rucksacks 🎒

    Entwickeln Sie einen Algorithmus, der das Problem des optimalen
    Bepackens eines Rucksackes löst. Es geht darum Gegenstände, die
    durch eine Bezeichnung, die Anzahl der Einheiten und den Wert pro
    Einheit bestimmt sind, in einen Rucksack einer vorgegebenen Größe
    zu packen. Optimal bedeutet, dass der Gesamtwert des bepackten
    Rucksacks maximal ist.

    Beispiel:
    Rucksack der Größe: 10
    Gegenstände:

    | Bezeichnung | Einheiten | Wert   |
    |-------------+-----------+--------|
    | Filzstift   |         3 | € 1,-  |
    | Füllfeder   |         1 | € 5,-  |
    | Radiergummi |        40 | € 0,50 |
    | Kreide      |       100 | € 0,10 |
    
    Optimale Bepackung:
    1 x Füllfeder, 3 x Filzstift, 6 x Radiergummi => 11€

    Der Algorithmus liefert als Rückgabewerte die optimale Bepackung
    und auch deren Gesamtwert zurück. Überlegen Sie sich sinnvolle
    Datenstrukturen!
    """
    loaded_items = []
    sorted_items = sorted(items, key=lambda item: item['value'], reverse=True)

    for item in sorted_items:
        add_item_to_backpack(item, loaded_items, backpack_size)

    loaded_items_value = sum(item['value'] * item['quantity'] for item in loaded_items)

    return loaded_items, loaded_items_value

def newtons_method():
    """2. Newtonsches Näherungsverfahren

    https://en.wikipedia.org/wiki/Newton%27s_method

    Das newtonsche Näherungsverfahren ist ein Verfahren zur Lösung von
    nichtlinearen Gleichungen bzw. Gleichungssystemen. Ausgehend von einer
    Funktion werden unter der Verwendung ihrer Tangente (1. Ableitung)
    näherungsweise die Nullstellen bestimmt. Die Annäherung dient infolge
    wieder als neuer Ausgangspunkt für die nächste Näherung. Dieser
    Prozess wird solange wiederholt, bis eine festgelegte Schranke
    unterschritten wird. Wandeln Sie den angegebenen Pseudo-Code in ein
    entsprechendes Python-Programm um. Überlegen Sie sich eine sinnvolle
    Strukturierung.

    f(x) = 2x2 + 3x – 5
    f'(x) = 4x + 3

    function f(x) {
        return 2x2 + 3x – 5
    }

    function f'(x) {
        return 4x + 3
    }

    function NewtonIterationFnct(x) {
        return x – f(x) / f‘(x)
    }

    x := 0.5 // Geratener Startwert
    do {
        xOld := x
        x := NewtonIterationFnct(x)
    } while (|xOld – x| > BORDER) -- z.B. BORDER == 0.001
    """
    pass

def pascals_triangle():
    """3. Pascal’sches Dreieck

    https://en.wikipedia.org/wiki/Pascal%27s_triangle

    Das Pascal’sche Dreieck ist ein Beispiel für eine
    Rekursion. Ausgehend von einem einzelnen gleichseitigen Dreieck
    wird durch sukzessive Erweiterung d.h. hinzufügen neuer Zeilen,
    die jeweils ein Dreieck mehr als die vorherige enthält, ein neues
    gleichseitiges Dreieck erzeugt.

                   ╱╲
                  ╱  ╲
                 ╱ 01 ╲ ................... Anfangssituation
                ╱╲‾‾‾‾╱╲
               ╱  ╲  ╱  ╲
              ╱ 01 ╲╱ 01 ╲ ................ 1. Erweiterung
             ╱╲‾‾‾‾╱╲‾‾‾‾╱╲
            ╱  ╲  ╱  ╲  ╱  ╲
           ╱ 01 ╲╱ 02 ╲╱ 01 ╲ ............. 2. Erweiterung
          ╱╲‾‾‾‾╱╲‾‾‾‾╱╲‾‾‾‾╱╲
         ╱  ╲  ╱  ╲  ╱  ╲  ╱  ╲
        ╱ 01 ╲╱ 03 ╲╱ 03 ╲╱ 01 ╲ .......... 3. Erweiterung
         ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  ‾‾‾‾  
    Jedem Dreieck ist ein numerischer Wert zugeordnet. Dreiecke am
    Rand haben der Wert 1, andere berechnen ihren Wert aus der Summe
    der Nachbarn in der vorherigen Zeile. Mathematisch lässt sich der
    Zusammenhang wie folgt darstellen:

        C (n, k ) = C (n − 1, k − 1) + C (n − 1, k)

        n...aktuelle Zeile
        k...aktuelle Spalte

    Entwickeln Sie eine rekursive Lösung für dieses Problem. Als
    Abbruchbedingung soll die Anzahl der Erweiterungen dienen. Geben
    Sie die berechneten Werde in „ansprechender“ Form am Bildschirm
    aus. Beachten Sie, dass die Werte des Dreiecks nicht gespeichert
    werden dürfen.
    """
    pass


if __name__ == '__main__':
    print(__doc__)

    test(load_backpack, 10, [
        {
            'title': 'Filzstift',
            'quantity': 3,
            'value': 1
        },
        {
            'title': 'Füllfeder',
            'quantity': 1,
            'value': 5
        },
        {
            'title': 'Radiergummi',
            'quantity': 40,
            'value': 0.50
        },
        {
            'title': 'Kreide',
            'quantity': 100,
            'value': 0.10
        },
    ])
