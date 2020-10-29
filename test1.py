import sqlite3

conn = sqlite3.connect('fileList.db')



with conn:
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS tbl_files;')
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT )')
        
    conn.commit()
conn.close()



fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')
for i in fileList:
    if i.endswith('.txt'):
        print(i)


conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    cur.execute('Select * FROM tbl_files WHERE col_fname LIKE "%txt"')
    cur.execute('''
                INSERT INTO fileList.db.tbl_files(?)
                VALUES
                (i)
                ''')
    conn.commit()
conn.close()







