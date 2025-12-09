# Proyecto 03 – Fallas en Correas Transportadoras

## 1. Contexto

Este proyecto analiza eventos de **falla en correas transportadoras** de una faena minera ficticia (“Faena Atacama Norte”).  
El objetivo es identificar qué correas, tramos y causas de falla generan mayor impacto en términos de **horas de paro** y **pérdida de producción (toneladas)**, y evaluar un **escenario de mejora** sobre la causa principal.

Los datos están estructurados como un registro histórico de eventos de falla, con marcas de tiempo, clasificación por tramo y estimación de impacto productivo.

## 2. Preguntas de negocio

- ¿Qué correas concentran la mayor cantidad de horas de paro y pérdida de producción?
- ¿Qué tramos específicos son más críticos dentro de cada correa?
- ¿Cuáles son las causas de falla más importantes (análisis de Pareto)?
- ¿Qué impacto tendría una reducción en la frecuencia o duración de la causa de falla principal?

## 3. Datos utilizados

- Archivo principal: `data/fallas_correas_transportadoras.csv`

Campos clave:

- `id_evento`: identificador del evento de falla.
- `correa`: identificador de la correa transportadora (ej. CV-01, CV-02, …).
- `tramo`: tramo de la correa (T1, T2, …).
- `fecha_inicio`, `fecha_termino`: marca de tiempo del inicio y término del evento.
- `causa_falla`: descripción resumida de la causa de falla (desalineamiento, rotura de empalme, etc.).
- `horas_paro`: duración del evento en horas.
- `impacto_produccion_ton`: impacto estimado en toneladas no producidas.
- `faena`, `mes`: contexto de operación y periodo.

## 4. Enfoque analítico

El análisis se desarrolla en el notebook:

- `notebooks/p03_analisis_fallas_correas.ipynb`

Pasos principales:

1. **KPIs por correa y tramo**
   - Suma de horas de paro e impacto en producción por `correa`.
   - Desglose por `correa` + `tramo` para identificar segmentos críticos.

2. **Análisis de causas de falla (Pareto)**
   - Agrupación de horas de paro por `causa_falla`.
   - Cálculo de porcentajes y porcentaje acumulado para identificar las causas que explican la mayor parte de las horas de detención.

3. **Escenario de mejora**
   - Identificación de la causa de falla principal.
   - Simulación de un escenario donde las horas de paro asociadas a esa causa se reducen en un porcentaje (ej. 30%).
   - Reestimación del impacto total en producción y comparación contra el escenario base.

4. **Visualización**
   - Horas de paro por correa.
   - Impacto en producción por correa.
   - Top de causas de falla por horas de paro.

## 5. Resultados clave (ejemplo de interpretación)

- Algunas correas concentran una proporción significativa de las horas de detención y del impacto en toneladas no producidas, lo que las convierte en focos prioritarios para proyectos de confiabilidad.
- El análisis por tramo permite localizar segmentos particularmente problemáticos dentro de una misma correa.
- El Pareto de causas de falla muestra que un conjunto reducido de modos de falla explica la mayor parte del impacto, facilitando la priorización de acciones de mantenimiento y mejoras de diseño.
- El escenario de mejora sobre la causa principal permite cuantificar el beneficio potencial (en horas de disponibilidad y toneladas) de iniciativas específicas (por ejemplo, mejoras en alineamiento, calidad de empalmes o monitoreo de rodillos).

## 6. Relevancia para Performance & Analytics en minería

Este proyecto demuestra la capacidad para:

- Modelar y analizar datos de eventos de falla con impacto operativo y productivo.
- Construir indicadores orientados a **disponibilidad de sistemas críticos** (correas transportadoras).
- Simular escenarios de mejora para estimar el beneficio de intervenciones específicas.
- Presentar resultados que pueden integrarse en dashboards y rutinas de gestión de activos.


## 👤 About Me – Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

Me especializo en estructurar y escalar procesos de análisis basados en datos, generar valor desde la observación —desde la operación minera hasta la investigación astronómica— y traducir métricas complejas en decisiones claras. He trabajado en arquitectura de datos, integración de sistemas, automatización, gestión de plataformas TI y habilitación de equipos técnicos.

Exploro, investigo y construyo soluciones. Mi enfoque une el método científico, la ingeniería y la narrativa visual; desde modelos analíticos hasta proyectos de cielo profundo. Creo en el uso inteligente de la información, en la rigurosidad técnica y en la elegancia de las soluciones simples que funcionan.

---

### 🔗 Contacto & Presencia Online

- ✉️ **Email**: [teleobjetivo.boutique@gmail.com](mailto:teleobjetivo.boutique@gmail.com)  
- 🌐 **Web**: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- 📷 **Instagram**: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
- 💻 **GitHub (Portafolio)**: [teleobjetivo/analytics-tech-portfolio](https://github.com/teleobjetivo/analytics-tech-portfolio)

---
