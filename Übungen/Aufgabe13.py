from typing import Optional
from dataclasses import dataclass

@dataclass
class Buch:
    titel: str
    autor: str
    ISBN: str

    def __str__(self):
        return f"{self.titel}, {self.autor}, {self.ISBN}"

class Regal:
    def __init__(self, buecher: list[Buch] = []):
        self._buecher = buecher

    @property
    def buecher(self) -> list[Buch]:
        return self._buecher
    
    @buecher.setter
    def buecher(self, buecher):
        self._buecher = buecher

    def __getitem__(self, index) -> Buch:
        return self._buecher[index]
    
    def __setitem__(self, index, buch):
        self._buecher[index] = buch

    def __delitem__(self, index):
        del self._buecher[index]

    def append(self, buch: Buch):
        self._buecher.append(buch)

if __name__ == "__main__":
    # Beispiel-Bücher erstellen
    buch1 = Buch("Numerisches Python", "Bernd Klein", "978-3-446-45076-9")
    buch2 = Buch("Testbuch Eins", "Max Mustermann", "123-4-567-89012-3")
    buch3 = Buch("Testbuch Zwei", "Frau Musterfrau", "123-4-567-89012-4")
    buch4 = Buch("Testbuch Drei", "Hans Beispiel", "123-4-567-89012-5")

    # Regal im Wohnzimmer mit den Büchern füllen
    wohnzimmer_regal = Regal([buch1, buch2, buch3, buch4])

    # Regal im Büro erstellen (leer)
    buero_regal = Regal()

    # 1.) Auf das dritte Buch im Wohnzimmer-Regal zugreifen
    drittes_buch = wohnzimmer_regal[2]
    print(f"Drittes Buch im Wohnzimmer-Regal: {drittes_buch}")

    # 2.) Auf die ISBN-Nummer des zweiten Buches im Wohnzimmer-Regal zugreifen
    zweites_buch_isbn = wohnzimmer_regal[1].ISBN
    print(f"ISBN-Nummer des zweiten Buches im Wohnzimmer-Regal: {zweites_buch_isbn}")

    # 3.) Das erste Buch aus dem Wohnzimmer-Regal entnehmen und dem Büro-Regal hinzufügen
    erstes_buch = wohnzimmer_regal[0]
    buero_regal.append(erstes_buch)
    del wohnzimmer_regal[0]  # Entfernen des Buches aus dem Wohnzimmer-Regal

    print(f"Erstes Buch im Büro-Regal: {erstes_buch}")