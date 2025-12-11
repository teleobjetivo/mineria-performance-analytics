from pathlib import Path

# Ruta base
BASE = Path("/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria")
P07 = BASE / "p07_alma_pipeline"

# Subcarpetas
folders = [
    P07,
    P07 / "data",
    P07 / "img",
    P07 / "notebooks"
]

for f in folders:
    f.mkdir(parents=True, exist_ok=True)

print("Estructura creada exitosamente:")
for f in folders:
    print(f" - {f}")
