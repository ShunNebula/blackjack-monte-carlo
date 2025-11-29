import pandas as pd
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

stats = df.groupby("start_sum").agg({
    "result": "mean",
    "did_bust": "mean"
})
print(stats)

stats["result"].plot(kind="bar")
plt.show()