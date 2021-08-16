# Intern_Tasks

## SQL Cheatset 

### Genel metedoloji:

* Gruplanacak değişkenlerin belirlenmesi(zaman tabanlı gruplamalarda ay için EXTRACT(MONTH FROM DATETIME(TIMESTAMP_MICROS(event_timestamp), "Europe/"Istanbul")) kullanılmalı.)
* Gruplancıcak unique olmayan gruplandırma sorgularının OVER(PARTITION BY) ile gruplandırılması.
* 'CASE WHEN' yapısı ile labellanacak olan dataların labellanması. 
* Unique şekilde gruplandırma yapılacaksa group by kullanılmalı.
* _TABLE_SUFFIX ile datanın zaman, özellik vb bakımlardan istenilen şekilde filtrelenmesi.

* DISTINCT:
     Python da .unique() karşılık gelir bir columnda eşsiz elemanları dizgiler.

* Primary key: 
     Eşsiz anahtar oluşturur.

* Foreign key: 
     Anahtarların bağlantılarını sağlar 

* EXCEPT : 
     İki sorgu içinde ki kümelerin ayrık olanlarını ortaya çıkarır

* INTERSECT : 
     İki farklı sorgu kümesinin ortak olan değerlerini dönderir union farklı olarak unique elemanları dönderir.

* UNION : 
    Çekilen columnlarda yalnızca kesişim değerlerini tek bir kümede dönderir.

* Sqlite'ın bazı sürümleri foreign key desteklemez print(conn.execute("PRAGMA foreign_keys")) 
ile 1 veya 0 döndermeli.

* IN : 
    Lokasyon içerisinde değer çekmek için kullanılır.

* EXISTS  
    Nested sorgularda binary karar dönderir ve karmaşıklığı azaltır.

* ANY  
    Operatörü SQLite da yok bunun yerine genelde IN kullanılılıyor.

* MAX, COUNT, AVG gibi operatörlerle numerik analiz yapılabilmekte

* PARSE_DATE: Parseing işlemi yapılıyor ve verilen tarih normal type da return ediliyor(örneğin 2021-08-01).

* OVER(PARTITION BY) : Group by'dan farklı olarak unique değerler döndermez.

 
Referans kitap: 
Ramakrishnan - Database Management Systems 3rd Edition

# Data Science task

İlgili taskın raporlanması:
[Home_Credit_Risk_Kaggle.pdf](https://github.com/erdmkbc/Intern_Tasks/files/6941686/Home_Credit_Risk_Kaggle.pdf)


