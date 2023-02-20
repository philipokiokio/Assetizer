from sqlalchemy.orm import Session

from src.app.database import SessionLocal


# ORM for interaction with the DB
class BaseRepo:
    def __init__(self) -> None:
        self.db: Session = self.get_db.__next__()

    @property
    def get_db(self):
        sess = SessionLocal()
        try:
            print("Database is ready!")
            yield sess
        except:
            sess.rollback()

        finally:
            sess.close()
            SessionLocal.close()
