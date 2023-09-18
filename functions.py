from tabulate import tabulate
import requests


def få_handling():
    instruksjoner = [
        {"Tast": "L", "Handling": "Legg til produkter"},
        {"Tast": "S", "Handling": "Se handleliste"},
        {"Tast": "F", "Handling": "Fjern produkt fra handleliste"},
        {"Tast": "T", "Handling": "Regn ut totalpris"},
        {"Tast": "A", "Handling": "Avslutt programmet"},
    ]

    print("\n" + tabulate(instruksjoner, headers="keys", tablefmt="simple_grid"))
    while True:
        handling = input("Hva ønsker du å gjøre? ").upper()
        for action in instruksjoner:
            if handling == action["Tast"]:
                return handling
        else:
            print(
                "Du er nødt til å velge en av tastene i menyen for å utføre en handling."
            )
            pass


def legge_til(handleliste):
    while True:
        try:
            item = input("\nHva vil du søke etter?: ").lower().strip()
            empty = []

            headers = {
                "Authorization": "Bearer Q2cQT9h4N5quT5UfIQFkqxSIUDHZG6WEPzwzEqxz"
            }

            params = {
                "search": item,
                "size": 20,
            }

            response = requests.get(
                "https://kassal.app/api/v1/products", params=params, headers=headers
            )
            o = response.json()

            if bool(o["data"]) == False:
                raise Exception

            for index, result in enumerate(o["data"], 1):
                navn, pris, butikk = (
                    result["name"],
                    result["current_price"],
                    result["store"]["name"],
                )
                vare = {
                    "Nummer": index,
                    "Navn": navn,
                    "Pris i NOK": pris,
                    "Butikk": butikk,
                }
                empty.append(vare)
            break
        except Exception:
            print("\nDet var ingen treff på søket ditt. Forsøk på nytt.")
            pass

    print("\n" + tabulate(empty, headers="keys", tablefmt="heavy_grid") + "\n")

    legge_til = ja_nei("Ønsker du å legge til noen av disse produktene? ")
    while legge_til == "ja":
        while True:
            try:
                produkt_valg = få_tall() - 1
                empty[produkt_valg]["Nummer"] = len(handleliste) + 1
                handleliste.append(empty[produkt_valg])
                break
            except IndexError:
                print("Nummeret du velger er nødt til å være en del av resultatet")
                pass
        legge_til = ja_nei("Ønsker du å legge til noen flere av disse produktene? ")


def se_liste(handleliste):
    if handleliste:
        print("\nHer er din handleliste!")
        print(tabulate(handleliste, headers="keys", tablefmt="heavy_grid"))
    else:
        print(
            "\nHandlelisten er tom! Du må legge til produkter før du kan se handlelisten."
        )


def regnut_t(handleliste):
    if handleliste:
        total = 0
        for ordbok in handleliste:
            total += ordbok["Pris i NOK"]
        return f"\nTotal pris er {round(total)} kroner."
    else:
        print(
            "\nHandlelisten er tom! Du må legge til produkter før du kan regne ut totalprisen."
        )


def fjern(handleliste):
    while True:
        try:
            if handleliste:
                print(tabulate(handleliste, headers="keys", tablefmt="heavy_grid"))
                fjerne = int(input("Hvilket nummer har produktet du ønsker å fjerne? "))
                handleliste.pop(fjerne - 1)
                return "\nProduktet er nå fjernet!"
            else:
                return "\nHandlelisten er tom! Det finnes ingen produkter å fjerne."
        except Exception:
            print("Du er nødt til å velge et nummer som er på handlelisten.")
            pass


def få_tall():
    while True:
        try:
            x = int(input("Hvilket nummer ønsker du å legge til? "))
            if x >= 1 and x <= 10:
                return x
            else:
                print("\nNummeret er nødt til å være mellom 1-10")
        except ValueError:
            print("\nDu er nødt til å skrive en tallverdi mellom 1-10.")
            pass


def ja_nei(x):
    while True:
        try:
            svar = input(x).lower()
            if svar == "ja" or svar == "nei":
                return svar

            raise ValueError
        except ValueError:
            print('Du kan kun svare "Ja" eller "Nei"')
            pass
