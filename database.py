from alchemy_youtube import Video, TermCaption, Playlist, Caption, Term
from json import load
import datetime

from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import Session, sessionmaker

with open("coleta-youtube/config.json") as jsonfile:
    db_config = load(jsonfile)['database_volt']

engine = create_engine(URL.create(db_config['drivername'], db_config['username'], db_config['password'], db_config['host'],
                                  db_config['port'], db_config['database']),
                       connect_args={'options': '-csearch_path={}'.format(db_config['schema'])})

def get_terms():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Term).all()


def insere_videos(videos):
    Session = sessionmaker(bind=engine)
    session = Session()

    for video in videos:
        try:
            db_vid = session.query(Video).filter_by(yt_video_id=video['snippet']['resourceId']['videoId']).first()
            if not db_vid:
                # print(video['snippet']['title'])
                session.add(Video(yt_video_id= video['snippet']['resourceId']['videoId'], title = video['snippet']['title'], created_at = video['snippet']['publishedAt'], description = video['snippet']['description'], has_caption = False))
        except:
            print("error")

    session.commit()
    session.close()


def insere_video(video):
    Session = sessionmaker(bind=engine)
    session = Session()


    db_vid = session.query(Video).filter_by(yt_video_id=video).first()
    if not db_vid:
        session.add(Video(yt_video_id=video, has_caption=False))

    session.commit()
    session.close()

def update_video(video):
    Session = sessionmaker(bind=engine)
    session = Session()


    db_vid = session.query(Video).filter_by(yt_video_id=video.videoid).first()
    if db_vid:
        db_vid.title = video.title
        db_vid.description = video.description
        db_vid.created_at = video.published
        db_vid.viewCount = video.viewcount
        db_vid.likeCount = video.likes
        db_vid.dislikeCount = video.dislikes
        db_vid.author = video.username


    session.commit()
    session.close()


def lista_playlists():
    Session = sessionmaker(bind=engine)
    session = Session()

    return session.query(Playlist).all()


def lista_videos(captionless):
    Session = sessionmaker(bind=engine)
    session = Session()

    if (not captionless):
        return session.query(Video).all()
    else:
        return session.query(Video).filter(Video.has_caption.is_(False)).all()


def insere_captions(captions, video):
    Session = sessionmaker(bind=engine)
    session = Session()

    video = session.query(Video).filter_by(yt_video_id=video).first()
    if (video.has_caption == False):
        video.has_caption = True

        for caption in captions:
            if 'line' in caption:
                session.add(Caption(video_id= video.id, order = caption['minute'], minute = caption['minute'], line = caption['line']))

        session.commit()
        session.close()


def get_captions(searched):
    Session = sessionmaker(bind=engine)
    session = Session()

    if (searched):
        return session.query(Caption).all()
    else:
        return session.query(Caption).filter(Caption.was_searched == False).limit(1000).all()


def update_caption(caption):
    Session = sessionmaker(bind=engine)
    session = Session()
    
    db_caption = session.query(Caption).filter(Caption.id==caption.id).first()    
    db_caption.was_searched = True

    session.commit()
    session.close()


def update_caption_term(caption, term):
    Session = sessionmaker(bind=engine)
    session = Session()

    db_caption = session.query(Caption).filter(Caption.id==caption.id).first()    
    db_video = session.query(Video).filter(Video.id == Caption.video_id).first()
    
    db_caption.has_terms = True
    db_video.has_terms = True

    session.add(TermCaption(caption_id = caption.id, term_id = term.id))

    session.commit()
    session.close()


def get_video_to_tweet():
    Session = sessionmaker(bind=engine)
    session = Session()

    db_video = session.query(Video).filter(Video.has_terms == True).filter(Video.bot_tweeted == False).first()
    db_captions = session.query(Caption).filter(Caption.video_id==db_video.id).filter(Caption.has_terms == True).all()
    
    return db_video, db_captions