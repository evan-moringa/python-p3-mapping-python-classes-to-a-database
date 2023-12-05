
import sqlite3

class Song:
    def __init__(self, name, album):
        self.name = name
        self.album = album

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('db/music.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS songs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                album TEXT
            );
        ''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('db/music.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO songs (name, album) VALUES (?, ?)
        ''', (self.name, self.album))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, name, album):
        song = cls(name, album)
        song.save()
        return song




        CURSOR.execute(sql)
    