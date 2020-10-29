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



conn = sqlite3.connect('fileList.db')

with conn:
    cur = conn.cursor()
    for i in fileList:
        if i.endswith('.txt'):
            print(i)
            cur.execute('INSERT INTO tbl_files(col_fname) VALUES (?)', (i,))
    conn.commit()
conn.close()







