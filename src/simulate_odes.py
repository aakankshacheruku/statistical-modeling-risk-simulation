#!/usr/bin/env python3
import numpy as np, pandas as pd, argparse, yaml, pathlib
from scipy.integrate import solve_ivp

def lorenz(t, y, sigma=10.0, beta=8/3, rho=28.0):
    x, y_, z = y
    return [sigma*(y_-x), x*(rho - z) - y_, x*y_ - beta*z]

def run_scenarios(cfg):
    all_rows = []
    for sc in cfg.get('scenarios', []):
        y0 = sc.get('y0', [1.0, 1.0, 1.0])
        t_end = float(sc.get('t_end', 20.0))
        params = sc.get('params', {})
        sol = solve_ivp(lambda t, y: lorenz(t, y, **params), [0, t_end], y0, max_step=0.02)
        df = pd.DataFrame({'t': sol.t, 'x': sol.y[0], 'y': sol.y[1], 'z': sol.y[2]})
        df['scenario_name'] = sc.get('scenario_name', 'unnamed')
        for k, v in params.items():
            df[f'param_{k}'] = v
        all_rows.append(df)
    return pd.concat(all_rows, ignore_index=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scenarios', required=True, help='YAML scenario file')
    ap.add_argument('--out', required=True, help='output parquet or csv path')
    args = ap.parse_args()

    with open(args.scenarios) as f:
        cfg = yaml.safe_load(f)

    outpath = pathlib.Path(args.out)
    outpath.parent.mkdir(parents=True, exist_ok=True)

    df = run_scenarios(cfg)

    try:
        df.to_parquet(outpath)
        print(f'Wrote Parquet: {outpath}')
    except Exception as e:
        print(f'Parquet failed ({e}); writing CSV instead.')
        df.to_csv(outpath.with_suffix(".csv"), index=False)
        print(f'Wrote CSV: {outpath.with_suffix(".csv")}')

if __name__ == '__main__':
    main()
