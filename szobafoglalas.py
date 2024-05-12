import datetime
class Szoba:
  def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 12999)

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 18999)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []
        self.foglalasok = []

    def szoba_hozzaadasa(self, szoba):
        self.szobak.append(szoba)

    def foglalas(self, szobaszam, datum):
        for szoba in self.szobak:
            if szoba.szobaszam == szobaszam:
                for foglalas in self.foglalasok:
                    if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                        return False
                foglalas = Foglalas(szoba, datum)
                self.foglalasok.append(foglalas)
                return True, szoba.ar
        return False, None

    def lemondas(self, szobaszam, datum):
        for foglalas in self.foglalasok:
            if foglalas.szoba.szobaszam == szobaszam and foglalas.datum == datum:
                self.foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self):
        foglalasok = []
        for foglalas in self.foglalasok:
            foglalasok.append({"szobaszam": foglalas.szoba.szobaszam, "datum": foglalas.datum.strftime('%Y-%m-%d')})
        return foglalasok

def main():
    szalloda = Szalloda("Szalloda")

    szalloda.szoba_hozzaadasa(EgyagyasSzoba("1"))
    szalloda.szoba_hozzaadasa(EgyagyasSzoba("3"))
    szalloda.szoba_hozzaadasa(KetagyasSzoba("2"))

    szalloda.foglalas("1", datetime.date(2024, 5, 10))
    szalloda.foglalas("3", datetime.date(2024, 7, 6))
    szalloda.foglalas("2", datetime.date(2024, 5, 9))
    szalloda.foglalas("1", datetime.date(2024, 5, 10))
    szalloda.foglalas("3", datetime.date(2024, 5, 11))

    while True:
        print("A szállodában 3 szoba van, egy, illetve egy másik kétágyas eloszlásban foglalható. Egyágyas szoba az 1-es és a 3-as szoba, kétágyas szoba a 2-es.")
        print("\nVálasszon egy opcíót:")
        print("1. Szoba foglalása")
        print("2. Foglalás lemondása")
        print("3. Foglalások listázása")
        print("0. Kilépés")
        valasztas = input("Adja meg a választott opció számát: ")
        if valasztas == "1":
            szobaszam = input("Adja meg a foglalni kívánt szoba számát: ")
            lehetséges_szobaszámok = "1" "3" "2"
            if szobaszam not in lehetséges_szobaszámok:
                print("A megadott szobaszám nem létezik.")
                return
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
                success, ar = szalloda.foglalas(szobaszam, datum)
                if success:
                    print(f"Sikeres foglalás! Ár: {ar}Ft")
                else:
                    print("Valamely szöveg hibás vagy a szoba már foglalt ezen a napon.")
            except ValueError:
                print("Hibás dátumformátum! Kérem, adjon meg érvényes dátumot.")

        elif valasztas == "2":
            szobaszam = input("Adja meg a lemondani kívánt foglalás szoba számát: ")
            datum_str = input("Adja meg a foglalás dátumát (ÉÉÉÉ-HH-NN formátumban): ")
            try:
                datum = datetime.datetime.strptime(datum_str, "%Y-%m-%d").date()
                if szalloda.lemondas(szobaszam, datum):
                    print("Sikeres lemondás!")
                else:
                    print("Nem található ilyen foglalás.")
            except ValueError:
                print("Hibás dátumformátum! pl: 2024-05-10")

        elif valasztas == "3":
            print("Lefoglalt szobák:")
            foglalasok = szalloda.foglalasok_listazasa()
            if foglalasok:
                for foglalas in foglalasok:
                    print(f"Foglalt szoba: {foglalas['szobaszam']}, Dátum: {foglalas['datum']}")
            else:
                print("Nincsenek foglalások.")

        elif valasztas == "0":
            print("Kilépés...")
            break

        else:
            print("Válasszon a 0 1 2 3! Kérem, válasszon újra.")

if __name__ == "__main__":
    main()