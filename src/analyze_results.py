#!/usr/bin/env python3
import pandas as pd, argparse, pathlib
import matplotlib.pyplot as plt

def load_any(path: pathlib.Path) -> pd.DataFrame:
    if path.suffix == '.parquet':
        try:
            return pd.read_parquet(path)
        except Exception:
            return pd.read_csv(path.with_suffix('.csv'))
    elif path.suffix == '.csv':
        return pd.read_csv(path)
    else:
        # try both
        if path.with_suffix('.parquet').exists():
            return pd.read_parquet(path.with_suffix('.parquet'))
        return pd.read_csv(path.with_suffix('.csv'))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--infile', required=True)
    ap.add_argument('--out', required=True)
    args = ap.parse_args()

    inpath = pathlib.Path(args.infile)
    outdir = pathlib.Path(args.out)
    outdir.mkdir(parents=True, exist_ok=True)

    df = load_any(inpath)

    # simple summaries and plots
    for var in ['x','y','z']:
        plt.figure()
        for name, g in df.groupby('scenario_name'):
            plt.plot(g['t'], g[var], alpha=0.8, label=name)
        plt.title(f'{var} over time by scenario')
        plt.xlabel('t'); plt.ylabel(var)
        try:
            plt.legend()
        except Exception:
            pass
        plt.savefig(outdir / f'{var}_by_scenario.png', bbox_inches='tight')
        plt.close()

    # peak z by scenario
    summary = df.groupby(['scenario_name'])['z'].agg(['max','mean','std']).reset_index()
    summary.to_csv(outdir / 'summary_peak_z.csv', index=False)
    print(f'Wrote figures and summary CSV to {outdir}')

if __name__ == '__main__':
    main()
