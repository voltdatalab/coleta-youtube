import pymysql

def conecta_banco():
    address = "projeto7c0db.cuuyhvyykzi3.us-east-2.rds.amazonaws.com"
    username = "lucaslago"
    passw = "xZuiFhK26ItRdL5%gz#P"
    database = "youtube_testes"

    db = pymysql.connect(address, username, passw, database)
    return db
