from pathlib import Path
import csv
import random
import os

# Base del proyecto (carpeta raíz donde está este archivo)
BASE_DIR = Path(__file__).resolve().parent

# Carpetas del proyecto P08
P08_DIR = BASE_DIR / "p08_datacopilot"
DATA_DIR = P08_DIR / "data"
REPORTS_DIR = P08_DIR / "reports"
IMG_DIR = P08_DIR / "img"


def ensure_dirs():
    """Crea carpetas necesarias."""
    for d in [P08_DIR, DATA_DIR, REPORTS_DIR, IMG_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def generate_sample_csv():
    """Genera un CSV de muestra si no existe."""
    path = DATA_DIR / "demo_sales.csv"
    if path.exists():
        return path

    random.seed(42)
    categories = ["Electronics", "Home", "Sports", "Fashion", "Grocery"]
    channels = ["Online", "Store", "App"]
    regions = ["Norte", "Centro", "Sur"]
    returned_flags = [0, 1]

    rows = []
    order_id = 1000

    for day in range(1, 31):
        for _ in range(random.randint(20, 40)):
            order_id += 1
            rows.append({
                "order_id": order_id,
                "customer_id": random.randint(1, 200),
                "day": day,
                "category": random.choice(categories),
                "channel": random.choice(channels),
                "region": random.choice(regions),
                "amount": round(random.uniform(10, 500), 2),
                "returned": random.choices(returned_flags, weights=[0.9, 0.1])[0],
            })

    fieldnames = ["order_id", "customer_id", "day", "category", "channel", "region", "amount", "returned"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    return path


def create_datacopilot_script():
    """Crea el script principal datacopilot.py si no existe."""
    script_path = P08_DIR / "datacopilot.py"
    if script_path.exists():
        return script_path

    code = """#!/usr/bin/env python
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
REPORTS_DIR = BASE_DIR / "reports"
IMG_DIR = BASE_DIR / "img"


def ensure_dirs():
    for d in [DATA_DIR, REPORTS_DIR, IMG_DIR]:
        d.mkdir(parents=True, exist_ok=True)


def load_dataset(csv_path=None):
    ensure_dirs()
    if csv_path is None:
        csv_path = DATA_DIR / "demo_sales.csv"
    df = pd.read_csv(csv_path)
    return df


def auto_analyze(df):
    summary = {}
    summary["shape"] = df.shape
    summary["columns"] = list(df.columns)
    summary["dtypes"] = df.dtypes.astype(str).to_dict()
    summary["missing_perc"] = (df.isna().mean() * 100).round(2).to_dict()

    numeric_cols = df.select_dtypes(include="number").columns
    summary["numeric_summary"] = df[numeric_cols].describe().to_dict()
    
    outliers = {}
    for col in numeric_cols:
        s = df[col].dropna()
        q1 = s.quantile(0.25)
        q3 = s.quantile(0.75)
        iqr = q3 - q1
        lower = q1 - 1.5 * iqr
        upper = q3 + 1.5 * iqr
        outliers[col] = int(((s < lower) | (s > upper)).sum())

    summary["outliers"] = outliers
    return summary


def plot_basic(df):
    ensure_dirs()
    if "amount" in df.columns:
        col = "amount"
    else:
        col = df.select_dtypes(include="number").columns[0]

    plt.figure()
    df[col].hist(bins=30)
    plt.title(f"Distribución de {col}")
    plt.xlabel(col)
    plt.ylabel("Frecuencia")
    img_path = IMG_DIR / f"hist_{col}.png"
    plt.tight_layout()
    plt.savefig(img_path)
    plt.close()
    return img_path


def build_insight(summary):
    n_rows, n_cols = summary["shape"]
    missing = summary["missing_perc"]
    outliers = summary["outliers"]

    lines = []
    lines.append(f"El dataset contiene **{n_rows} filas** y **{n_cols} columnas**.")

    high_missing = [c for c, v in missing.items() if v > 5]
    if high_missing:
        cols = ", ".join(high_missing)
        lines.append(f"Columnas con alto porcentaje de datos faltantes (>5%): {cols}.")
    else:
        lines.append("No se detectan problemas significativos de datos faltantes.")

    strong_outliers = [c for c, v in outliers.items() if v > 0]
    if strong_outliers:
        cols = ", ".join(strong_outliers)
        lines.append(f"Outliers detectados en: {cols}.")

    return "\\n".join(lines)


def generate_markdown_report(summary, img_path):
    ensure_dirs()
    path = REPORTS_DIR / "auto_report.md"

    md = []
    md.append("# DataCopilot – Informe Automático")
    md.append("")
    md.append("## Resumen Estructural")
    md.append(f"- Filas: {summary['shape'][0]}")
    md.append(f"- Columnas: {summary['shape'][1]}")
    md.append("")

    md.append("## Tipos de datos")
    for col, dt in summary["dtypes"].items():
        md.append(f"- `{col}`: `{dt}`")
    md.append("")

    md.append("## Porcentaje de datos faltantes")
    for col, pct in summary["missing_perc"].items():
        md.append(f"- {col}: {pct}%")
    md.append("")

    md.append("## Outliers detectados")
    for col, v in summary["outliers"].items():
        md.append(f"- {col}: {v}")
    md.append("")

    md.append("## Insight Automático")
    md.append(build_insight(summary))
    md.append("")

    md.append("## Gráfico generado")
    md.append(f"- {img_path.name}")
    md.append("")

    path.write_text("\\n".join(md), encoding="utf-8")
    return path


def main():
    ensure_dirs()
    df = load_dataset()
    summary = auto_analyze(df)
    img = plot_basic(df)
    report = generate_markdown_report(summary, img)

    print("✅ Análisis completado")
    print(f"Dataset: {summary['shape']} (filas, columnas)")
    print(f"Reporte generado en: {report}")
    print(f"Imagen generada: {img}")


if __name__ == "__main__":
    main()
"""
    script_path.write_text(code, encoding="utf-8")
    os.chmod(script_path, 0o755)
    return script_path


def main():
    print("▶ Configurando P08 – DataCopilot Auto-Analyst...")
    ensure_dirs()
    csv = generate_sample_csv()
    script = create_datacopilot_script()
    print(f"CSV generado en: {csv}")
    print(f"Script principal en: {script}")
    print("✅ P08 listo para ejecutarse.")


if __name__ == "__main__":
    main()
