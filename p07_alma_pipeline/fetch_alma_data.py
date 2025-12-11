import requests
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# URL: Catálogo pequeño y filtrado (ligero)
# ALMA proporciona un endpoint CSV basado en consultas
URL = (
    "https://almascience.eso.org/store/observations/alma-data-pub-01.csv"
)

OUT_FILE = DATA_DIR / "alma_sample.csv"

def fetch_small_dataset():
    try:
        print("Descargando dataset pequeño desde ALMA...")
        response = requests.get(URL, timeout=30)

        if response.status_code != 200:
            raise Exception(f"ALMA respondió con código {response.status_code}")

        with open(OUT_FILE, "wb") as f:
            f.write(response.content)

        print(f"Dataset guardado en: {OUT_FILE}")

    except Exception as e:
        print("\n⚠ ALMA no respondió correctamente.")
        print("Cargando dataset de respaldo didáctico.")

        # Dataset de respaldo minimalista (compatible con pipeline)
        backup = pd.DataFrame({
            "project_code": ["2019.1.00001.S", "2021.1.00423.S"],
            "ra": [150.25, 10.33],
            "dec": [-35.2, -72.11],
            "frequency": [230.5, 345.0],
            "resolution": [0.7, 0.4],
            "instrument": ["ALMA-12m", "ALMA-7m"]
        })
        backup.to_csv(OUT_FILE, index=False)
        print(f"Backup generado en {OUT_FILE}")
        print(f"Detalle error original: {e}")


if __name__ == "__main__":
    fetch_small_dataset()
