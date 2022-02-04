# importiamo il modulo socket
import socket

nome_utente = input("Inserire il nome dell'utente: ")

# chiediamo l'IP del server
ip_server = input("Inserire l'indirizzo IP del server: ")
# chiediamo la porta del server
porta_server = int(input("Inserire la porta del server: "))
# creiamo il socket
client_socket = socket.socket()
# stabiliamo la connessione al server
client_socket.connect((ip_server, porta_server))

print("Connessione effettuata!")

while True: # per sempre
    msg_client = input("> ") # chiediamo il messaggio all'utente client
    msg_client = nome_utente + "> " + msg_client
    client_socket.send(bytes(msg_client, "utf-8")) # e lo inviamo come gruppo di byte al server via socket
    if msg_client == "STOP!": # se tale messaggio è "STOP!"
        break # usciamo dal ciclo
    msg_server = client_socket.recv(1024) # leggiamo quanto scritto dal socket (1024 byte)
    print(f"{str(msg_server, 'utf-8')}") # e lo stampiamo, dopo essere stato convertito in stringa

# siamo usciti dal ciclo, avviso l'utente del client
print("Fine della connessione, come richiesto.")

# chiudiamo il socket
client_socket.close()