from datetime import date


def calculate_issue_date_age(birth_date, issue_date):
    issue_date_age = issue_date.year - birth_date.year

    if issue_date.month < birth_date.month or (
            issue_date.month == birth_date.month and issue_date.day < birth_date.day):
        issue_date_age -= 1

    return issue_date_age


# メイン処理
if __name__ == "__main__":
    # 生年月日の入力
    birth_year = int(input("生まれた年を入力してください（例: 1990）: "))
    birth_month = int(input("生まれた月を入力してください（1-12）: "))
    birth_day = int(input("生まれた日を入力してください（1-31）: "))

    # 現在の日付を取得
    issue_date = date.today()

    # 生年月日のdate objectを作成
    birth_date = date(birth_year, birth_month, birth_day)

    # 年齢を計算
    age = calculate_issue_date_age(birth_date, issue_date)

    print(f"あなたの年齢は {age} 歳です。")
