import sqlite3

# データベースに接続
conn = sqlite3.connect('ldtp_app.db')  # 'ldtp_app.db'を実際のデータベースファイル名に変更してください
cursor = conn.cursor()

# alembic_versionテーブルの内容を表示
print("Current alembic_version table contents:")
cursor.execute("SELECT * FROM alembic_version")
print(cursor.fetchall())

# 特定のリビジョンを削除
revision_to_delete = 'e0b9dc6f0d8a'  # 削除したいリビジョン番号
cursor.execute("DELETE FROM alembic_version WHERE version_num = ?", (revision_to_delete,))
conn.commit()

# 削除後のalembic_versionテーブルの内容を表示
print("\nAlembic_version table contents after deletion:")
cursor.execute("SELECT * FROM alembic_version")
print(cursor.fetchall())

# 接続を閉じる
conn.close()

print(f"\nRevision {revision_to_delete} has been deleted from the alembic_version table.")
