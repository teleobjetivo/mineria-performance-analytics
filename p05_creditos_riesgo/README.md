# P05 — Segmentación de Riesgo de Créditos (Scoring explicable)

_De un CSV operativo a un score y segmentos Bajo/Medio/Alto._

## Resumen

Soy Hugo Baghetti. Este proyecto toma un dataset de créditos de consumo simulado y construye una segmentación de riesgo explicable para apoyar decisiones como priorización de gestión, revisión de políticas o monitoreo de cartera.

## Por qué hice este proyecto

En banca y retail financiero, muchas decisiones se toman con reglas (o modelos) que deben ser explicables: por qué un crédito entra en 'Alto' y cuál es el factor dominante. Quise demostrar un scoring simple pero realista, usando señales típicas: relación monto/ingreso, comportamiento de pago (mora) y variables de perfil.

## Qué demuestra (en trabajo real)

- Diseño de score auditable y portable (reglas claras, sin 'caja negra').
- Feature engineering básico (ratios) y normalización.
- Producción de salidas reutilizables: CSV enriquecido + gráfico para reporte.

## Estructura del proyecto

```text
p05_creditos_riesgo/
├── data/
│   ├── creditos_raw.csv
│   └── creditos_riesgo_segmentado.csv
├── notebooks/
│   └── p05_riesgo_creditos.ipynb
├── img/
│   └── creditos_por_segmento_riesgo.png
└── README.md
```

## Qué hace cada archivo

- `data/creditos_raw.csv`: dataset de entrada (créditos) con variables de cliente y producto.
- `notebooks/p05_riesgo_creditos.ipynb`: notebook de scoring y segmentación.
- `data/creditos_riesgo_segmentado.csv`: salida con features y scores (incluye `score_total` y `segmento_riesgo`).
- `img/creditos_por_segmento_riesgo.png`: gráfico de distribución por segmento.

## Instalación

```bash
cd <repository-root>
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
pip install -U pip
pip install pandas matplotlib jupyter
```

## Ejecución

```bash
cd <repository-root>
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows
cd p05_creditos_riesgo
jupyter notebook
```

Ejecutar:
- `notebooks/p05_riesgo_creditos.ipynb`

## Entradas y salidas

- **Entrada**: `data/creditos_raw.csv` con columnas como: `monto_credito`, `ingreso_mensual`, `plazo_meses`, `tasa_interes_anual`, `segmento`, `region`, `estado`.
- **Salidas**:
  - `data/creditos_riesgo_segmentado.csv` con columnas adicionales: `ratio_monto_ingreso`, `score_mora`, `score_ratio`, `score_monto`, `score_buro_norm`, `score_total`, `segmento_riesgo`.
  - `img/creditos_por_segmento_riesgo.png` con la distribución de segmentos.

## Metodología (resumen técnico)

- Feature engineering: `ratio_monto_ingreso = monto_credito / ingreso_mensual`.
- Scoring por componentes (ejemplo conceptual):
  - **mora**: puntaje mayor si hay señales de atraso.
  - **ratio**: puntaje mayor si el monto relativo al ingreso es alto.
  - **monto**: puntaje por tramos del monto.
  - **buro (normalizado)**: componente numérico adicional para robustez.
- Suma de componentes → `score_total`.
- Segmentación en tres niveles: Bajo / Medio / Alto (umbrales definidos en el notebook).

## Resultados esperables / cómo interpretar

En trabajo real, este tipo de segmentación sirve para:
- priorizar gestión de cobranza y alertas,
- reforzar políticas (por segmento, región o producto),
- monitorear drift si el score se recalcula periódicamente,
- alimentar un tablero simple para riesgo operacional/financiero.

Importante: aquí la intención es la **explicabilidad** y la trazabilidad del criterio, no competir con modelos de score crediticio comerciales.

## Notas y referencias técnicas

- Scoring rules-based: útil cuando se requiere auditoría y justificación.
- Feature engineering con ratios (monto/ingreso) como proxy de carga financiera.
- Segmentación ordinal (Bajo/Medio/Alto) para operación y comunicación ejecutiva.

## Próximos pasos

- Agregar validación con holdout temporal y métricas (si existiera variable objetivo: mora real).
- Sensibilidad de umbrales y pesos (análisis de impacto por política).
- Exportar como función/CLI para recalcular score en batch.

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
