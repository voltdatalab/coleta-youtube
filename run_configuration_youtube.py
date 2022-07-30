from alchemy_youtube import Playlist, Video, TermCaption, Caption, Term
from json import load
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL


## Criando tabelas
with open("coleta-youtube/config.json") as jsonfile:
    db_config = load(jsonfile)['database_volt']

engine = create_engine(URL.create(db_config['drivername'], db_config['username'], db_config['password'], db_config['host'],
                                  db_config['port'], db_config['database']),
                       connect_args={'options': '-csearch_path={}'.format(db_config['schema'])})


Playlist.__table__.create(bind=engine, checkfirst=True)
Video.__table__.create(bind=engine, checkfirst=True)
Caption.__table__.create(bind=engine, checkfirst=True)
Term.__table__.create(bind=engine,checkfirst=True)
TermCaption.__table__.create(bind=engine, checkfirst=True)
