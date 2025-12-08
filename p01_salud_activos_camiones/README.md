# Proyecto 01 – Salud de Activos: Camiones de Extracción

## 1. Contexto

Este proyecto simula el análisis de la **salud de una flota de camiones de extracción (CAEX)** en una faena minera ficticia (“Faena Atacama Norte”).  
El objetivo es mostrar cómo, a partir de datos estructurados de forma similar a una extracción de **SAP PM**, se pueden construir indicadores de mantenimiento y visualizaciones que apoyen decisiones de desempeño y confiabilidad.

El análisis está implementado en **Python (pandas + matplotlib) sobre Jupyter Notebooks**, pensando en que la lógica sea fácilmente trasladable a herramientas como Power BI u otras plataformas de reporting corporativo.

## 2. Preguntas de negocio

El caso responde, entre otras, a las siguientes preguntas:

- ¿Cuál es la **disponibilidad** de la flota por mes y por camión?
- ¿Qué equipos concentran la mayor cantidad de **horas de detención**?
- ¿Cuáles son las **principales causas de falla** (análisis de Pareto)?
- ¿Cómo se comportan los indicadores **MTBF** (Mean Time Between Failures) y **MTTR** (Mean Time To Repair) por equipo?

## 3. Datos utilizados

- Archivo principal: `data/camiones_mina_mantenimiento.csv`
- Registros simulados de órdenes de trabajo de mantenimiento, con estructura compatible con un escenario típico de SAP PM:

Campos clave:

- `id_ot`: identificador de la orden de trabajo.
- `equipo`: código del camión (ej. CAEX-101, CAEX-102, …).
- `fecha_inicio`, `fecha_termino`: marca de tiempo de la intervención.
- `tipo_mantencion`: Preventiva / Correctiva.
- `sistema`: Motor, Transmisión, Frenos, Eléctrico, Neumáticos, Hidráulico.
- `causa_raiz`: descripción resumida de la causa de la intervención.
- `horas_paro`: horas de detención asociadas a la OT.
- `horas_trabajadas_periodo`: horas operadas por el camión en el periodo.
- `criticidad_equipo`: Alta / Media / Baja.
- `faena`: nombre de la faena ficticia.
- `mes`: periodo de análisis (formato YYYY-MM).

Los datos cubren varios meses y múltiples equipos, permitiendo calcular indicadores por camión y por periodo.

## 4. Enfoque analítico

El análisis se desarrolla en el notebook:

- `notebooks/p01_analisis_salud_activos.ipynb`

Los pasos principales son:

1. **Preparación de datos**
   - Carga del CSV y conversión de campos de fecha/hora.
   - Agrupación de la información por `equipo` y `mes`.
   - Consolidación de horas de paro (`horas_paro_total`) y horas trabajadas (`horas_trab_periodo`).

2. **Cálculo de indicadores**
   - **Horas disponibles** = horas trabajadas + horas de paro.
   - **Disponibilidad** = horas trabajadas / horas disponibles.
   - **Número de fallas** = cantidad de OT en el periodo.
   - **MTTR** = horas de paro total / número de fallas.
   - **MTBF** ≈ horas trabajadas / número de fallas.

3. **Análisis de causas de falla**
   - Agrupación de horas de paro por `causa_raiz`.
   - Construcción de un **Pareto de fallas**, calculando porcentaje y porcentaje acumulado para cada causa.

4. **Visualización**
   - Gráficos de barras para:
     - Disponibilidad promedio por equipo.
     - Horas de paro totales por equipo.
     - Top de causas de falla por horas de paro.
   - Estos gráficos permiten identificar rápidamente equipos y modos de falla prioritarios.

## 5. Resultados clave (ejemplo de interpretación)

> Nota: Los valores específicos dependen del dataset simulado; aquí se muestra el tipo de conclusiones que se pueden obtener.

- La **disponibilidad promedio de la flota** se mantiene en un rango razonable, pero se observan diferencias claras entre equipos: algunos camiones muestran disponibilidades cercanas al mínimo del conjunto, lo que los convierte en candidatos naturales para planes de mejora de confiabilidad.

- Un subconjunto reducido de camiones concentra una proporción importante de las **horas de detención**. Focalizar acciones sobre esos equipos (revisiones específicas, cambios de estrategia de mantenimiento, análisis detallado de causas) puede generar una mejora relevante en la disponibilidad global.

- El análisis de **Pareto de causas de falla** muestra que unas pocas causas raíz (por ejemplo, fugas hidráulicas y sobrecalentamiento de motor) explican la mayor parte de las horas de paro. Esto permite priorizar recursos en esos modos de falla antes de dispersarse en causas menores.

- Los indicadores **MTBF** (tiempo medio entre fallas) y **MTTR** (tiempo medio de reparación) por equipo entregan una base cuantitativa para:
  - Comparar el comportamiento entre camiones.
  - Medir el efecto de iniciativas futuras (reducción de tiempos de reparación, ajustes a la mantención preventiva, cambios de repuestos, etc.).


## 6. Relevancia para un rol de Performance & Analytics en minería

Este proyecto ilustra la capacidad para:

- Diseñar y estructurar modelos de datos inspirados en información de **SAP PM / sistemas ERP**.
- Calcular indicadores clave de mantenimiento (disponibilidad, MTBF, MTTR) a partir de registros de órdenes de trabajo.
- Identificar oportunidades de mejora mediante análisis de Pareto y comparación entre equipos.
- Presentar resultados de manera clara y accionable, listos para ser llevados a dashboards en herramientas como **Power BI** u otras plataformas corporativas.

En un entorno real, la misma lógica se puede conectar a fuentes de datos productivas, integrarse con rutinas de reporte y alimentar procesos de mejora continua (PDCA) en mantenimiento y confiabilidad.
