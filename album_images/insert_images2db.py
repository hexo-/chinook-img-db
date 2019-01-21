"""
Update Album with image from file system. Directory name of image match album id in Chinook database.
"""

import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, scoped_session

def img(album_id):
    """
    Return content from image file
    :param album_id: 
    :return: 
    """
    imgdir = "img/"+str(album_id)+"/"

    image_filenames = os.listdir(imgdir)
    if len(image_filenames)>0:
        imgfilename = image_filenames[0]
        with open(imgdir + imgfilename, "rb") as imgfile:
            return imgfile.read()

config=[{"engine": "postgresql://scott:tiger@localhost/chinook", "blob": "bytea"},
        {"engine": "sqlite:///../../db/chinook.db", "blob": "blob"}]

for entry in config:
    db = create_engine(entry['engine'])
    Session = scoped_session(sessionmaker(db))
    session = Session()
    try: # Ignore if such column already exists
        session.execute('ALTER TABLE "Album" ADD COLUMN "Img" {};'.format(entry['blob']))
    except Exception as e:
        try: #ROLLBACK 4 Postgress
            session.execute('ROLLBACK');
        except:
            pass

    print('\nUpdate images in Album@'+entry['engine'])
    for row in session.execute('select "AlbumId" from "Album"'):
        print('.', end='', flush=True)
        album_id = row[0]
        session.execute('UPDATE "Album" SET "Img" = :img WHERE "AlbumId" = :album_id',
                        {"img":img(album_id), "album_id": album_id})
    session.execute('COMMIT;')
pass
