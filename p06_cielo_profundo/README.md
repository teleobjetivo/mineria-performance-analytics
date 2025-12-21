# P06 — Score de Calidad de Noche para Cielo Profundo (Astrofotografía)

_Modelo simple para priorizar noches observables usando variables físicas._

## Resumen

Soy Hugo Baghetti. Este proyecto prioriza noches para astrofotografía de cielo profundo construyendo un score (0–100) a partir de variables típicas: oscuridad, seeing, nubosidad, humedad y fase lunar.

## Por qué hice este proyecto

Planificar salidas astronómicas sin un criterio cuantitativo es perder tiempo y combustible. Yo quería una regla clara para escoger 'las mejores noches' y, de paso, demostrar que el mismo patrón se aplica a problemas corporativos: priorización de activos, riesgos, iniciativas o mantenimiento.

## Qué demuestra (en trabajo real)

- Normalización y ponderación de variables para un score interpretable.
- Ranking (top‑N) y visualización para decisión.
- Capacidad de traducir señales físicas a un indicador operativo (sin complicar innecesariamente).

## Estructura del proyecto

```text
p06_cielo_profundo/
├── data/
│   └── (dataset de condiciones nocturnas)
├── notebooks/
│   └── p06_analisis_cielo_profundo.ipynb
├── img/
│   └── score_calidad_noche_top.png
└── README.md
```

## Qué hace cada archivo

- `notebooks/p06_analisis_cielo_profundo.ipynb`: cálculo del score y ranking.
- `img/score_calidad_noche_top.png`: gráfico de las mejores noches.
- `data/`: dataset de ejemplo con variables meteorológicas/astronómicas (estructura documentada en el notebook).

## Instalación

> Asumo un entorno virtual `.venv` creado en la raíz del portafolio.

```bash
cd <repository-root>
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install -U pip
pip install pandas numpy matplotlib jupyter
```

Si el proyecto usa otros paquetes, los indico en su sección de ejecución.

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
cd p06_cielo_profundo
jupyter notebook
```

Ejecutar:
- `notebooks/p06_analisis_cielo_profundo.ipynb`

## Entradas y salidas

- **Entrada**: dataset en `data/` con variables de condiciones.
- **Salida**: ranking top‑N en el notebook y figura `img/score_calidad_noche_top.png`.

## Metodología (resumen técnico)

- Normalización de variables (para compararlas en una escala común).
- Definición de pesos (ponderación) según impacto en observación.
- Score final 0–100 y ranking descendente.
- Export visual simple para reportar las mejores noches.

## Resultados esperables / cómo interpretar

Resultado práctico: un top‑N de noches con mayor probabilidad de sesión exitosa. En contexto laboral, es un ejemplo claro de cómo construir un score explicable con múltiples variables (multi‑criteria scoring).

## Notas y referencias técnicas

- Multi‑criteria scoring (normalización + ponderación).
- Variables típicas de calidad de cielo: seeing, nubes, humedad, fase lunar, oscuridad.

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
