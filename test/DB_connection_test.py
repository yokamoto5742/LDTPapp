import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="fletapp",
        user="postgres",
        password="postgres"
    )
    print("データベースに接続できました。")
    conn.close()
except psycopg2.OperationalError as e:
    print("データベースに接続できませんでした。")
    print(e)