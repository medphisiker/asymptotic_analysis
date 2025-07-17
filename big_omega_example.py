"""Графическая иллюстрация определения Ω-большое для квадратичной функции."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

# Параметры графика
X_MIN = 0  # Минимальное значение по оси X
X_MAX = 20  # Максимальное значение по оси X
Y_MIN = 0  # Минимальное значение по оси Y
Y_MAX = 160  # Максимальное значение по оси Y
N_POINTS = 500  # Количество точек для построения

# Параметры асимптотического анализа
C = 0.2  # Константа для оценки снизу
N0 = 0  # Пороговое значение n

plt.figure(figsize=(14, 8))  # Настройка размера графика


def f(n: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Реальная сложность: квадратичная функция."""
    return 0.2 * n**2 + 3 * n + 15


def g(n: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Асимптотическая оценка: квадратичная функция."""
    return n**2


n = np.linspace(X_MIN, X_MAX, N_POINTS)  # Диапазон значений n

# Построение графиков функций и оценки снизу
plt.plot(n, f(n), label=r"$f(n) = 0.2n^2 + 3n + 15$", lw=3, color="blue")
plt.plot(
    n,
    C * g(n),
    "--",
    label=rf"$c \cdot g(n) = {C:.2f}n^2$",
    lw=2,
    color="red",
)

# Визуализация порогового значения n0
plt.axvline(N0, color="green", linestyle=":", alpha=0.7, label=rf"Порог $n_0 = {N0}$")
plt.scatter(N0, f(N0), color="green", s=80, zorder=5, marker="o")
plt.annotate(
    rf"$f({N0}) = {float(f(N0)):.1f}$",
    (N0, float(f(N0))),
    xytext=(N0 + 2, float(f(N0)) + 20),
    arrowprops={"arrowstyle": "->"},
)

# Заштрихованная область, где выполняется условие Ω-большое
plt.fill_between(
    n,
    f(n),
    C * g(n),
    where=list((n >= N0) & (f(n) >= C * g(n))),
    color="limegreen",
    alpha=0.2,
    label=rf"$f(n) \geq c \cdot g(n)$ для $n \geq n_0 = {N0}$",
)

# Оформление графика
plt.title(
    (
        rf"$\Omega(n^2):\ c={C:.2f},\ n_0={N0}:"
        r"\ \forall n \geq n_0 \rightarrow f(n) \geq c n^2$"
    ),
    fontsize=16,
    pad=20,
)
plt.xlabel("n", fontsize=14)
plt.ylabel("Значение функции", fontsize=14)
plt.legend(loc="upper left", fontsize=10)
plt.xticks(np.arange(X_MIN, X_MAX + 1, 2))
plt.ylim(Y_MIN, Y_MAX)
plt.grid(visible=True, alpha=0.3)

plt.tight_layout()
Path("plots").mkdir(parents=True, exist_ok=True)
plt.savefig("plots/big_omega_notation.png", dpi=200)
