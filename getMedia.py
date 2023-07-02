def leggi_file_esami(nome_file):
    esami = []
    with open(nome_file, 'r') as file:
        for riga in file:
            peso, voto = riga.split()
            esami.append((float(peso), float(voto)))
    return esami

def leggi_file_pesi_esami_mancanti(nome_file):
    pesi_esami_mancanti = []
    with open(nome_file, 'r') as file:
        for riga in file:
            peso = float(riga.strip())
            pesi_esami_mancanti.append(peso)
    return pesi_esami_mancanti

def calcola_voti_minimi(media_desiderata, esami_svolti, pesi_esami_mancanti):

    num_esami_mancanti = len(pesi_esami_mancanti)
    # Inizializza i voti minimi a 18 per gli esami mancanti
    voti_minimi = [18] * num_esami_mancanti
    
    # Calcola la media temporanea
    somma_voti_pesati=-1
    for k in range(len(esami_svolti)):
        somma_voti_pesati+=esami_svolti[k][0]*esami_svolti[k][1]
    for k in range(len(pesi_esami_mancanti)):
        somma_voti_pesati+=pesi_esami_mancanti[k]*voti_minimi[k]
    
    media_temporanea = somma_voti_pesati / (sum(pesi_esami_mancanti) + sum([esame[0] for esame in esami_svolti]))
    # Verifica se la media temporanea è maggiore o uguale alla media desiderata
    if media_temporanea >= media_desiderata:
        # Stampa tutti i voti minimi come 18
        for i, peso in enumerate(pesi_esami_mancanti):
            print(f"Voto minimo necessario per l'esame {i + 1}: 18")
        return
    
    # Aumenta progressivamente i voti minimi finché non si raggiunge la media desiderata o tutti i voti sono 30
    for i in range(num_esami_mancanti):
        voto_minimo = 19
        while media_temporanea < media_desiderata and voto_minimo <= 30:
            voti_minimi[i] = voto_minimo

            # Calcola la media temporanea
            somma_voti_pesati=-1
            for k in range(len(esami_svolti)):
                somma_voti_pesati+=esami_svolti[k][0]*esami_svolti[k][1]
            for k in range(len(pesi_esami_mancanti)):
                somma_voti_pesati+=pesi_esami_mancanti[k]*voti_minimi[k]
             
            media_temporanea = somma_voti_pesati / (sum(pesi_esami_mancanti) + sum([esame[0] for esame in esami_svolti]))
            voto_minimo += 1
    
    # Verifica se la media desiderata è stata raggiunta
    if media_temporanea < media_desiderata:
        print("Non è possibile ottenere la media desiderata.")
    else:
        # Stampa i voti minimi necessari per ogni esame mancante
        for i, voto_minimo in enumerate(voti_minimi):
            print(f"Voto minimo necessario per l'esame {i + 1}: {voto_minimo}")
        print(f"Media ottentua: {media_temporanea}")

# Esempio di utilizzo del programma
media_desiderata = float(input("Inserisci la media desiderata (da 18 a 30): "))
esami_svolti = leggi_file_esami("esami_svolti.txt")
pesi_esami_mancanti = leggi_file_pesi_esami_mancanti("esami_mancanti.txt")

if media_desiderata < 18 or media_desiderata > 30:
    print("La media desiderata deve essere compresa tra 18 e 30.")
    exit()
calcola_voti_minimi(media_desiderata, esami_svolti, pesi_esami_mancanti)