import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from simulation import play_game, strategy

N_GAMES = 10000
data = []

print(f"Запуск симуляции {N_GAMES} игр ...")

for _ in range(N_GAMES):
    res = play_game(strategy)
    data.append(res)

# print(data[0])

df = pd.DataFrame(data)

# Сводная таблица
pivot = df.pivot_table(
    index="player_sum", 
    columns="dealer_card", 
    values="result", 
    aggfunc="mean"
)

# pd.set_option('display.max_columns', None) # Чтобы показать все колонки
# pd.set_option('display.precision', 2)      # 2 знака после запятой
# print("\n--- WIN RATE HEATMAP (Smart Strategy) ---")
# print(pivot)

print(f"\nОбщий Win Rate: {df['result'].mean() * 100:.2f}%")

plt.figure(figsize=(10, 8))

# Рисуем тепловую карту
sns.heatmap(
    pivot, 
    annot=True,
    fmt=".2f",
    cmap="RdYlGn",
    center=0,
    linewidths=0.5,
    linecolor='black'
)

plt.title("Blackjack Strategy Win Rate")
plt.ylabel("Сумма игрока")
plt.xlabel("Карта дилера")

# Показать окно с графиком
plt.show()

# stats = df.groupby("start_sum").agg({
#     "result": "mean",
#     "did_bust": "mean"
# })
# print(stats)

# stats["result"].plot(kind="bar")
# plt.show()