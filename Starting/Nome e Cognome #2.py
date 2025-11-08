#Chiederemo nome e cognome, ma solo l'utente scelto potrà accedere ai contenuti
nome=input("Qual'è il tuo nome?")
print(nome,"Grazie per avermelo comunicato")

#Creiamo un altra variabile per il cognome
cognome=input("Qual'è il tuo cognome?")
print(nome,"Grazie per avermelo comunicato")

#Andiamo a specificare le nostre variabili di controllo per l'accesso
nomecheck="Samina"
cognomecheck="Pericleanu"

#Andiamo a creare una variabile IF per verificare il contenuto"
if nomecheck==nome and cognomecheck==cognome:
    print("Ti amo tanto amore")

#Se invece non sono corretti i dati
else:
    print("Accesso negato")