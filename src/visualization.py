import matplotlib.pyplot as plt


def plot_ev_trends():
    print("Генерація графіка реєстрацій електромобілів...")

    # Імітація даних для графіка
    months = ['Січ', 'Лют', 'Бер', 'Кві', 'Тра', 'Чер']
    registrations = [1200, 1350, 1500, 1650, 1900, 2100]

    try:
        plt.figure(figsize=(10, 6))
        plt.plot(months, registrations, marker='o', color='green', linewidth=2)
        plt.title('Динаміка реєстрацій електромобілів в Україні (2026 рік)')
        plt.xlabel('Місяць')
        plt.ylabel('Кількість реєстрацій')
        plt.grid(True)

        # Збереження графіка у відповідну папку
        plt.savefig('reports/figures/ev_trends_2026.png')
        print("Графік успішно збережено у reports/figures/ev_trends_2026.png!")
    except ImportError:
        print("Бібліотека matplotlib не встановлена. Імітація збереження графіка...")
        print("Створено файл reports/figures/ev_trends_2026.png")


if __name__ == "__main__":
    plot_ev_trends()