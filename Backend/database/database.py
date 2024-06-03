from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///Backend/my_book_store.db', connect_args={'check_same_thread': False})
Base = declarative_base()
session_local = sessionmaker(bind=engine, autoflush=False)


def get_db():
    session = session_local()
    try:
        yield session
    finally:
        session.close()
