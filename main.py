
"""
Čtvrtý projekt Engeto - Task manager
autor: Patricie Hermanová
email: patriciehermanova@gmail.com
"""
#------------------------------------------------------------------------------

ukoly = []

def hlavni_menu():
    while True:
        print(30*"-")
        print("Správce úkolů - Hlavní menu")
        print("1. Přidat nový úkol")
        print("2. Zobrazit všechny úkoly")
        print("3. Odstranit úkol")
        print("4. Konec programu")

        volba = input("Vyberte možnost (1-4): ")
        print(30*"-")

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print("Konec programu.")
            break
        else:
            print("Neplatná volba, zkuste to znovu.")

def pridat_ukol():
    while True:
        nazev = input("Zadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        if nazev == "" or popis == "":
            print("Název ani popis nesmí být prázdný. Zkuste to znovu.")
        else:
            ukol = {
                "nazev": nazev,
                "popis": popis
            }
            ukoly.append(ukol)
            print(f'Úkol "{nazev}" byl přidán.')
            break

def zobrazit_ukoly():
    if not ukoly:
        print("Seznam úkolů je prázdný.")
    else:
        print("Seznam úkolů:")
        for index, ukol in enumerate(ukoly, start=1):
            print(f"{index}. {ukol['nazev']} - {ukol['popis']}")

def odstranit_ukol():
    if not ukoly:
        print("Nejsou žádné úkoly k odstranění.")
        return

    zobrazit_ukoly()

    cislo = input("Zadejte číslo úkolu, který chcete odstranit: ")

    if not cislo.isdigit():
        print("Zadejte platné číslo.")
        return

    cislo = int(cislo)

    if cislo < 1 or cislo > len(ukoly):
        print("Takový úkol neexistuje.")
    else:
        odstraneny_ukol = ukoly.pop(cislo - 1)
        print(f'Úkol "{odstraneny_ukol["nazev"]}" byl odstraněn.')

hlavni_menu()

