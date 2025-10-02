import csv

def carica_da_file(file_path):
    """Carica i libri dal file"""
    biblioteca = []
    try:
        with open(file_path, newline="") as infile:
            reader = csv.reader(infile)
            for riga in reader:
                biblioteca.append(riga)
        return biblioteca
    except FileNotFoundError:
        return None

#creo una lista (biblioteca) di liste in cui ogni lista contiene il titolo del libro e tutti i suoi attributi


def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    for libro in biblioteca:
        if libro[0] == titolo:
            return None

    nuovo_libro = [titolo, autore, anno, pagine, sezione]
    biblioteca.append(nuovo_libro)

#ora aggingo il nuovo libro anche al file csv
    try:
            with open(file_path, "a", newline="") as outfile:
                writer = csv.writer(outfile)
                writer.writerow(nuovo_libro)
            return nuovo_libro
    except FileNotFoundError:
            return None

#controllo che nella libreria non sia gia presente il titolo da inserire (in tal caso blocco la funzione)
#e nel caso non fosse presente inserisco il libro e i suoi attributi nella libreria

def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO
    for libro in biblioteca:
        if libro[0] == titolo:   #il titolo è la prima colonna!
            return libro
    return None  #Se il ciclo finisce senza trovare nulla, la funzione ritorna None per indicare “non trovato”


def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    risultato = []
    for libro in biblioteca:
        if str(libro[4]) == str(sezione):
            risultato.append(libro[0])

        if not risultato:    #sezione non trovata
            return None

        return sorted(risultato)    # sorted ordina in ordine alfabetico

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

