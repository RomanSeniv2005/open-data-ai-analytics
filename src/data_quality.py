import pandas as pd
from data_load import load_data


def clean_data(df):
    print("Початок очистки даних...")
    df_cleaned = df.dropna(how='all')

    initial_len = len(df_cleaned)
    df_cleaned = df_cleaned.drop_duplicates()
    print(f"Видалено {initial_len - len(df_cleaned)} дублікатів.")

    return df_cleaned


if __name__ == "__main__":
    df = load_data("data/raw/reestrtz01.01.2026.csv")
    if df is not None:
        clean_df = clean_data(df)