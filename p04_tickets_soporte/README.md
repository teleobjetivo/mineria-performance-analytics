# P04 — Priorización de Tickets de Soporte TI (Score Operacional)

_Reglas simples, auditable y listo para Excel/Power BI._

## Resumen

Soy Hugo Baghetti. En este proyecto transformo un listado de tickets de soporte en una cola priorizada, usando un score compuesto (prioridad base, SLA, días abiertos, estado). El objetivo es formalizar criterios que normalmente viven 'en la cabeza' del equipo.

## Por qué hice este proyecto

En soporte, la fricción típica es siempre la misma: se atiende por urgencia percibida y no por riesgo. Yo necesitaba un mecanismo explicable para ordenar el trabajo, minimizar incumplimientos de SLA y visualizar dónde está el dolor.

## Qué demuestra (en trabajo real)

- Modelado de reglas de negocio en scoring explicable.
- Generación de artefactos operacionales (CSV priorizado) para integración rápida.
- Visualización para gestión: identificar categorías con mayor score promedio.

## Estructura del proyecto

```text
p04_tickets_soporte/
├── data/
│   ├── tickets_soporte_demo.csv
│   └── tickets_priorizados.csv
├── notebooks/
│   └── p04_priorizacion_tickets.ipynb
├── img/
│   └── score_promedio_por_categoria.png
└── README.md
```

## Qué hace cada archivo

- `data/tickets_soporte_demo.csv`: dataset de entrada (tickets).
- `notebooks/p04_priorizacion_tickets.ipynb`: notebook que calcula los scores y genera salidas.
- `data/tickets_priorizados.csv`: salida con columnas de scoring.
- `img/score_promedio_por_categoria.png`: figura de gestión.

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
cd p04_tickets_soporte
jupyter notebook
```

Ejecutar:
- `notebooks/p04_priorizacion_tickets.ipynb`

## Entradas y salidas

- **Entrada**: `data/tickets_soporte_demo.csv`.
- **Salidas**:
  - `data/tickets_priorizados.csv` (incluye `score_prioridad_base`, `score_sla`, `score_dias`, `score_estado`, `score_total`).
  - `img/score_promedio_por_categoria.png`.

## Metodología (resumen técnico)

- Asignación de puntajes por criterios (prioridad, SLA vencido, días abiertos, estado).
- Suma ponderada → `score_total`.
- Ordenamiento descendente por score (y desempate por días abiertos).
- Export de CSV y una visualización simple para análisis por categoría.

## Resultados esperables / cómo interpretar

Lo útil aquí es que el output es un artefacto operativo:
- se puede cargar directo a Excel/Power BI,
- sirve como cola diaria y como base de gobernanza,
- permite explicar por qué un ticket está arriba (auditable).

## Notas y referencias técnicas

- Scoring explicable como alternativa liviana a modelos ML cuando se requiere gobernanza.
- SLA + antigüedad + estado suelen ser predictores fuertes del riesgo operacional en soporte.

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
