import sqlite3

conn = sqlite3.connect('fileList.db')



with conn:
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS tbl_files;')
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_files (\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_ftype TEXT) ')
        
    conn.commit()
conn.close()




conn = sqlite3.connect('fileList.db')


with conn:
    cur = conn.cursor()
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('information', 'docx'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('Hello', 'txt'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('myImage', 'png'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('myMovie', 'mpg'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('World', 'txt'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('data', 'pdf'))
    cur.execute('INSERT INTO tbl_files(col_fname, col_ftype) VALUES (?,?)' , \
                ('myPhoto', 'jpg'))
    
    conn.commit()
conn.close()

conn = sqlite3.connect('fileList.db')


with conn:
    cur = conn.cursor()
    cur.execute('SELECT col_fname FROM tbl_files WHERE col_ftype = "txt"')
    varFile = cur.fetchall()
    for item in varFile:
        items = "Your txt files are displayed here: {}.txt".format(item[0] + '{}.txt'.format(item[0]))
    print(items)
