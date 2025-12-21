# P07 — ALMA Deep‑Sky Data Pipeline (Chile)

_Ingesta (API + fallback), limpieza, visualización y métricas sobre datos astronómicos._

## Resumen

Soy Hugo Baghetti. En este proyecto implemento un pipeline educativo para explorar datos científicos asociados a ALMA. El flujo intenta consumir una API pública y, si no está disponible, cae a un dataset didáctico para mantener reproducibilidad.

## Por qué hice este proyecto

Necesitaba un ejemplo que uniera ingeniería (pipeline) con ciencia aplicada, sin depender de infraestructura pesada. El valor es doble: (1) mostrar diseño modular y robusto, (2) entregar un recurso de docencia que funcione online/offline.

## Qué demuestra (en trabajo real)

- Diseño modular (ingesta → estandarización → limpieza → visualización → métricas).
- Manejo de fallas (fallback) y reproducibilidad.
- Capacidad de llevar datos científicos a un formato analítico estándar.

## Estructura del proyecto

```text
p07_alma_pipeline/
├── data/
│   └── alma_sample.csv
├── plots/
│   └── (salidas gráficas)
├── p07_alma_pipeline/
│   ├── fetch_alma_data.py
│   ├── ingest.py
│   ├── clean.py
│   ├── plot_maps.py
│   └── metrics.py
└── README.md
```

## Qué hace cada archivo

- `fetch_alma_data.py`: descarga desde API; si falla, genera/usa un dataset reproducible.
- `ingest.py`: unifica esquema/columnas y prepara dataset analítico.
- `clean.py`: filtros de calidad y normalización.
- `plot_maps.py`: visualizaciones exploratorias.
- `metrics.py`: métricas resumidas del catálogo.
- `data/alma_sample.csv`: dataset de ejemplo.
- `plots/`: imágenes de salida.

## Instalación

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install pandas matplotlib requests
```

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

# Ejecutar pipeline (módulos)
python p07_alma_pipeline/p07_alma_pipeline/fetch_alma_data.py
python p07_alma_pipeline/p07_alma_pipeline/ingest.py
python p07_alma_pipeline/p07_alma_pipeline/clean.py
python p07_alma_pipeline/p07_alma_pipeline/plot_maps.py
python p07_alma_pipeline/p07_alma_pipeline/metrics.py
```

## Entradas y salidas

- **Entradas**: API pública (si está disponible) o `data/alma_sample.csv`.
- **Salidas**: dataset limpio (según módulos) y figuras en `plots/`.

## Metodología (resumen técnico)

- Arquitectura por etapas (cada módulo hace una cosa y lo hace bien).
- Fallback para garantizar ejecución reproducible.
- Visualización exploratoria y métricas de catálogo como capa inicial para análisis posterior (ML, clasificación, etc.).

## Resultados esperables / cómo interpretar

Este proyecto está pensado como base. Lo más importante es el diseño: modular, reproducible y listo para extender.

## Notas y referencias técnicas

- Pipelines científicos: trazabilidad y reproducibilidad.
- Patrón de 'fallback dataset' para docencia y demostraciones técnicas sin dependencia de servicios externos.

## Contacto & Presencia Online

- Email: teleobjetivo.boutique@gmail.com
- Web: www.teleobjetivo.cl
- Instagram: @tele.objetivo
- GitHub: https://github.com/teleobjetivo

**Rol**: University Lecturer (Data & Analytics) · Science Communicator · Research Collaborator

---

## Related Work (Author)

- P01 — Asset Health Analytics for Mining Operations  
- P02 — Maintenance Backlog Prioritization  
- P03 — Failure Pattern Analysis for Conveyor Systems  
- P04 — IT Support Ticket Scoring  
- P05 — Credit Risk Segmentation  
- P06 — Multi-Criteria Scoring for Astrophotography Planning  
- P07 — Scientific Data Pipelines (ALMA-inspired)  
- P08 — Automated Exploratory Data Analysis (DataCopilot)  
- P09 — Static Executive KPI Dashboards  
- P10 — Analytics Readiness Framework  

---

---

## Technical References & Background

1. Han, J., Kamber, M., & Pei, J. (2012). *Data Mining: Concepts and Techniques*. Morgan Kaufmann.
2. Provost, F., & Fawcett, T. (2013). *Data Science for Business*. O’Reilly Media.
3. CRISP-DM 1.0 — Cross-Industry Standard Process for Data Mining.
4. ISO/IEC 25010 — Systems and Software Quality Models.
5. Basel Committee on Banking Supervision. *Principles for the Management of Credit Risk*.

---

---

## Author & Professional Profile

**Hugo Baghetti**  
Applied Analytics Researcher & Scientific Communicator  

**Areas:** Data Analytics · Decision Support Systems · Applied AI · Data Engineering  

**Contact**
- Email: teleobjetivo.boutique@gmail.com  
- Web: https://www.teleobjetivo.cl  
- GitHub: https://github.com/teleobjetivo  
- Instagram (visual science communication): https://www.instagram.com/tele.objetivo  

---
