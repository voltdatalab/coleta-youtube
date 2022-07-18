from alchemy_youtube import Playlist, Video, TermCaption, Caption, Term
from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker


## Criando tabelas
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_dml']

engine = create_engine(URL(db_config['drivername'], 
						   db_config['username'], db_config['password'], 
						   db_config['host'], db_config['port'], 
						   db_config['database']))



Playlist.__table__.create(bind=engine, checkfirst=True)
Video.__table__.create(bind=engine, checkfirst=True)
Caption.__table__.create(bind=engine, checkfirst=True)
Term.__table__.create(bind=engine,checkfirst=True)
TermCaption.__table__.create(bind=engine, checkfirst=True)

## Adicionando dados iniciais
with open("config.json") as jsonfile:
    db_config = load(jsonfile)['database_ddl']

engine = create_engine(URL(db_config['drivername'], 
						   db_config['username'], db_config['password'], 
						   db_config['host'], db_config['port'], 
						   db_config['database']))


# Session = sessionmaker(bind=engine)
# session = Session()

# session.add(Playlist(yt_playlist_id = "UU8hGUtfEgvvnp6IaHSAg1OQ", name = "Todos os vídeos do canal do Bolsonaro", address = "https://www.youtube.com/watch?v=&list=UU8hGUtfEgvvnp6IaHSAg1OQ"))

# session.commit()
