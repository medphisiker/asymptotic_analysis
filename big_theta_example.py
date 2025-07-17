"""Графическая иллюстрация определения Θ-большое для квадратичной функции."""

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


n0 = 10  # Пороговое значение n
n = np.linspace(1, 20, 500)  # Диапазон значений n

# Автоматический подбор c1 и c2 для n >= n0
n_mask = n >= n0
ratios = f(n[n_mask]) / g(n[n_mask])
c1 = np.min(ratios)  # Минимальное значение c1
c2 = np.max(ratios)  # Максимальное значение c2

# Построение графиков функций и двух оценок
plt.plot(n, f(n), label=r"$f(n) = 0.2n^2 + 3n + 15$", lw=3, color="blue")
plt.plot(
    n,
    c1 * g(n),
    "--",
    label=rf"$c_1 \cdot g(n) = {c1:.2f}n^2$",
    lw=2,
    color="red",
)
plt.plot(
    n,
    c2 * g(n),
    "--",
    label=rf"$c_2 \cdot g(n) = {c2:.2f}n^2$",
    lw=2,
    color="green",
)

# Визуализация порогового значения n0
plt.axvline(n0, color="green", linestyle=":", alpha=0.7, label=rf"Порог $n_0 = {n0}$")
plt.scatter(n0, f(n0), color="green", s=80, zorder=5, marker="o")
plt.annotate(
    rf"$f({n0}) = {float(f(n0)):.1f}$",
    (n0, float(f(n0))),
    xytext=(n0 - 4, float(f(n0)) + 10),
    arrowprops={"arrowstyle": "->"},
)

# Заштрихованная область, где выполняется условие Θ-большое
plt.fill_between(
    n,
    c1 * g(n),
    c2 * g(n),
    where=list(n >= n0),
    color="limegreen",
    alpha=0.2,
    label=rf"$c_1 g(n) \leq f(n) \leq c_2 g(n)$ для $n \geq n_0 = {n0}$",
)

# Оформление графика
plt.title(
    rf"$\Theta(n^2)$: c_1={c1:.2f},\ c_2={c2:.2f},\ n_0={n0}:$"
    r"$\forall n \geq n_0 \rightarrow c_1 n^2 \leq f(n) \leq c_2 n^2$",
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
plt.savefig("plots/big_theta_notation.png", dpi=200)
