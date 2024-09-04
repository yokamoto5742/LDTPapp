from datetime import date


def calculate_age(birth_date, current_date):
    age = current_date.year - birth_date.year

    # 現在の日付が誕生日より前の場合、年齢を1歳引く
    if current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day):
        age -= 1

    return age


# メイン処理
if __name__ == "__main__":
    # 生年月日の入力
    birth_year = int(input("生まれた年を入力してください（例: 1990）: "))
    birth_month = int(input("生まれた月を入力してください（1-12）: "))
    birth_day = int(input("生まれた日を入力してください（1-31）: "))

    # 現在の日付を取得
    today = date.today()

    # 生年月日のdate objectを作成
    birth_date = date(birth_year, birth_month, birth_day)

    # 年齢を計算
    age = calculate_age(birth_date, today)

    print(f"あなたの年齢は {age} 歳です。")