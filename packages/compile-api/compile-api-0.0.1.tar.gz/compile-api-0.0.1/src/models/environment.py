"""models.py"""
from sqlalchemy import Column, Integer, String, Boolean,Text
from sqlalchemy.orm import Session
from models.database import Database

#instance for database
db=Database()

#instance for create declarative base
Base=db.create_base()


class Environment(Base):
    """
    Table ENVIRONMENT
    """

    __tablename__='ENVIRONMENT'

    id = Column(Integer, primary_key=True,index=True,autoincrement=True)
    name=Column(String)
    url=Column(String)
    enabled=Column(Boolean,default=bool(True))
    version=Column(String)
    is_latest=Column(Boolean,default=bool(True))
    base_image_id=Column(Integer,default=0)
    short_name = Column(String(5))
    status = Column(String,default="Draft")
    icon=Column(String)
    py_version=Column(String)
    r_version=Column(String)
    py_requirements=Column(Text)
    r_requirements=Column(Text)
    py_requirements_compiled=Column(Text)
    r_requirements_compiled=Column(Text)


    def get_py_requirements(self, db_session: Session):
        """
        Get Py requirements. If py_requirements_compiled is not None, return it, otherwise return py_requirements.

        Args:
            db_session: Database session.

        Returns:
            str: Py requirements.
        """
        return self.py_requirements_compiled if self.py_requirements_compiled!="NULL" else self.py_requirements

    @staticmethod
    def get_requirements_by_id(db_session: Session, image_id: int):
        """
        Get Py requirements by image ID.

        Args:
            db_session: Database session.
            image_id (int): Image ID.

        Returns:
            str: Py requirements.
        """

        environment = db_session.query(Environment).filter(Environment.id == image_id).all()
        if environment:
            return environment[0].get_py_requirements(db_session)
        return None
