
"""
Script that use select to test if images are updated in table Album
"""
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

config=[{"engine": "postgresql://scott:tiger@localhost/chinook", "blob": "bytea"}, {"engine": "sqlite:///../../db/chinook.db", "blob": "blob"}]
engine="postgresql://scott:tiger@localhost/chinook"

for entry in config:
    db = create_engine(entry['engine'])
    Session = scoped_session(sessionmaker(db))
    session = Session()

    for i, row in enumerate(session.execute('select "AlbumId", "Img" from "Album" where "Img" is not NULL ORDER BY "AlbumId"')):
        print(entry['engine'], row[0], len(row[1]))
pass
