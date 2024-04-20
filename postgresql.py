SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'name': 'fletapp'  # 事前に作成したデータベース名
})

print(SQLALCHEMY_DATABASE_URI)
