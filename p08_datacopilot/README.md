# P08 — DataCopilot (Auto‑Analyst para CSV)

_EDA automático y generación de reportes en Markdown._

## Resumen

Soy Hugo Baghetti. DataCopilot es un script liviano en Python que toma un CSV, calcula estadísticas y genera un reporte en Markdown con un primer diagnóstico: columnas, nulos, distribuciones básicas y comentarios interpretativos.

## Por qué hice este proyecto

En equipos de datos, el cuello de botella inicial se repite: llega un CSV y se pierde tiempo en abrir notebooks y hacer lo mismo. Yo quería estandarizar ese primer vistazo con un reporte reproducible, versionable y fácil de compartir.

## Qué demuestra (en trabajo real)

- Automatización de EDA (sin notebooks gigantes).
- Producción de un artefacto portable (Markdown) útil para documentación y handoff.
- Enfoque reutilizable: funciona con datasets de minería, banca, TI, retail, etc.

## Estructura del proyecto

```text
p08_datacopilot/
├── data/
│   └── ejemplo_dataset.csv
├── reports/
│   └── reporte_datacopilot.md
├── notebooks/
│   └── p08_datacopilot_demo.ipynb
└── src/
    └── datacopilot.py
```

## Qué hace cada archivo

- `src/datacopilot.py`: CLI que ejecuta el análisis y genera el reporte.
- `data/ejemplo_dataset.csv`: dataset de ejemplo.
- `reports/`: salida de reportes Markdown.
- `notebooks/p08_datacopilot_demo.ipynb`: demo opcional.

## Instalación

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install pandas
```

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

python p08_datacopilot/src/datacopilot.py   --input "p08_datacopilot/data/ejemplo_dataset.csv"   --output "p08_datacopilot/reports/reporte_datacopilot.md"
```

## Entradas y salidas

- **Entrada**: cualquier CSV tabular con encabezados.
- **Salida**: un archivo Markdown con:
  - resumen general del dataset,
  - estadísticas numéricas,
  - valores faltantes,
  - cardinalidad de categóricas,
  - comentarios base.

## Metodología (resumen técnico)

- Identificación de columnas numéricas/categóricas.
- `describe()` para numéricas + conteos de nulos.
- Generación de Markdown estructurado para documentación.

## Resultados esperables / cómo interpretar

Resultado práctico: un reporte base coherente para cualquier dataset. Útil para triage, handoff, QA inicial y para iniciar un análisis más profundo con criterios.

## Notas y referencias técnicas

- EDA reproducible como práctica de ingeniería de datos.
- Reportes en Markdown como artefacto versionable en Git.

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
