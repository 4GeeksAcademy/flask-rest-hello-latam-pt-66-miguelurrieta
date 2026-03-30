import os
import sys
from sqlalchemy import String, ForeignKey, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "user"
   
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
   
    
    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")

    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="author")

class Post(Base):
    __tablename__ = "post"
   
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
   
    
    author: Mapped["User"] = relationship("User", back_populates="posts")
    
    media: Mapped[list["Media"]] = relationship("Media", back_populates="post")

class Comment(Base):
    __tablename__ = "comment"
   
    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(255), nullable=False)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
   
    author: Mapped["User"] = relationship("User", back_populates="comments")

class Media(Base):
    __tablename__ = "media"
   
    id: Mapped[int] = mapped_column(primary_key=True)
    url: Mapped[str] = mapped_column(String(255))
    post_id: Mapped[int] = mapped_column(ForeignKey("post.id"))
   
    post: Mapped["Post"] = relationship("Post", back_populates="media")


try:
    render_er(Base, 'diagram.png')
    print("¡Éxito! El diagrama se guardó en la raíz como diagram.png")
except Exception as e:
    print("Error al generar el diagrama")
    raise e