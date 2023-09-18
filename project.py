from functions import få_handling, legge_til, fjern, regnut_t, se_liste


def main():
    print("\nVelkommen til Handlelisten! | Søk etter norske produkter ")
    handleliste = []
    while True:
        handling = få_handling()

        if handling == "L":
            legge_til(handleliste)
        elif handling == "S":
            se_liste(handleliste)
        elif handling == "F":
            print(fjern(handleliste))
        elif handling == "T":
            print(regnut_t(handleliste))
        else:
            break



if __name__ == "__main__":
    main()
