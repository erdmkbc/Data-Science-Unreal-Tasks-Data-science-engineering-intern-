# Inter_Tasks

## SQL Cheatset 

* DISTINCT: Python da .unique() karşılık gelir bir columnda eşsiz elemanları dizgiler.
* Primary key: eşsiz anahtar oluşturur.
* Foreign key: anahtarların bağlantılarını sağlar 
* EXCEPT : İki sorgu içinde ki kümelerin ayrık olanlarını ortaya çıkarır
* INTERSECT : İki farklı sorgu kümesinin ortak olan değerlerini dönderir union farklı olarak unique elemanları dönderir.
* UNION : Çekilen columnlarda yalnızca kesişim değerlerini tek bir kümede dönderir.
* Sqlite'ın bazı sürümleri foreign key desteklemez print(conn.execute("PRAGMA foreign_keys")) 
ile 1 veya 0 döndermeli
* IN : Lokasyon içerisinde değer çekmek için kullanılır.
* EXISTS : Nested sorgularda binary karar dönderir ve karmaşıklığı azaltır.
* ANY : Operatörü SQLite da yok bunun yerine genelde IN kullanılılıyor.
* MAX, COUNT, AVG gibi operatörlerle numerik analiz yapılabilmekte

 

