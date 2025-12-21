# P10 — Analytics Readiness Framework (ARF)

_Marco de madurez analítica con scoring reproducible y mini‑paper versionable._

## Resumen

Soy Hugo Baghetti. Este proyecto define un marco de madurez analítica (ARF‑1 a ARF‑5) y lo aterriza en un score numérico con dimensiones medibles (personas, procesos, datos, tecnología, gobierno). El código genera figuras reproducibles y un documento tipo paper.

## Por qué hice este proyecto

En organizaciones, el problema no es 'hacer analítica' sino saber qué tan preparada está la empresa para sostenerla. Yo necesitaba un esquema claro para diagnosticar, discutir brechas y priorizar hoja de ruta (2–3 años) con lenguaje ejecutivo.

## Qué demuestra (en trabajo real)

- Traducción de estrategia a dimensiones medibles.
- Construcción de scoring y comunicación ejecutiva.
- Producción de artefactos: figuras + paper, versionables como código.

## Estructura del proyecto

```text
p10_analytics_readiness_framework/
├── paper/
│   ├── paper_p10.md
│   └── figures/
│       ├── arf_levels.png
│       └── arf_score_distribution.png
├── src/
│   └── generate_figures_p10.py
└── README.md
```

## Qué hace cada archivo

- `src/generate_figures_p10.py`: genera dataset simulado, calcula score y exporta figuras.
- `paper/paper_p10.md`: documento técnico (mini‑paper).
- `paper/figures/`: figuras generadas.

## Instalación

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install pandas matplotlib
```

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
python p10_analytics_readiness_framework/src/generate_figures_p10.py
```

Figuras:
- `p10_analytics_readiness_framework/paper/figures/arf_levels.png`
- `p10_analytics_readiness_framework/paper/figures/arf_score_distribution.png`

## Entradas y salidas

- **Entrada**: en la versión demo, el dataset es simulado dentro del script.
- **Salidas**: figuras en `paper/figures/` + contenido en `paper/paper_p10.md`.

## Metodología (resumen técnico)

- Definición de dimensiones y niveles (ARF‑1…ARF‑5).
- Score compuesto sobre dimensiones (ponderación explícita).
- Generación de figuras para comunicación ejecutiva.

## Resultados esperables / cómo interpretar

Resultado: un marco listo para discusión real (diagnóstico y roadmap). Es útil para consultoría interna, comités de datos y procesos de selección donde se evalúa pensamiento estratégico.

## Notas y referencias técnicas

- Frameworks de madurez: evaluación por dimensiones y niveles.
- Artefactos reproducibles: figuras generadas por código para evitar 'presentaciones sin trazabilidad'.

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
