from pathlib import Path
import csv
import random
import datetime as dt


BASE_DIR = Path(__file__).parent


def ensure_dirs(path: Path):
    path.mkdir(parents=True, exist_ok=True)


# ---------- P04: Tickets de soporte TI ----------

def create_p04():
    project_dir = BASE_DIR / "p04_tickets_soporte"
    data_dir = project_dir / "data"
    ensure_dirs(data_dir)

    readme = project_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            "# P04 – Prioridad de tickets de soporte TI\n\n"
            "Este proyecto simula tickets de soporte (tipo mesa de ayuda / Jira) para:\n"
            "- Preparar los datos (fechas, SLA, estado).\n"
            "- Calcular un score de prioridad.\n"
            "- Generar un listado de tickets priorizados.\n\n"
            "Los datos simulados se guardan en `data/tickets_soporte_raw.csv`.\n",
            encoding="utf-8"
        )

    raw_csv = data_dir / "tickets_soporte_raw.csv"
    if not raw_csv.exists():
        categorias = ["Correo", "Impresora", "VPN", "Aplicación interna", "SAP", "Red", "Accesos"]
        prioridades = ["Baja", "Media", "Alta", "Crítica"]
        estados = ["Abierto", "En curso", "Resuelto", "Cerrado"]
        analistas = ["Analista 1", "Analista 2", "Analista 3", "Analista 4"]
        canales = ["Portal", "Correo", "Teléfono"]

        start_date = dt.date(2025, 1, 1)

        with raw_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "ticket_id",
                "fecha_creacion",
                "fecha_cierre",
                "categoria",
                "prioridad",
                "estado",
                "asignado_a",
                "canal",
                "sla_vencido"
            ])

            for i in range(1, 61):
                fecha_creacion = start_date + dt.timedelta(days=random.randint(0, 60))
                estado = random.choice(estados)

                if estado in ["Resuelto", "Cerrado"]:
                    dias = random.randint(0, 10)
                    fecha_cierre = fecha_creacion + dt.timedelta(days=dias)
                else:
                    fecha_cierre = ""

                prioridad = random.choice(prioridades)
                categoria = random.choice(categorias)
                asignado = random.choice(analistas)
                canal = random.choice(canales)

                if estado in ["Resuelto", "Cerrado"] and fecha_cierre:
                    delta = (fecha_cierre - fecha_creacion).days
                    sla_vencido = "Sí" if (prioridad in ["Alta", "Crítica"] and delta > 2) else "No"
                else:
                    sla_vencido = random.choice(["Sí", "No"])

                writer.writerow([
                    f"T-{i:04d}",
                    fecha_creacion.isoformat(),
                    fecha_cierre.isoformat() if fecha_cierre else "",
                    categoria,
                    prioridad,
                    estado,
                    asignado,
                    canal,
                    sla_vencido
                ])


# ---------- P05: Créditos y riesgo ----------

def create_p05():
    project_dir = BASE_DIR / "p05_creditos_riesgo"
    data_dir = project_dir / "data"
    ensure_dirs(data_dir)

    readme = project_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            "# P05 – Segmentación de riesgo de créditos retail\n\n"
            "Este proyecto simula una cartera de créditos para:\n"
            "- Calcular variables derivadas (cuota, ratio cuota/ingreso, antigüedad).\n"
            "- Clasificar créditos en segmentos de riesgo (bajo/medio/alto) según reglas simples.\n\n"
            "Los datos simulados se guardan en `data/creditos_raw.csv`.\n",
            encoding="utf-8"
        )

    raw_csv = data_dir / "creditos_raw.csv"
    if not raw_csv.exists():
        segmentos = ["Retail", "PYME", "Corporativo"]
        regiones = ["RM", "V", "VIII", "II", "X", "XIII"]
        estados = ["Vigente", "Mora30", "Mora60", "Mora90"]

        with raw_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "credito_id",
                "cliente_id",
                "segmento",
                "monto_credito",
                "plazo_meses",
                "tasa_interes_anual",
                "region",
                "ingreso_mensual",
                "antiguedad_cliente_anios",
                "estado"
            ])

            for i in range(1, 81):
                segmento = random.choice(segmentos)
                region = random.choice(regiones)
                estado = random.choices(
                    estados,
                    weights=[0.7, 0.15, 0.10, 0.05],
                    k=1
                )[0]

                monto = random.randint(1_000_000, 20_000_000)
                plazo = random.choice([12, 24, 36, 48, 60])
                tasa = random.choice([0.10, 0.12, 0.15, 0.18])
                ingreso = random.randint(400_000, 3_000_000)
                antiguedad = round(random.uniform(0.1, 15.0), 1)

                writer.writerow([
                    f"CRED-{i:04d}",
                    f"CLI-{random.randint(1, 200):04d}",
                    segmento,
                    monto,
                    plazo,
                    tasa,
                    region,
                    ingreso,
                    antiguedad,
                    estado
                ])


# ---------- P06: Condiciones de cielo profundo ----------

def create_p06():
    project_dir = BASE_DIR / "p06_cielo_profundo"
    data_dir = project_dir / "data"
    ensure_dirs(data_dir)

    readme = project_dir / "README.md"
    if not readme.exists():
        readme.write_text(
            "# P06 – Ranking de noches para cielo profundo\n\n"
            "Este proyecto simula condiciones de cielo (seeing, SQM, nubosidad, fase lunar)\n"
            "en distintas ubicaciones (Santiago, Pochoco, Elqui, Atacama costero) para:\n"
            "- Calcular un score de calidad de cielo.\n"
            "- Generar un ranking de noches y ubicaciones.\n\n"
            "Los datos simulados se guardan en `data/condiciones_cielo.csv`.\n",
            encoding="utf-8"
        )

    raw_csv = data_dir / "condiciones_cielo.csv"
    if not raw_csv.exists():
        ubicaciones = ["Santiago", "Pochoco", "Valle del Elqui", "Atacama costero"]
        start_date = dt.date(2025, 1, 1)

        with raw_csv.open("w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([
                "fecha",
                "ubicacion",
                "seeing_arcsec",
                "sqm_mag",
                "nubes_pct",
                "humedad_pct",
                "fase_lunar_pct",
                "apto_cielo_profundo"
            ])

            for i in range(0, 60):
                fecha = start_date + dt.timedelta(days=i)
                for ubicacion in ubicaciones:
                    seeing = round(random.uniform(0.7, 3.0), 2)
                    sqm = round(random.uniform(18.0, 21.8), 2)
                    nubes = random.randint(0, 100)
                    humedad = random.randint(10, 90)
                    fase_lunar = random.randint(0, 100)

                    apto = (
                        seeing < 1.8 and
                        sqm > 20.5 and
                        nubes < 40 and
                        fase_lunar < 40
                    )

                    writer.writerow([
                        fecha.isoformat(),
                        ubicacion,
                        seeing,
                        sqm,
                        nubes,
                        humedad,
                        fase_lunar,
                        "Sí" if apto else "No"
                    ])


def main():
    print("Creando P04 (tickets soporte)...")
    create_p04()
    print("OK P04")

    print("Creando P05 (créditos riesgo)...")
    create_p05()
    print("OK P05")

    print("Creando P06 (cielo profundo)...")
    create_p06()
    print("OK P06")

    print("Listo: p04_tickets_soporte, p05_creditos_riesgo y p06_cielo_profundo creados.")


if __name__ == "__main__":
    main()
