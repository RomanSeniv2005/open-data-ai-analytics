import pandas as pd
import os


def load_data(filepath):
    print(f"Завантаження даних з {filepath}...")

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, filepath)

    if not os.path.exists(full_path):
        print(f"Файл не знайдено за шляхом: {full_path}")
        return None

    try:
        df = pd.read_csv(full_path, sep=';', low_memory=False)
        print(f"Успішно завантажено {len(df)} рядків!")

        fuel_cols = [col for col in df.columns if 'пальне' in col.lower() or 'fuel' in col.lower()]
        if fuel_cols:
            col_name = fuel_cols[0]
            df = df[df[col_name].astype(str).str.contains('ЕЛЕКТРО', case=False, na=False)]
            print(f"Після фільтрації залишилось {len(df)} електромобілів.")

        return df
    except Exception as e:
        print(f"Помилка завантаження: {e}")
        return None


if __name__ == "__main__":
    df = load_data("data/raw/reestrtz01.01.2026.csv")
    if df is not None:
        print("Перші 3 рядки датасету:")
        print(df.head(3))