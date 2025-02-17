# Analiza rozkładu cechy w danych ciągłych

# Zadanie 1: Funkcja, która oblicza współczynniki zmienności dla ciągu danych,
# w tym średnią, medianę, oraz odchylenie standardowe dla danych w szeregu rozdzielczym punktowym.
def oblicz_srednia(dane1):
    suma_x = 0  # inicjalizacja sumy wartości x * f
    suma_f = sum(dane1.values())  # suma wszystkich częstości (f)

    for x, f in dane1.items():  # iteracja przez wartości (x) i ich liczności (f)
        suma_x += x * f  # mnożenie wartości przez ich częstość i dodanie do sumy

    return suma_x / suma_f  # średnia


def oblicz_mediane(dane1):
    suma_f = sum(dane1.values())
    pozycja_mediany = suma_f / 2  # miejsce mediany
    suma_skumulowana = 0  # inicjalizacja sumy skumulowanej częstości

    for x, f in dane1.items():
        suma_skumulowana += f  # sumowanie skumulowane częstości
        if suma_skumulowana >= pozycja_mediany:  # jeśli suma przekroczy połowę liczby obserwacji
            return x  # zwracamy wartość x jako mediane


def oblicz_odchylenie(dane1):
    srednia = oblicz_srednia(dane1)
    suma_f = sum(dane1.values())
    suma_kwadratow = 0  # inicjalizacja sumy kwadratów różnic

    for x, f in dane1.items():
        suma_kwadratow += ((x - srednia) ** 2) * f  # sumowanie ważonych kwadratów różnic od średniej

    return (suma_kwadratow / suma_f) ** 0.5  # odchylenie standardowe


def oblicz_wspolczynnik_zmiennosci(dane1):
    srednia = oblicz_srednia(dane1)
    odchylenie = oblicz_odchylenie(dane1)

    return (odchylenie / srednia) * 100  # współczynnik zmienności (%)


def analiza_szeregu_punktowego(dane1):
    print("Wyniki analizy szeregu punktowego: ")
    print("Średnia:", oblicz_srednia(dane1))
    print("Mediana", oblicz_mediane(dane1))
    print("Odchylenie standardowe:", oblicz_odchylenie(dane1))
    print("Wspolczynnnik zmiennosci:", oblicz_wspolczynnik_zmiennosci(dane1), "%")
    print()


# Zadanie 2: Funkcja, która oblicza współczynniki zmienności dla szeregu rozdzielczego przedziałowego
def oblicz_srednia_przedzialowa(dane2):
    suma_wazonych_srodkow = 0  # inicjalizacja sumy ważonych środków przedziałów

    for (dolna, gorna), f in dane2.items():  # iteracja przez przedziały i ich częstości
        srodek = (dolna + gorna) / 2  # obliczenie środka przedziału
        suma_wazonych_srodkow += srodek * f  # sumowanie wartości środków przedziałów ważonych częstością

    return suma_wazonych_srodkow / sum(dane2.values())  # średnia przedziałów


def oblicz_odchylenie_przedzialowe(dane2):
    srednia = oblicz_srednia_przedzialowa(dane2)
    suma_f = sum(dane2.values())
    suma_wazonych_kwadratow = 0  # inicjalizacja sumy ważonych kwadratów różnic

    for (dolna, gorna), f in dane2.items():
        srodek = (dolna + gorna) / 2
        suma_wazonych_kwadratow += ((srodek - srednia) ** 2) * f  # sumowanie ważonych kwadratów różnic od średniej

    return (suma_wazonych_kwadratow / suma_f) ** 0.5  # odchylenie standardowe


def oblicz_wspolczynnik_zmiennosci_przedzialowe(dane2):
    srednia = oblicz_srednia_przedzialowa(dane2)
    odchylenie = oblicz_odchylenie_przedzialowe(dane2)

    return (odchylenie / srednia) * 100  # współczynnik zmienności (%)


def analiza_szeregu_przedzialowego(dane2):
    print("Wyniki analizy szeregu przedzialowego: ")
    print("Średnia:", oblicz_srednia_przedzialowa(dane2))
    print("Odchylenie standardowe:", oblicz_odchylenie_przedzialowe(dane2))
    print("Wspolczynnnik zmiennosci:", oblicz_wspolczynnik_zmiennosci_przedzialowe(dane2), "%")
    print()


# Zadanie 3: Funkcja, która wyznacza współczynniki zmienności dla ciągu danych,
# biorąc pod uwagę zastosowanie miar skośności, a także wykorzystując estymatory Grenandera oraz metody „kciuka”

def miary_skosnosci(dane1):
    srednia = oblicz_srednia(dane1)
    odchylenie = oblicz_odchylenie(dane1)
    suma_f = sum(dane1.values())
    suma_wazonych_szescianow = 0  # inicjalizacja sumy ważonych sześcianów różnicv

    for x, f in dane1.items():
        suma_wazonych_szescianow += ((x - srednia) ** 3) * f  # sumowanie ważonych sześcianów różnic od średniej

    return suma_wazonych_szescianow / (suma_f * (odchylenie ** 3))  # współczynnik skośności


def estymator(dane1):
    suma_grenandera = 0  # inicjalizacja sumy ważonych wartości bezwzględnych różnic od średniej
    srednia = oblicz_srednia(dane1)
    suma_f = sum(dane1.values())

    for x, f in dane1.items():
        suma_grenandera += abs(x - srednia) * f  # sumowanie ważonych wartości bezwzględnych różnic

    return suma_grenandera / suma_f  # estymator Grenandera


def metoda_kciuka(dane1):
    odchylenie = oblicz_odchylenie(dane1)
    mediana = oblicz_mediane(dane1)

    return odchylenie / mediana  # współczynnik zmienności metodą kciuka


def analiza_zaawansowana(dane1):
    print("Analiza zaawansowana:")
    print("Skosnosc:", miary_skosnosci(dane1))
    print("Estymator Grenandera:", estymator(dane1))
    print("Metoda kciuka: ", metoda_kciuka(dane1))


dane1 = {1: 4, 2: 7, 3: 15, 4: 10, 5: 6, 6: 5, 7: 3}  # dane szeregu
dane2 = {(0, 5): 8, (5, 10): 14, (10, 15): 22, (15, 20): 18, (20, 25): 10, (25, 30): 6}  # dane szeregu przedziałowego

# wywołanie funckji analizujących dane
analiza_szeregu_punktowego(dane1)
analiza_szeregu_przedzialowego(dane2)
analiza_zaawansowana(dane1)
