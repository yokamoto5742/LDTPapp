import pandas as pd


def load_patient_data():
    date_columns = [0, 6]
    return pd.read_csv("pat.csv", encoding="shift_jis", header=None, parse_dates=date_columns)




patient_data = load_patient_data()
print(patient_data)
print(pd.to_datetime(patient_data.iloc[0, 0], format='%Y%m%d'))
print(patient_data.iloc[0, 6])
