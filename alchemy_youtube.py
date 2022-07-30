from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Playlist(Base):
    __tablename__ = 'playlists'

    id = Column(Integer, primary_key=True)
    yt_playlist_id = Column(Text)
    name = Column(Text)
    address = Column(Text)

    def __repr__(self):
        return f'Playlist {self.name}'


class Video(Base):
    __tablename__ = 'videos'
    # table control
    id = Column(Integer, primary_key=True)
    # basic information
    yt_video_id = Column(Text)
    title = Column(Text)
    description = Column(Text)
    created_at = Column(DateTime)
    # statistics
    viewCount = Column(Integer)
    likeCount = Column(Integer)
    dislikeCount = Column(Integer)
    commentCount = Column(Integer)
    author = Column(Text)
    # caption
    has_caption = Column(Boolean)

    def __repr__(self):
        return f'Video {self.twitter_id}'

class Caption(Base):
    __tablename__ = 'captions'
    id = Column(Integer, primary_key=True)
    video_id = Column(Integer, ForeignKey("videos.id"), nullable="False")
    order = Column(Integer)
    minute = Column(Integer)
    line = Column(Text)
    #controle de busca
    was_searched = Column(Boolean, default=False)
    has_terms = Column(Boolean)



class TermCaption(Base):
    __tablename__ = 'term_caption'
    id = Column(Integer, primary_key=True)
    term_id = Column(Integer, ForeignKey("terms.id"), nullable="False")
    caption_id = Column(Integer, ForeignKey("captions.id"), nullable="False")

class Term(Base):
    __tablename__ = 'terms'

    id = Column(Integer, primary_key=True)
    theme = Column(Text)
    term = Column(Text)
    positive = Column(Boolean)
