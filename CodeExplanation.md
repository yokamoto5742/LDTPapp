# LDTPapp Code Explanation

このコードは、生活習慣病療養計画書の作成と管理を行うためのデスクトップアプリケーションを実装しています。
主な機能と構成要素は以下の通りです：

1. **データベース設計**:
   - `SQLAlchemy`を使用してORMを実装
   - 主なモデル: `PatientInfo`, `MainDisease`, `SheetName`, `Template`

2. **UIフレームワーク**:
   - `flet`ライブラリを使用してGUIを構築

3. **主要クラス**:
   - `TreatmentPlanGenerator`: 治療計画書の生成を担当
   - `TemplateManager`: テンプレートの管理を行う
   - `MyHandler`: Pat.csvファイル監視のためのハンドラ

4. **主要機能**:
   - Pat.csvファイルからの患者情報の取込み
   - 治療計画書の作成、編集、削除
   - テンプレートの管理と適用
   - CSVファイル形式のデータのインポート/エクスポート
   - 治療計画書のバーコード生成

5. **ユーザーインターフェース**:
   - メイン画面: 患者情報入力、履歴表示
   - 新規作成画面: 新しい治療計画書の作成
   - 編集画面: 既存の治療計画書の編集
   - テンプレート画面: テンプレートの編集

6. **主要関数**:
   - `create_ui()`: UIの構築
   - `load_patient_data()`: CSVファイルから患者データを読み込む
   - `create_treatment_plan()`: 治療計画を作成し、データベースに保存
   - `apply_template()`: 選択されたテンプレートを適用
   - `update_history()`: 履歴表示を更新

7. **その他の特徴**:
   - 設定ファイル（config.ini）を使用してアプリケーションの設定を管理
   - ファイル監視機能により、Pat.csvファイルの変更を検知
   - エラーハンドリングとユーザーへのフィードバック機能

## VERSION = "1.0.6" の更新内容

1. **バーコード生成機能の追加**:
   - `TreatmentPlanGenerator`クラスに`Code128`を使用したバーコード生成機能を追加
   - 生成されたバーコードを初回用と継続用の両シートに追加

2. **UI改善**:
   - テーマに基づいたボタンスタイルの作成（`create_theme_aware_button_style`関数）
   - 日付選択のためのカレンダーアイコンボタンの追加

3. **機能拡張**:
   - 操作マニュアルPDFを開くための`open_manual_pdf`関数の追加
   - CSVインポート時のファイル名チェック機能の追加

4. **エラーハンドリングの強化**:
   - 各種エラー時のSnackBarによるユーザーへのフィードバック機能の拡充

5. **コード構造の改善**:
   - `create_form_fields`関数の導入によるUI要素生成の整理
   - `on_tobacco_checkbox_change`関数によるチェックボックスの相互排他制御の追加

## クラスの詳細説明

1. **PatientInfo**
   - 患者情報を表すSQLAlchemyモデル
   - 属性: 患者ID、氏名、性別、生年月日、発行日、医師名など

2. **MainDisease**
   - 主病名を表すSQLAlchemyモデル
   - 属性: ID、名前

3. **SheetName**
   - 主病名に関連するシート名を表すSQLAlchemyモデル
   - 属性: ID、主病名ID、名前

4. **Template**
   - テンプレートを表すSQLAlchemyモデル
   - 属性: 主病名、シート名、目標、食事、運動の種類など

5. **TreatmentPlanGenerator**
   - 治療計画書を生成するクラス
   - メソッド:
     - `generate_plan()`: 患者情報を基に計画書を生成
     - `populate_common_sheet()`: Excelシートの共通情報にデータを出力

6. **TemplateManager**
   - テンプレートを管理するクラス
   - メソッド:
     - `get_template()`: 指定されたテンプレートを取得

7. **MyHandler**
   - ファイル監視のためのハンドラクラス
   - メソッド:
     - `on_deleted()`: Pat.csvファイル削除時の処理

## 主要関数の詳細説明

1. **create_ui(page)**
   - アプリケーションのUIを構築する関数
   - 引数: `page` (fletのPage)オブジェクト
   - 主な処理:
     - UIコンポーネントの初期化
     - イベントハンドラの設定
     - ページレイアウトの構成

2. **load_patient_data()**
   - CSVファイルから患者データを読み込む関数
   - 戻り値: エラーメッセージ（あれば）とpandasのDataFrame

3. **create_treatment_plan(p_id, doctor_id, doctor_name, department, department_id, patients_df)**
   - 新しい治療計画を作成し、データベースに保存する関数
   - 引数: 患者ID、医師氏名、診療科、患者データのDataFrame
   - 処理: 治療計画オブジェクトの作成、データベースへの保存、計画書の生成

4. **save_treatment_plan(p_id, doctor_id, doctor_name, department, department_id, patients_df)**
   - 治療計画をデータベースに保存する関数（計画書は生成しない）
   - 引数: `create_treatment_plan`と同じ

5. **apply_template(e=None)**
   - 選択されたテンプレートを現在の入力フィールドに適用する関数
   - 処理: データベースからテンプレートを取得し、各フィールドに値を設定

6. **save_template(e)**
   - 現在の入力内容をテンプレートとして保存する関数
   - 処理: 既存のテンプレートの更新

7. **update_history(filter_patient_id=None)**
   - 履歴表示を更新する関数
   - 引数: フィルタリングする患者ID（オプション）
   - 処理: データベースから履歴データを取得し、UIを更新

8. **on_patient_id_change(e)**
   - 患者IDが変更された時の処理を行う関数
   - 処理: 患者情報の読み込み、履歴の更新

9. **save_data(e)**
   - 編集された患者情報をデータベースに保存する関数
   - 処理: 現在の入力内容をデータベースに反映

10. **import_csv(file_path)**
    - CSVファイルからデータをインポートする関数
    - 処理: CSVファイルの読み込み、データのバリデーション、データベースへの保存

11. **export_to_csv(e)**
    - データベースの内容をCSVファイルにエクスポートする関数
    - 処理: データベースからデータを取得し、CSVファイルに書き出し

12. **open_manual_pdf(e)**
    - 操作マニュアルPDFを開く関数
    - 処理: 設定されたパスのPDFファイルを外部アプリケーションで開く

13. **create_theme_aware_button_style(page: ft.Page)**
    - テーマに基づいたボタンスタイルを作成する関数
    - 戻り値: ボタンスタイルの辞書

これらの更新により、アプリケーションの機能が拡張され、ユーザビリティが向上しています。バーコード生成機能の追加は、文書管理の効率化に貢献し、UI改善によってユーザーエクスペリエンスが向上しています。また、エラーハンドリングの強化により、アプリケーションの安定性が向上しています。
