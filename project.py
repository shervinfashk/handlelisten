import requests
from tabulate import tabulate
from functions import få_handling, legge_til, fjern, regnut_t

handleliste = []


def main():
    print("\nVelkommen til Handlelisten! | Søk etter norske produkter ")

    while True:
        handling = få_handling()

        if handling == "L":
            legge_til()
        elif handling == "S":
            se_liste()
        elif handling == "F":
            print(fjern(handleliste))
        elif handling == "T":
            print(regnut_t(handleliste))
        else:
            break



if __name__ == "__main__":
    main()
