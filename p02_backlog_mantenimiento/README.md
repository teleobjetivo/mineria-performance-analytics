# P02 — Backlog de Mantenimiento: Priorización de Órdenes de Trabajo

_Score explicable para ordenar OTs por criticidad, antigüedad y estado._

## Resumen

Soy Hugo Baghetti. Aquí construyo un análisis de backlog de órdenes de trabajo (OT) y un modelo simple de priorización para convertir un listado grande (y desordenado) en un ranking accionable.

## Por qué hice este proyecto

En la práctica, un backlog crece por falta de capacidad, mala planificación o gobernanza débil. El problema no es solo 'cuánto backlog hay', sino cómo decidir qué se atiende primero sin depender del ruido del día. Este proyecto muestra un score transparente y defendible.

## Qué demuestra (en trabajo real)

- Definición de reglas de negocio en un modelo numérico auditable.
- Cálculo de KPIs de backlog (tamaño, vencimiento, antigüedad) y visualización.
- Capacidad de entregar un artefacto listo para operación (ranking).

## Estructura del proyecto

```text
p02_backlog_mantenimiento/
├── data/
│   └── backlog_ordenes_trabajo.csv
├── notebooks/
│   └── p02_analisis_backlog.ipynb
├── img/
│   └── (figuras exportadas por el notebook)
└── README.md
```

## Qué hace cada archivo

- `data/backlog_ordenes_trabajo.csv`: backlog simulado tipo SAP PM/ERP (criticidad, fechas, estado, sistema, etc.).
- `notebooks/p02_analisis_backlog.ipynb`: KPIs + construcción del score de prioridad.
- `img/`: figuras para reporte/seguimiento.

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
cd p02_backlog_mantenimiento
jupyter notebook
```

Ejecutar:
- `notebooks/p02_analisis_backlog.ipynb`

## Entradas y salidas

- **Entrada**: `data/backlog_ordenes_trabajo.csv`.
- **Salidas**: tablas de KPIs en el notebook y figuras en `img/` (distribución por criticidad, edad del backlog, etc.).

## Metodología (resumen técnico)

- Cálculo de `dias_backlog` desde `fecha_creacion` a una fecha de corte.
- Identificación de OT vencidas por `fecha_vencimiento`.
- Score de prioridad combinando: criticidad OT, criticidad equipo, antigüedad (normalizada) y peso por estado.
- Ranking final para cola de atención.

## Resultados esperables / cómo interpretar

Lo esperable es obtener:
- Una foto clara del backlog y su envejecimiento.
- Un ranking que permite discutir capacidad, planificación y riesgo operacional.
- Un punto de partida para evolucionar a modelos más robustos (SLA real, costos, probabilidad de falla, impacto productivo).

## Notas y referencias técnicas

- Priorización multicriterio (scoring) y explicabilidad como requisito operacional.
- Gestión de backlog en mantenimiento: antigüedad + criticidad + vencimiento como señales base.

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
