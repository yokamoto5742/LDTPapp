import pandas as pd

def load_patient_data():
    column_names = ['発行日', 'column2', '患者ID', '氏名', 'カナ', '性別', '生年月日', 'column8', 'column9', '医師ID', '医師名', 'column12', 'column13', 'column14', '診療科']
    date_columns = [0, 6]
    dtype_dict = {'患者ID': str, '医師ID': str}
    try:
        return pd.read_csv("pat.csv", encoding="shift_jis", header=None, names=column_names, parse_dates=date_columns, dtype=dtype_dict)
    except Exception as e:
        print(f"Error occurred while reading the CSV file: {str(e)}")
        return None

df = load_patient_data()

if df is not None:
    print(df.head())
    patient_data = load_patient_data()
    print(patient_data.head())
    print(patient_data.dtypes)
    print(patient_data)

else:
    print("Failed to load the patient data.")
