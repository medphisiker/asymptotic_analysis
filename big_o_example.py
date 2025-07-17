"""Графическая иллюстрация определения O-большое для квадратичной функции."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numpy.typing import NDArray

plt.figure(figsize=(14, 8))  # Настройка размера графика


def f(n: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Реальная сложность: квадратичная функция."""
    return 0.2 * n**2 + 3 * n + 15


def g(n: float | NDArray[np.float64]) -> float | NDArray[np.float64]:
    """Асимптотическая оценка: квадратичная функция."""
    return n**2


c = 0.75  # Константа для оценки сверху
n0 = 10  # Пороговое значение n

n = np.linspace(1, 20, 500)  # Диапазон значений n

# Построение графиков функций и оценки сверху
plt.plot(n, f(n), label=r"$f(n) = 0.2n^2 + 3n + 15$", lw=3, color="blue")
plt.plot(
    n,
    c * g(n),
    "--",
    label=rf"$c \cdot g(n) = {c}n^2$",
    lw=2.5,
    color="red",
)

# Визуализация порогового значения n0
plt.axvline(n0, color="green", linestyle=":", alpha=0.7, label=rf"Порог $n_0 = {n0}$")
plt.scatter(n0, f(n0), color="green", s=80, zorder=5, marker="o")
plt.annotate(
    rf"$f({n0}) = {float(f(n0)):.1f} < c\cdot g({n0}) = {float(c * g(n0)):.1f}$",
    (n0, float(f(n0))),
    xytext=(n0 - 4, float(f(n0)) + 10),
    arrowprops={"arrowstyle": "->"},
)

# Заштрихованная область, где выполняется условие O-большое
mask = (n >= n0) & (f(n) <= c * g(n))
plt.fill_between(
    n,
    f(n),
    c * g(n),
    where=list(mask),
    color="limegreen",
    alpha=0.2,
    label=rf"$f(n) \leq c \cdot g(n)$ для $n \geq n_0 = {n0}$",
)

# Оформление графика
plt.title(
    rf"$O(n^2)$: \exists c={c},\ n_0={n0}:$"
    r"$\forall n \geq n_0 \rightarrow f(n) \leq c n^2$",
    fontsize=16,
    pad=20,
)
plt.xlabel("n", fontsize=14)
plt.ylabel("Значение функции", fontsize=14)
plt.legend(loc="upper left", fontsize=10)
plt.xticks(np.arange(0, 21, 2))
plt.ylim(0, 160)
plt.grid(visible=True, alpha=0.3)

plt.tight_layout()
Path("plots").mkdir(parents=True, exist_ok=True)
plt.savefig("plots/big_o_notation.png", dpi=200)
