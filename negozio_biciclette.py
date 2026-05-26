import mysql.connector

connessione = mysql.connector.connect(
    host="gateway01.eu-central-1.prod.aws.tidbcloud.com",
    port=4000,
    user="2BZEoRab1Jt2wpc.root",
    password="joKqUYHQMk0Qr8Wh",
    database="negozio_biciclette",
    ssl_ca="ca.pem",
    ssl_verify_cert=True
)

cursore = connessione.cursor()

# SELECT 1 - Tutti i clienti
print("=== CLIENTI ===")
cursore.execute("SELECT * FROM Clienti LIMIT 5")
for riga in cursore.fetchall():
    print(riga)

# SELECT 2 - Tutte le biciclette
print("\n=== BICICLETTE ===")
cursore.execute("SELECT * FROM Biciclette LIMIT 5")
for riga in cursore.fetchall():
    print(riga)

# SELECT 3 - Noleggi con nome cliente e bici
print("\n=== NOLEGGI ===")
cursore.execute("""
    SELECT c.nome, c.cognome, b.marca, b.modello, n.data_noleggio, n.data_restituzione
    FROM Noleggi n
    JOIN Clienti c ON n.id_cliente = c.id_cliente
    JOIN Biciclette b ON n.id_bicicletta = b.id_bicicletta
    LIMIT 5
""")
for riga in cursore.fetchall():
    print(riga)

cursore.close()
connessione.close()
print("\nConnessione chiusa.")