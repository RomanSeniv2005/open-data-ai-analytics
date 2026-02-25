import pandas as pd
import os


def load_ev_data(filepath):
    """Функція для завантаження та первинної фільтрації даних про електромобілі."""
    print(f"Пошук файлу за шляхом: {filepath}")

    if os.path.exists(filepath):
        try:
            # У реальному проєкті тут ми б завантажували CSV:
            # df = pd.read_csv(filepath)
            print("Файл знайдено. Імітуємо завантаження даних у pandas DataFrame...")
            print("Фільтруємо дані за типом пального 'Електро'...")
            print("Дані успішно завантажено!")
            return True
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")
            return False
    else:
        print("Помилка: Файл не знайдено. Перевірте наявність датасету в data/raw/")
        return False


if __name__ == "__main__":
    # Шлях до файлу (відносно кореня репозиторію)
    load_ev_data("data/raw/vehicles_data.csv")