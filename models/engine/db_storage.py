#!/usr/bin/python3
"""Creating a new engine `DBStorage`"""

from models.base_model import Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
import os
from sqlalchemy.orm import sessionmaker
from models.city import City
from models.state import State
from models.place import Place
from models.amenity import Amenity
from models.user import User
from models.review import Review


class DBStorage():
    """Represents a database storage engine"""

    __engine = None
    __session = None

    def __init__(self):
        """Initializes a new instance"""

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                           format(os.environ.get('HBNB_MYSQL_USER'),
                               os.environ.get('HBNB_MYSQL_PWD'),
                               os.environ.get('HBNB_MYSQL_HOST'),
                               os.environ.get('HBNB_MYSQL_DB')),
                           pool_pre_ping=True)

        if (os.environ.get('HBNB_ENV') == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session all objects depending of the class name"""

        dictionary = {}
        query_results = []
        if cls:
            query_results = self.__session.query(eval(cls)).all()

        else:
            class_list = [State, City, User, Place, Review]
            for elem in class_list:
                query_results.extend(self.__session.query(elem).all())

        for field in query_results:
            key = f"{type(field).__name__}.{field.id}"
            dictionary[key] = field
        return (dictionary)

    def new(self, obj):
        """adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None"""
        try:
            if obj:
                self.__session.delete(obj)
        except Exception:
            pass

    def close(self):
        """Disposes of current session if active"""
        self.__session.remove()


    def reload(self):
        """creates all tables in the database"""
        Base.metadata.create_all(self.__engine)

        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
