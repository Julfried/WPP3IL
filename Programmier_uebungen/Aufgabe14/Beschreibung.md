# Aufgabe 14 "Manuelles Multiplizieren"

### Funktionsbeschreibung

Die Funktion `mult_manu(num_a, num_b)` multipliziert zwei ganze Zahlen und gibt die Zwischenergebnisse sowie das Endergebnis in einem bestimmten Layout aus.

1. **Konvertierung in Strings**: `num_a` und `num_b` werden in Strings umgewandelt, um die Ziffern von `num_b` einzeln zu durchlaufen.

2. **Zwischenergebnisse berechnen**: Jede Ziffer von `num_b` wird mit `num_a` multipliziert und das Ergebnis in `intermediate_results` gespeichert.

3. **Endergebnis berechnen**: Das finale Ergebnis wird durch `num_a * num_b` berechnet.

4. **Formatierte Ausgabe**

   - **Erste Zeile**: Die Eingabezahlen `num_a` und `num_b` werden gemeinsam mit dem Multiplikationszeichen (`*`) angezeigt, z.B. `123 * 456`.

   - **Linie aus Bindestrichen**: Eine Linie aus Bindestrichen (`-`) trennt die Eingabe von den Zwischenergebnissen. Die Länge der Linie wird so berechnet, dass sie die Eingabezahlen und das Ergebnis vollständig abdeckt.

   - **Zwischenergebnisse**: Jedes Zwischenergebnis, das aus der Multiplikation einer Ziffer von `num_b` mit `num_a` resultiert, wird untereinander ausgegeben. Die Zwischenergebnisse sind entsprechend der Position der Ziffer in `num_b` eingerückt, sodass die schriftliche Multiplikation korrekt visualisiert wird.
      - Die erste Ziffer wird ohne Einrückung dargestellt.
      - Jede weitere Ziffer wird um jeweils eine Position weiter nach rechts eingerückt, um die Verschiebung darzustellen.

   - **Abschließende Linie**: Eine weitere Linie aus Bindestrichen wird ausgegeben, um die Zwischenergebnisse vom Endergebnis zu trennen.

   - **Endergebnis**: Das finale Resultat der Multiplikation wird unterhalb der abschließenden Linie ausgegeben.

### Beispielaufrufe

Die Funktion wird mit zwei Beispielaufrufen getestet:

```python
if __name__ == "__main__":
    mult_manu(123, 456)
    print("\n\n")
    mult_manu(100024, 655457)
```

#### Konsolenausgabe der Beispielaufrufe

```
123 * 456
---------
492
 615
  738
---------
56088


100024 * 655457
---------------
700168
 500120
  500120
   000000
    000000
     100024
---------------
65548813768
```