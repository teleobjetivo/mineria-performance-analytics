# Portafolio – Performance & Analytics (Minería, Retail, Soporte TI y Astronomía)

Este repositorio reúne una serie de **mini–proyectos de análisis de datos**
orientados a roles de **Performance & Analytics / Data Analyst** en contextos
de minería, banca retail, soporte TI y un caso de astronomía aplicado.

Todos los ejemplos están construidos en **Python + Jupyter Notebooks**, con
datasets simulados pero **realistas** y lógica de negocio explicable, pensada
para discutir con equipos técnicos y no técnicos.

---

## Índice de proyectos

### P01 – Salud de activos de camiones de extracción (Minería)

**Carpeta:** [`p01_salud_activos_camiones/`](./p01_salud_activos_camiones/README.md)  

Analiza la **disponibilidad de la flota de camiones** en una operación minera:

- Dataset de eventos de mantenimiento y horas de paro por equipo.
- Cálculo de KPIs claves (disponibilidad, horas de detención, MTBF, MTTR).
- Identificación de **equipos críticos** con mayor impacto en horas de paro.
- Gráficos listos para usar en reportes o dashboards ejecutivos.

---

### P02 – Backlog de órdenes de trabajo de mantenimiento (Minería)

**Carpeta:** [`p02_backlog_mantenimiento/`](./p02_backlog_mantenimiento/README.md)  

Evalúa el **backlog de mantenimiento** para identificar riesgos operacionales:

- Dataset de órdenes de trabajo con criticidad, días de atraso y estado.
- Construcción de un **score de riesgo del backlog**.
- Distribución de órdenes por criticidad y días en atraso.
- Base para discutir **priorización de mantenimiento** y mejora continua (PDCA).

---

### P03 – Fallas en correas transportadoras (Minería)

**Carpeta:** [`p03_fallas_correas/`](./p03_fallas_correas/README.md)  

Explora la **confiabilidad de correas transportadoras** en una planta minera:

- Dataset de fallas con horas de paro, causa raíz y correa afectada.
- Identificación de correas con **mayor impacto en producción**.
- Análisis de Pareto de causas de falla.
- Soporte para decisiones de **plan de acción de confiabilidad**.

---

### P04 – Priorización de tickets de soporte TI

**Carpeta:** [`p04_tickets_soporte/`](./p04_tickets_soporte/README.md)  

Modelo sencillo para **priorizar tickets de soporte** según impacto y urgencia:

- Dataset de tickets con severidad, categoría, tiempos de resolución.
- Construcción de un **score de priorización de tickets**.
- Ranking de categorías con mayor “dolor” para el negocio.
- Visualización del **score promedio por categoría**.

Este ejemplo calza bien con roles de **Soporte Tecnológico / Performance &
Analytics** que deben traducir datos de operación TI en decisiones accionables.

---

### P05 – Segmentación de riesgo de créditos retail

**Carpeta:** [`p05_creditos_riesgo/`](./p05_creditos_riesgo/README.md)  

Simula una cartera de **créditos de consumo retail** y construye un
**score de riesgo explicable**:

- Dataset con monto, ingreso, historial de mora y score de buró simulado.
- Cálculo de un **score_total** compuesto (mora, carga financiera, monto y buró).
- Segmentación en **Bajo / Medio / Alto riesgo**.
- CSV resultante listo para alimentar **Power BI, Excel o tableros internos**.

Ejemplo útil para roles en **banca / riesgo retail / analytics**.

---

### P06 – Condiciones de cielo para observación de cielo profundo

**Carpeta:** [`p06_cielo_profundo/`](./p06_cielo_profundo/README.md)  

Caso compacto inspirado en **astronomía / astrofotografía**:

- Dataset con condiciones de cielo (seeing, transparencia, fase lunar, Bortle).
- Score simple para **priorizar noches** según calidad de observación.
- Base para discutir cómo integrar datos operacionales y de entorno
  en decisiones de planificación (ej.: elección de ventana de observación).

Este proyecto sirve como ejemplo de **aplicación de analítica a un dominio técnico
no tradicional**, mostrando versatilidad en el uso de datos.

---

## Tecnologías utilizadas

- **Lenguaje:** Python (3.x)
- **Entorno:** Jupyter Notebooks / VS Code
- **Librerías principales:**
  - `pandas` para manejo de datos
  - `matplotlib` para visualizaciones simples
- **Control de versiones:** Git + GitHub

---

## Cómo ejecutar localmente

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/teleobjetivo/mineria-performance-analytics.git
   cd mineria-performance-analytics
   ```

2. Crear y activar entorno virtual (opcional pero recomendado):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Instalar dependencias mínimas:

   ```bash
   pip install pandas matplotlib jupyter
   ```

4. Abrir el proyecto en VS Code o Jupyter y ejecutar los notebooks dentro de
   cada carpeta (`p05_.../notebooks`).


## 👤 About Me – Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

Me especializo en estructurar y escalar procesos de análisis basados en datos, generar valor desde la observación —desde la operación minera hasta la investigación astronómica— y traducir métricas complejas en decisiones claras. He trabajado en arquitectura de datos, integración de sistemas, automatización, gestión de plataformas TI y habilitación de equipos técnicos.

Exploro, investigo y construyo soluciones. Mi enfoque une el método científico, la ingeniería y la narrativa visual; desde modelos analíticos hasta proyectos de cielo profundo. Creo en el uso inteligente de la información, en la rigurosidad técnica y en la elegancia de las soluciones simples que funcionan.

---

### 🔗 Contacto & Presencia Online

- ✉️ **Email**: [teleobjetivo.boutique@gmail.com](mailto:teleobjetivo.boutique@gmail.com)  
- 🌐 **Web**: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- 📷 **Instagram**: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
- 💻 **GitHub (Portafolio)**: [teleobjetivo/mineria-performance-analytics](https://github.com/teleobjetivo/portfolio-data-analytics)

---

---

