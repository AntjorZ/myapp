import matplotlib.pyplot as plt
import seaborn as sns

# Имитация данных мониторинга (количество запросов к маршрутам)
routes = ["GET /", "GET /status", "GET /data", "GET /stats"]
request_counts = [42, 15, 28, 5]
response_times_ms = [12, 8, 15, 10]

# Настройка стиля
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("Мониторинг Flask-приложения", fontsize=14, fontweight="bold")

# График 1: количество запросов
colors = sns.color_palette("Blues_d", len(routes))
axes[0].bar(routes, request_counts, color=colors)
axes[0].set_title("Количество запросов по маршрутам")
axes[0].set_xlabel("Маршрут")
axes[0].set_ylabel("Количество запросов")
axes[0].tick_params(axis="x", rotation=15)

for i, count in enumerate(request_counts):
    axes[0].text(i, count + 0.5, str(count), ha="center", fontsize=11)

# График 2: среднее время ответа
axes[1].bar(routes, response_times_ms, color=sns.color_palette("Oranges_d", len(routes)))
axes[1].set_title("Среднее время ответа (мс)")
axes[1].set_xlabel("Маршрут")
axes[1].set_ylabel("Время (мс)")
axes[1].tick_params(axis="x", rotation=15)

for i, t in enumerate(response_times_ms):
    axes[1].text(i, t + 0.2, f"{t} мс", ha="center", fontsize=11)

plt.tight_layout()
plt.savefig("requests_stats.png", dpi=150)
print("График сохранён: requests_stats.png")
plt.show()