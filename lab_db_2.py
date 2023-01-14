import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = '************'
database = 'lab_db'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT country, count(id) FROM artist GROUP by country
'''

query_2 = '''
SELECT genre_name, count(id) FROM genre GROUP by genre_name
'''

query_3 = '''
SELECT artist.name, sell.selling FROM sell inner join artist ON artist.id = sell.artist_id order by sell.selling
'''

conn = psycopg2.connect(user = username, password = password, dbname = database, host = host, port = port)

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    cur.execute(query_1)
    x = []
    y = []
    for row in cur:
        x.append(row[0]+"-[{}]".format(row[1]))
        y.append(row[1])
    plt.pie(y, labels=x)
    plt.title("Count of artists - country")
    plt.show()

    print('\n2.')
    x = []
    y = []
    cur.execute(query_2)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x,y)
    plt.title("Genre - count of artists")
    plt.xlabel("genre")
    plt.ylabel("count of artists")
    plt.show()

    print('\n3.')
    x = []
    y = []
    cur.execute(query_3)
    for row in cur:
        x.append(row[0])
        y.append(row[1])
    plt.bar(x, y)
    plt.title("paying")
    plt.xlabel("artist")
    plt.ylabel("paying")
    plt.show()