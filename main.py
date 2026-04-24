import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
from distributions import DISTRIBUTIONS

SAMPLE_SIZES = [10, 100, 1_000, 10_000]

FILENAMES = {
    "Uniform (int)":  "uniform_int",
    "Uniform (real)": "uniform_real",
    "Normal":         "normal",
    "Exponential":    "exponential",
    "Poisson":        "poisson",
}

SUPTITLES = {
    "Uniform (int)":  "Uniform (int) [20, 40]",
    "Uniform (real)": "Uniform (real) [2.0, 3.0]",
    "Normal":         "Normal (μ=0, σ=0.5)",
    "Exponential":    "Exponential (mean=4)",
    "Poisson":        "Poisson (λ=5)",
}

def theo_curve(name, x_vals):
    if name == "Uniform (int)":
        dist = stats.randint(20, 41)
        xs = list(range(20, 41))
        return xs, dist.pmf(xs)
    if name == "Uniform (real)":
        dist = stats.uniform(loc=2.0, scale=1.0)
        return x_vals, dist.pdf(x_vals)
    if name == "Normal":
        dist = stats.norm(loc=0, scale=0.5)
        return x_vals, dist.pdf(x_vals)
    if name == "Exponential":
        dist = stats.expon(scale=4)
        return x_vals, dist.pdf(x_vals)
    if name == "Poisson":
        lo, hi = int(x_vals[0]), int(x_vals[-1])
        dist = stats.poisson(mu=5)
        xs = list(range(lo, hi + 1))
        return xs, dist.pmf(xs)


os.makedirs("histograms", exist_ok=True)
sns.set_theme(style="whitegrid", palette="muted")

samples_10k = {}

for name, meta in DISTRIBUTIONS.items():
    fn = meta["generator"]
    discrete = meta["discrete"]

    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes = axes.flatten()

    for i, n in enumerate(SAMPLE_SIZES):
        rng = np.random.default_rng(seed=3)
        data = fn(rng, n)

        print(f"Distribution: {name}, n={n}")
        if n <= 100:
            print(", ".join(str(x) for x in data))
        else:
            print(f"[{n} values generated]")

        if n == 10_000:
            samples_10k[name] = data

        ax = axes[i]
        if discrete:
            sns.histplot(data, discrete=True, stat="density",
                         color="steelblue", edgecolor="white", alpha=0.8, ax=ax)
        else:
            sns.histplot(data, bins=min(30, n // 2 or 1), stat="density",
                         kde=False, color="steelblue", edgecolor="white", alpha=0.8, ax=ax)

        if n == 10_000:
            if discrete:
                x_vals = np.arange(data.min(), data.max() + 1)
            else:
                x_vals = np.linspace(data.min(), data.max(), 300)
            xs, ys = theo_curve(name, x_vals)
            if discrete:
                ax.plot(xs, ys, 'o', color="crimson", markersize=5,
                        linestyle="none", label="Theoretical")
            else:
                ax.plot(xs, ys, color="crimson", linewidth=1.5, label="Theoretical")
            ax.legend(fontsize=8)

        ax.set_title(f"n = {n}")
        ax.set_xlabel("Value")
        ax.set_ylabel("Density")

        # Set specific ticks for Uniform (int) distribution
        if name == "Uniform (int)":
            ax.set_xticks([20, 25, 30, 35, 40])

    fig.suptitle(SUPTITLES[name], fontsize=13)
    plt.tight_layout()
    plt.savefig(f"histograms/{FILENAMES[name]}.png", dpi=150)
    plt.close()

print()
header = f"{'Distribution':<18} | {'Theo. Mean':>10} | {'Sample Mean':>11} | {'Theo. Std':>9} | {'Sample Std':>10}"
print(header)
print("-" * len(header))

for name, meta in DISTRIBUTIONS.items():
    data = samples_10k[name]
    print(
        f"{name:<18} | {meta['theo_mean']:>10.3f} | {data.mean():>11.4f} | {meta['theo_std']:>9.3f} | {data.std():>10.4f}"
    )
