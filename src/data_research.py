import pandas as pd
import matplotlib.pyplot as plt
import os


def test_hypothesis_1(df, base_dir):
    print("\n🚀 Перевірка Гіпотези 1: Частка електромобілів серед нових авто...")

    # Перевіряємо, чи є стандартні колонки МВС
    required_cols = ['KIND', 'OPER_NAME', 'FUEL']
    for col in required_cols:
        if col not in df.columns:
            print(f"❌ Не знайдено колонку {col}. Доступні: {df.columns.tolist()}")
            return

    # 1. Залишаємо тільки ЛЕГКОВІ авто (використовуємо точну колонку KIND)
    df_passenger = df[df['KIND'].astype(str).str.contains('ЛЕГКОВИЙ', case=False, na=False)]

    # 2. Залишаємо тільки ПЕРВИННУ реєстрацію (використовуємо точну колонку OPER_NAME)
    df_new = df_passenger[df_passenger['OPER_NAME'].astype(str).str.contains('ПЕРВИННА', case=False, na=False)]

    total_new_cars = len(df_new)

    # 3. Рахуємо електромобілі серед них (використовуємо точну колонку FUEL)
    ev_cars = len(df_new[df_new['FUEL'].astype(str).str.contains('ЕЛЕКТРО', case=False, na=False)])

    if total_new_cars > 0:
        ev_share = (ev_cars / total_new_cars) * 100
        print("-" * 40)
        print(f"🚗 Всього вперше зареєстрованих легкових авто: {total_new_cars}")
        print(f"⚡ З них електромобілів (EV): {ev_cars}")
        print(f"📊 Частка електромобілів: {ev_share:.2f}%")
        print("-" * 40)

        if ev_share >= 25:
            print("✅ ВИСНОВОК: Гіпотеза ПІДТВЕРДЖЕНА! Частка становить 25% або більше.")
        else:
            print("❌ ВИСНОВОК: Гіпотеза СПРОСТОВАНА! Частка менша за 25%.")

        # Візуалізація
        labels = ['Електромобілі (EV)', 'ДВЗ та Гібриди']
        sizes = [ev_cars, total_new_cars - ev_cars]
        colors = ['#2ca02c', '#7f7f7f']
        explode = (0.1, 0)

        plt.figure(figsize=(8, 6))
        plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
        plt.title('Частка нових електромобілів на ринку України')

        save_path = os.path.join(base_dir, 'reports/figures/hypothesis_1_pie.png')
        plt.savefig(save_path)
        print(f"🖼️ Графік успішно збережено у: reports/figures/hypothesis_1_pie.png")
    else:
        print("❌ Немає даних для аналізу після фільтрації.")


def plot_top_brands(df, base_dir):
    print("\n📊 Генерація графіка ТОП-10 марок для електромобілів...")

    if 'FUEL' in df.columns and 'BRAND' in df.columns:
        # Залишаємо тільки електромобілі
        df_ev = df[df['FUEL'].astype(str).str.contains('ЕЛЕКТРО', case=False, na=False)]

        # Рахуємо ТОП-10
        top_brands = df_ev['BRAND'].value_counts().head(10)

        plt.figure(figsize=(12, 6))
        top_brands.plot(kind='bar', color='#2ca02c')
        plt.title('ТОП-10 найпопулярніших марок електромобілів в Україні')
        plt.xlabel('Марка електромобіля')
        plt.ylabel('Кількість реєстрацій')
        plt.xticks(rotation=45)
        plt.tight_layout()

        save_path = os.path.join(base_dir, 'reports/figures/top_ev_brands_real.png')
        plt.savefig(save_path)
        print(f"🖼️ Графік успішно збережено у: reports/figures/top_ev_brands_real.png")
    else:
        print("❌ Не знайдено колонки FUEL або BRAND.")


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filepath = os.path.join(base_dir, "data/raw/reestrtz01.01.2026.csv")

    print("Завантаження даних (це може зайняти кілька секунд)...")
    if os.path.exists(filepath):
        df_main = pd.read_csv(filepath, sep=';', low_memory=False)
        test_hypothesis_1(df_main, base_dir)
        plot_top_brands(df_main, base_dir)
    else:
        print(f"❌ Файл не знайдено: {filepath}")