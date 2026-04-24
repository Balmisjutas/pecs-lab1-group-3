# Random Variable Generation Lab Report

This project demonstrates histogram convergence for five probability distributions using numpy's PCG64 PRNG (seed 3).

## Overview

Generates samples at sizes n ∈ {10, 100, 1000, 10000} for:
- Uniform (int): [20, 40]
- Uniform (real): [2.0, 3.0]
- Normal: μ=0, σ=0.5
- Exponential: mean=4
- Poisson: λ=5

## Running

```bash
uv run python main.py
```

Generates:
- Histograms in `histograms/` showing convergence to theoretical PDF/PMF
- Statistics table comparing sample and theoretical means/standard deviations

## Output

- `poisson.png`, `uniform_int.png`: Discrete distributions shown with PMF marker points at n=10000
- `normal.png`, `exponential.png`, `uniform_real.png`: Continuous distributions shown with PDF curves at n=10000
- Console output: Statistical validation table

