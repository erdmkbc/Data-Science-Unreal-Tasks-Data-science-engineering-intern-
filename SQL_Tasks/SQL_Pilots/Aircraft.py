# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 11:27:14 2021

@author: erdmk
"""
#%% importing sqlite module 
import sqlite3

#%% databasein ayağa kaldırılmasi

conn = sqlite3.connect('task_2_sql.db')
conn.execute("PRAGMA foreign_keys = ON") # foreign keysin sqlite için aktif edilmesi
c = conn.cursor() 


#%% Flights

cursor = c.execute('''CREATE TABLE IF NOT EXISTS flights
             (no INTEGER INTEGER PRIMARY KEY,
              frm  TEXT,
              too  TEXT, 
              distance INTEGER,
              departs  TEXT,
              arrives  TEXT,
              price    REAL)''')

cursor = c.execute('''CREATE TABLE IF NOT EXISTS aircraft
             (aid  INTEGER INTEGER PRIMARY KEY,
              aname   TEXT,
              cruisingrange   TEXT)''')

cursor = c.execute('''CREATE TABLE IF NOT EXISTS employees
             (eid   INTEGER PRIMARY KEY,
              ename    TEXT,
              salary    TEXT)''')

cursor = c.execute('''CREATE TABLE IF NOT EXISTS certified
             (eid   INTEGER,  
              aid   INTEGER, 
              FOREIGN KEY (eid) REFERENCES employees (eid),
              FOREIGN KEY (aid) REFERENCES aircraft (aid))''')


#%% Inserting flights

c.execute("""INSERT INTO flights VALUES
            (1,'Bangalore','Mangalore',360,'10:45:00','12:00:00',10000)""")
            
c.execute("""INSERT INTO flights VALUES
            (2,'Bangalore','Delhi',5000,'12:15:00','04:30:00',25000)""")
            
c.execute("""INSERT INTO flights VALUES
            (3,'Bangalore','Mumbai',3500,'02:15:00','05:25:00',30000)""")
            
c.execute("""INSERT INTO flights VALUES
            (4,'Delhi','Mumbai',4500,'10:15:00','12:05:00',35000)""")
            
c.execute("""INSERT INTO flights VALUES
            (5,'Delhi','Frankfurt',18000,'07:15:00','05:30:00',90000)""")
            
c.execute("""INSERT INTO flights VALUES
            (6,'Bangalore','Frankfurt',19500,'10:00:00','07:45:00',95000)""")
            
c.execute("""INSERT INTO flights VALUES
            (7,'Bangalore','Frankfurt',17000,'12:00:00','06:30:00',99000)""")
            
conn.commit()

#%% Inserting flights aircraft

c.execute("""INSERT INTO aircraft VALUES
            (123,'Airbus',1000)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (302,'Boeing',5000)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (306,'Jet01',5000)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (378,'Airbus380',8000)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (456,'Aircraft',500)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (789,'Aircraft02',800)""")
            
c.execute("""INSERT INTO aircraft VALUES
            (951,'Aircraft03',1000)""")
conn.commit()

#%% 

c.execute("""INSERT INTO employees  VALUES
            (1,'Ajay',30000)""")
            
c.execute("""INSERT INTO employees  VALUES
            (2,'Ajith',85000)""")
            
c.execute("""INSERT INTO employees  VALUES
            (3,'Arnab',50000)""")
            
c.execute("""INSERT INTO employees  VALUES
            (4,'Harry',45000)""")
            
c.execute("""INSERT INTO employees  VALUES
            (5,'Ron',90000)""")
            
c.execute("""INSERT INTO employees  VALUES
            (6,'Josh',75000)""")
            
c.execute("""INSERT INTO employees VALUES
            (7,'Ram',100000)""")
            
conn.commit()

#%% 

conn.execute("PRAGMA foreign_keys = ON")

c.execute("""INSERT INTO certified   VALUES
            (1,123)""")
            
c.execute("""INSERT INTO certified   VALUES
            (2,123)""")
            
c.execute("""INSERT INTO certified   VALUES
            (1,302)""")
            
c.execute("""INSERT INTO certified   VALUES
            (5,302)""")
            
c.execute("""INSERT INTO certified   VALUES
            (7,302)""")
            
c.execute("""INSERT INTO certified   VALUES
            (1,306)""")
            
c.execute("""INSERT INTO certified  VALUES
            (2,306)""")

c.execute("""INSERT INTO certified  VALUES
            (1,378)""")
            
c.execute("""INSERT INTO certified  VALUES
            (2,378)""")
            
c.execute("""INSERT INTO certified  VALUES
            (4,378)""")

c.execute("""INSERT INTO certified  VALUES
            (6,456)""")

c.execute("""INSERT INTO certified  VALUES
            (3,456)""")

c.execute("""INSERT INTO certified  VALUES
            (5,789)""")

c.execute("""INSERT INTO certified  VALUES
            (6,789)""")

c.execute("""INSERT INTO certified  VALUES
            (3,951)""")

c.execute("""INSERT INTO certified  VALUES
            (1,951)""")

c.execute("""INSERT INTO certified  VALUES
            (1,789)""")

conn.commit()

#%% Sorgular 

#%% 1 - )  Find the names of aircraft such that all pilots certified to operate them earn more than
#$80,000.

cursor = conn.execute('''SELECT A.aname
                      FROM aircraft A, employees E
                      WHERE E.salary > 80.000''')

for row in cursor:
    print(row)

#%% 2 - ) For each pilot who is certified for more than three aircrafts,find the 
#eid and the maximum cruisingrange of the aircraft for which he/she is certified.

"""
İstenilen değerlerin select ile genel tanımı 
aid lerin eşleştirilmesi 
MAX cruisingrangelerin eid lere göre gruplandılması 
3 ve fazla olanların filtreye tabi tutulması
"""

cursor = conn.execute('''SELECT c.eid,MAX(A.cruisingrange)
                      FROM certified C,aircraft A 
                      WHERE C.aid=A.aid
                      GROUP BY C.eid
                      HAVING COUNT(*)>3''')
for row in cursor:
    print(row)
#%% 3-) Find the names of all pilots whose salary is less than the price of the cheapest route from 
#Delhi to Frankfurt.

"""
İstenilen değerlerin select ile genel tanımı 
Pilotların maaşlarının karşılaştırma yapılması 
Karşılaştırılmak istenen ifade için nested sorgu açılması 
İkinci katmanda ki sorgunun istenilen lokasyonlara göre en ucuzunun döndürülmesi.
"""

cursor = conn.execute("""SELECT E.ename 
                      FROM employees E
                      WHERE E.salary < (SELECT MIN(F.price) 
                                        FROM flights F
                                        WHERE F.frm = 'Delhi' AND F.too = 'Frankfurt')""")

for row in cursor:
    print(row)

#%% 4- ) For all aircraft with cmisingmnge over 1000 miles, find the name of the aircraft and the
#average salary of all pilots certified for this aircraft.

"""
Aircraft isminin ve istenilen maaşın ortalamasının tanımlanması
id lerin birleştirilmesi 
gerekli filtrenin uygulanması 
çoklu gösterim için GROUP BY ın kullanımlması
"""

cursor = conn.execute("""SELECT A.aname, AVG(E.salary)
                      FROM aircraft A, certified C, employees E
                      WHERE A.aid = C.aid AND E.eid = C.eid AND A.cruisingrange > 1000
                      GROUP BY A.aid,A.aname
                      """)

for row in cursor:
    print(row)

#%% 5- ) Find the names of pilots certified for some Boeing aircraft
"""
İstenilen değerin tanımının yapılması 
e-> c -> a -> c adımı takip edilerek tablelar arası bağlantının sağlanması
filtrenin yapılması
"""

cursor = conn.execute("""SELECT E.ename
                      FROM employees E, aircraft A, certified C
                      WHERE A.aid = C.aid AND E.eid = C.eid AND A.aname = 'Boeing'""")

for row in cursor:
    print(row)

#%% 6- ) Print the enames of pilots who can operate planes with cruisingmnge greater than 3000
#miles but are not certified on any Boeing aircraft

"""
İstenen displain tanımlanması 
table lar arası bağlatının kurulması 
ilgili filtrenin uygulanması
EXCEPT ile aynı şekilde haraket edilerek iki kümeden ayrık olanların display edilmesi
"""
cursor = conn.execute("""SELECT E.ename
                      FROM employees E, aircraft A, certified C
                      WHERE A.aid = C.aid AND E.eid = C.eid AND A.cruisingrange > 3000
                      EXCEPT
                      SELECT E2.ename 
                      FROM employees E2, aircraft A2, certified C2
                      WHERE A2.aid = C2.aid AND E2.eid = C2.eid AND A2.aname = 'Boeing' """)

for row in cursor:
    print(row)

#%% 7-) Print the names of employees who are certified only on aircrafts with cruising range
#longer than 1000 miles.

cursor = conn.execute("""SELECT E.ename 
                      FROM employees E, aircraft A, certified C
                      WHERE A.aid = C.aid AND E.eid = C.eid AND A.cruisingrange > 1000""")

for row in cursor:
    print(row)
#%% 





