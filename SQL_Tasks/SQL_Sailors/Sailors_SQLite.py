# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:52:43 2021

@author: erdmk
"""

#%% 
"""
Öğrendiklerim

Primary key: eşsiz anahtar oluşturur.

Foreign key: anahtarların bağlantılarını sağlar 

EXCEPT : İki sorgu içinde ki kümelerin ayrık olanlarını ortaya çıkarır

UNION : İki sorgu çıktısının kesişimini çıkarır.

Sqlite'ın bazı sürümleri foreign key desteklemez print(conn.execute("PRAGMA foreign_keys")) 
ile 1 veya 0 döndermeli

IN : Lokasyon içerisinde değer çekmek için kullanılır.

EXISTS : Nested sorgularda binary karar dönderir ve karmaşıklığı azaltıyor.

ANY : Operatörü SQLite da yok bunun yerine genelde IN kullanılılıyor.

MAX, COUNT, AVG gibi operatörlerle numerik analiz yapılabilmekte

"""

#%% importing sqlite module 
import sqlite3

#%% databasein ayağa kaldırılmasi

conn = sqlite3.connect('task_sql.db')
conn.execute("PRAGMA foreign_keys = 1") # foreign keysin sqlite için aktif edilmesi
c = conn.cursor() 

#%% create table Sailors 
c.execute('''CREATE TABLE IF NOT EXISTS Sailors
             (sid INTEGER,  
              snmame TEXT,
              rating INTEGER, 
              age REAL)''')

#%% create table class 

c.execute('''CREATE TABLE IF NOT EXISTS Reserves
             (sid INTEGER,  
              bid INTEGER,
              day TEXT)''')
             
#%% create table Sailors
c.execute('''CREATE TABLE IF NOT EXISTS Boats
             (bid INTEGER,  
              bname TEXT,
              color TEXT)''')


#%% insert students class 

#c.execute("""INSERT INTO Sailors VALUES(22, 'Dustin ', 7, 45.0)""")
#c.execute("""INSERT INTO Sailors VALUES(29, 'Brutus', 1, 33.0)""")
#c.execute("""INSERT INTO Sailors VALUES(31, 'Lubber', 8, 55.5)""")
#c.execute("""INSERT INTO Sailors VALUES(32, 'Andy', 8, 25.5)""")
#c.execute("""INSERT INTO Sailors VALUES(58, 'Rusty', 10, 35.0)""")
#c.execute("""INSERT INTO Sailors VALUES(64, 'Horatio', 7, 35.0)""")
#c.execute("""INSERT INTO Sailors VALUES(71, 'Zorba', 10, 16.0)""")
#c.execute("""INSERT INTO Sailors VALUES(74, 'Horatio', 9, 35.0)""")
#c.execute("""INSERT INTO Sailors VALUES(85, 'Art', 3, 35.0)""")
#c.execute("""INSERT INTO Sailors VALUES(95, 'Bob', 3, 63.5)""")
conn.commit()

#%% Insterting Reserves 

#c.execute("""INSERT INTO Reserves VALUES(22, 101, '10/10/98')""")
#c.execute("""INSERT INTO Reserves VALUES(22, 102, '10/10/98')""")
#c.execute("""INSERT INTO Reserves VALUES(22, 103, '10/8/98')""")
#c.execute("""INSERT INTO Reserves VALUES(22, 104,'10/7/98')""")
#c.execute("""INSERT INTO Reserves VALUES(31, 102, '11/10/98')""")
#c.execute("""INSERT INTO Reserves VALUES(31, 103, '11/6/98')""")
#c.execute("""INSERT INTO Reserves VALUES(31, 104, '11/12/98')""")
#c.execute("""INSERT INTO Reserves VALUES(64, 101, '9/5/98')""")
#c.execute("""INSERT INTO Reserves VALUES(64, 102, '9/8/98')""")
#c.execute("""INSERT INTO Reserves VALUES(74, 103, '9/8/98')""")
conn.commit()

#%% Insterting Boats 
#c.execute("""INSERT INTO Boats VALUES(101, 'Interlake', 'blue')""")
#c.execute("""INSERT INTO Boats VALUES(102, 'Interlake', 'red')""")
#c.execute("""INSERT INTO Boats VALUES(103, 'Clipper', 'green')""")
#c.execute("""INSERT INTO Boats VALUES(104, 'Marine','red')""")
conn.commit()

#%% BASİC QUERİES

#%% 1 - ) Find the' names and ages of all sailors.

cursor = conn.execute('''SELECT DISTINCT S.snmame, S.age
                      FROM Sailors AS S''')
for row in cursor:
    print(row)

#%% 2-) Find all sailors with a rating above 7

cursor = conn.execute('''SELECT S.sid, S.snmame, S.rating, S.age
                      FROM Sailors AS S 
                      WHERE S.rating > 7 ''')
for row in cursor:
    print(row)

#%% 3-) Find the names of sailors 'Who have reseTved boat number

cursor = conn.execute('''SELECT S.snmame
                         FROM Sailors S, Reserves R
                         WHERE S.sid = R.sid AND R.bid = 103''')
                      
for row in cursor:
    print(row)

#%% 4-) Find the sids of sailors who have TeseTved a red boat

cursor = conn.execute('''SELECT R.sid 
                         FROM Boats B, Reserves R
                         WHERE B.bid = R.bid AND B.color = 'red' ''')

for row in cursor:
    print(row)

#%% 5- ) Find the names of sailors 'Who have TeseTved a red boat

cursor = conn.execute('''SELECT S.snmame
                         FROM Sailors S, Boats B, Reserves R
                         WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red' ''')
for row in cursor:
    print(row)
    
#%% 6- ) Find the colorS of boats reserved by Lubbe

cursor = conn.execute("""SELECT B.color 
                      FROM Sailors S, Boats B, Reserves R
                      WHERE S.sid = R.sid AND R.bid = B.bid AND S.snmame = 'Lubber'""")
for row in cursor:
    print(row)

#%% 7- ) Find the names of sa'iloTs who have Teserved at least one boat

cursor = conn.execute("""SELECT S.snmame 
                      FROM Sailors S, Reserves R
                      WHERE S.sid = R.sid""")
for row in cursor:
    print(row)

#%% 8-) Find the sids of all sailor's who have reserved red boats but not green boats

cursor = conn.execute('''SELECT S.sid
                         FROM Sailors S, Boats B, Reserves R
                         WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red'
                         EXCEPT
                         SELECT S2.sid
                         FROM Sailors S2, Boats B2, Reserves R2
                         WHERE S2.sid = R2.sid AND R2.bid = B2.bid AND B2.color = 'green' ''')

for row in cursor:
    print(row)
    
#%% 9- ) Find all sids of sailors who have a rating of 10 or reserved boat 104

cursor = conn.execute('''SELECT S.sid
                         FROM Sailors S, Boats B, Reserves R
                         WHERE S.sid = R.sid AND R.bid = B.bid AND S.rating = 10
                         UNION
                         SELECT S2.sid
                         FROM Sailors S2, Boats B2, Reserves R2
                         WHERE S2.sid = R2.sid AND R2.bid = B2.bid AND B2.bid = 104 ''')

for row in cursor:
    print(row)

#%% NESTED QUERIES 

#%% 1-)  Find the names of sailors who have reserved boat 103.

"""
103 boat -> s.sid -> s.sname
"""
cursor = conn.execute("""SELECT S.snmame
                      FROM Sailors S
                      WHERE S.sid IN(SELECT R.sid
                                     FROM Reserves R
                                     WHERE R.bid = 103)""")

for row in cursor:
    print(row)

#%% 2-) Find the names of sailors 'who ha'ue reserved a red boat

"""
red boat -> r.sid number -> s.sid number -> s.snmame  
"""
cursor = conn.execute("""SELECT S.snmame 
                      FROM Sailors S
                      WHERE S.sid IN(SELECT R.sid
                                     FROM Reserves R
                                     WHERE R.bid IN(SELECT B.bid
                                                    FROM Boats B
                                                    WHERE B.color = 'red'))""")
for row in cursor:
    print(row)

#%% 3- ) Pind the names of sailors who have reserved boat nv,mber 103.(Correlated nested ile)

cursor = conn.execute("""SELECT S.snmame
                      FROM Sailors S
                      WHERE EXISTS (SELECT * 
                             FROM Reserves R
                             WHERE R.bid = 103 AND 
                             R.sid = S.sid)""")
for row in cursor:
    print(row)

#%% Compransionlar ile sorgu 

#%% 1-) Find sailors whose rating is better than some sailor called Horatio

cursor = conn.execute("""SELECT S.rating 
                      FROM Sailors S 
                      WHERE S.rating > (SELECT S2.rating 
                                            FROM Sailors S2
                                            WHERE S2.snmame = 'Horatio') """)
for row in cursor:
    print(row)

#%%  AGGREGATE OPERATORS ile sorgu ve bilgi alma 

#%% ortalama alma 

cursor = conn.execute("SELECT AVG (S.age) FROM Sailors S")

for row in cursor:
    print(row)

#%% Find the average age of sailors with a rating of 10. 

cursor = conn.execute("SELECT AVG (S.age) FROM Sailors S WHERE S.rating = 10")

for row in cursor:
    print(row)
    
#%% Max min operators 

cursor = conn.execute("SELECT S.snmame, MAX(S.age) FROM Sailors S")

for row in cursor:
    print(row)

#%% Count the nmnber of d'i.fferent sailor names.

cursor = conn.execute("SELECT COUNT (DISTINCT S.snmame) FROM Sailors S") 

for row in cursor:
    print(row)

#%% Find the names of sailors who are older than the oldest sailor with a rating of 10

cursor = conn.execute("""SELECT S.snmame 
                      FROM Sailors S 
                      WHERE S.age > (SELECT MAX(S2.age)
                      FROM Sailors S2 
                      WHERE S2.rating = 10)""")
for row in cursor:
    print(row)
    
#%% UNION, INTERSECT, AND EXCEPT

#%% 1- ) Find the names of sailors who have reserved a red 01' a green boat.

cursor = conn.execute("""SELECT S.snmame
                      FROM Sailors S, Reserves R, Boats B 
                      WHERE S.sid = R.sid AND R.bid = B.bid
                      AND(B.color = 'red' OR B.color = 'green')""")
for row in cursor:
    print(row)

#%% 2- ) Find the sids of all sailor's who have reserved red boats but not green boats.

cursor = conn.execute("""SELECT S.sid 
                      FROM Sailors S, Reserves R, Boats B
                      WHERE S.sid = R.sid AND R.bid = B.bid AND B.color = 'red'
                      EXCEPT
                      SELECT S2.sid
                      FROM Sailors S2, Reserves R2, Boats B2
                      WHERE S2.sid = R2.sid AND R2.bid = B2.bid AND B2.color = 'green'""")
for row in cursor:
    print(row)

#%% 3-)Bonus yeşil bot rezervasyonu yaptıran, 22 sidsine sahip olan yaşı 22 yaş üzerinde 
#kırmızı bot kiralamamış yaşı 40 üzeri olmayan verdiği rating 6 üzeri olan insanların adı 

cursor = conn.execute("""SELECT S.snmame 
                      FROM Sailors S, Reserves R, Boats B 
                      WHERE S.sid = R.sid AND R.bid = B.bid AND(B.color = 'green' AND 
                                                                S.sid = 22 AND S.age > 20 AND
                                                                S.rating > 5)
                      EXCEPT
                      SELECT S2.sid 
                      FROM Sailors S2, Reserves R2, Boats B2
                      WHERE S2.sid = R2.sid AND R2.bid = B2.bid AND(B2.color = 'red' AND S2.age > 40)""")
for row in cursor:
    print(row)