# Creiamo una var check per vedere se l'utente deve registrarsi o loggarsi
import os
check = input("Devi registrare un account? Y o N: ").strip().upper()

#Inizializziamo le variabili per evitare errori
user = ""
passw = ""

if check == "Y":
    #Registrazione
    user = input("Inserisci il tuo Nome Utente: ")
    print(user, "Nome utente Generato")

    #Registrazione Password
    while True:
        passw = input("Inserisci la password ( minimino 8 caratteri)")
        if len(passw) >= 8:
            print("Password Accettata, registrazione completata")
            break
        else:
            print("La Password inserita non rispetta le condizione")

    print("Ora effettua il Login")
#Adesso se l'utente mette N, ovvero dice che è già registrato, lo portiamo al Login
else:
    print("Perfetto, procediamo direttamente al Login!")

#Login
usercheck = input("Prego inserire nome utente: ")
passwcheck = input("Inserire password utente: ")

#Verifica delle credenziali
if usercheck == user and passwcheck == passw:
    print("Ti sei loggato con Successo!")
    os.system("python Main1.py")
else:
    print("Credenziali errate o nessun account registrato")


