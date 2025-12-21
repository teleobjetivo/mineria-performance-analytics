# P01 — Salud de Activos (CAEX): Disponibilidad, MTBF y MTTR

_Análisis reproducible de órdenes de trabajo estilo SAP PM para gestión de mantenimiento._

## Resumen

Soy Hugo Baghetti. En este proyecto simulo y analizo la salud de una flota de camiones de extracción (CAEX) en una faena ficticia. A partir de un dataset tabular (tipo extracción SAP PM), construyo indicadores operacionales y visualizaciones que permiten priorizar focos de mejora de confiabilidad.

## Por qué hice este proyecto

En operaciones reales, la disponibilidad se pierde por pocas causas recurrentes y por un subconjunto de equipos. Quise demostrar una forma simple, auditable y portable de pasar de 'datos de OT' a decisiones: qué equipo duele más, qué causas explican el mayor impacto y cómo medir MTBF/MTTR para comparar y gestionar.

## Qué demuestra (en trabajo real)

- Modelado analítico a partir de eventos (OT) y cálculo de KPIs clásicos de mantenimiento.
- Capacidad de estructurar un pipeline simple (carga → limpieza → agregación → métricas → visualización).
- Enfoque explicable: resultados listos para convertirse en dashboard (Power BI/Looker/QuickSight) o rutina mensual.

## Estructura del proyecto

```text
p01_salud_activos_camiones/
├── data/
│   └── camiones_mina_mantenimiento.csv
├── notebooks/
│   └── p01_analisis_salud_activos.ipynb
├── img/
│   └── (figuras exportadas por el notebook)
└── README.md
```

## Qué hace cada archivo

- `data/camiones_mina_mantenimiento.csv`: histórico simulado de OT con horas de paro, horas trabajadas, causa raíz, sistema, etc.
- `notebooks/p01_analisis_salud_activos.ipynb`: notebook principal (cálculo de disponibilidad, MTBF/MTTR, Pareto y gráficos).
- `img/`: salida de figuras para usar en reportes o presentaciones.

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
cd p01_salud_activos_camiones

# Abrir el notebook (VS Code o Jupyter)
jupyter notebook
```

Luego ejecutar el notebook:
- `notebooks/p01_analisis_salud_activos.ipynb`

## Entradas y salidas

- **Entrada**: `data/camiones_mina_mantenimiento.csv`.
- **Salidas**: tablas agregadas dentro del notebook y figuras en `img/` (por ejemplo: disponibilidad por equipo, horas de paro por equipo, Pareto por causa).

## Metodología (resumen técnico)

- Conversión de fechas y normalización de campos.
- Agregación por `equipo` y `mes`.
- Definición de métricas: disponibilidad (horas trabajadas / horas disponibles), conteo de fallas, MTTR y MTBF.
- Pareto por `causa_raiz` y visualizaciones para priorización.

## Resultados esperables / cómo interpretar

Lo esperable es identificar:
- Equipos que concentran horas de paro y baja disponibilidad.
- Un conjunto reducido de causas raíz que explican la mayor parte del impacto.
- Diferencias claras MTBF/MTTR entre equipos (base para acciones: repuestos, planes PM, entrenamiento, rediseño).

## Notas y referencias técnicas

- KPIs clásicos de mantenimiento: Availability, MTBF, MTTR.
- Principio de Pareto aplicado a fallas.
- En entornos corporativos, este enfoque suele alimentarse desde SAP PM/Maximo u otras fuentes ERP/CMMS.

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
