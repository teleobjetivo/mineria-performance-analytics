# Proyecto 02 – Backlog de Mantenimiento: Priorización de Órdenes de Trabajo

## 1. Contexto

Este proyecto aborda el análisis de un **backlog de órdenes de trabajo (OT)** de mantenimiento en una faena minera ficticia.  
El foco está en entender el tamaño y composición del backlog, y en construir un **modelo simple de priorización** que permita ordenar las OT según su impacto potencial en el negocio.

Los datos están estructurados de forma similar a un extracto de **SAP PM / ERP**, e incluyen criticidades, fechas, estados y características técnicas de las OT.

## 2. Preguntas de negocio

- ¿Cuál es el **tamaño del backlog** y cómo se distribuye por criticidad y estado?
- ¿Cuál es la **edad** del backlog (días desde la creación de la OT)?
- ¿Qué porcentaje del backlog está **vencido** respecto de una fecha de corte?
- ¿Cómo se puede definir un **score de prioridad** que ordene las OT de forma consistente y explicable?

## 3. Datos utilizados

- Archivo principal: `data/backlog_ordenes_trabajo.csv`

Campos principales:

- `id_ot`: identificador de la OT de mantenimiento.
- `equipo`: equipo asociado a la OT.
- `fecha_creacion`: fecha en que se crea la OT.
- `fecha_vencimiento`: fecha comprometida o límite de atención.
- `criticidad_ot`: criticidad de la OT (Alta, Media, Baja).
- `criticidad_equipo`: criticidad del equipo asociado.
- `tipo_trabajo`: Correctivo, Preventivo, Inspección, Mejora.
- `sistema`: sistema intervenido.
- `estado`: Abierta, En ejecución, Planificada.
- `dias_backlog`: días transcurridos desde la creación hasta la fecha de corte.
- `faena`, `mes`: información contextual para el periodo de análisis.

## 4. Enfoque analítico y modelo de prioridad

El análisis se implementa en:

- `notebooks/p02_analisis_backlog.ipynb`

Pasos principales:

1. **KPIs de backlog**
   - Cálculo del tamaño total del backlog.
   - Distribución por criticidad, estado y otros atributos.
   - Cálculo de estadísticas sobre `dias_backlog`.
   - Identificación de OT vencidas respecto a una fecha de corte.

2. **Construcción de un score de prioridad**
   - Asignación de pesos a:
     - Criticidad de la OT (`criticidad_ot`).
     - Criticidad del equipo (`criticidad_equipo`).
     - Antigüedad de la OT (`dias_backlog`, normalizada).
     - Estado de la OT (mayor peso a “Abierta” que a “Planificada”).
   - Definición de un **score numérico** que combina estos factores de forma explicable:

     > Ejemplo de fórmula:  
     > `score_prioridad = 2 * criticidad_ot + criticidad_equipo + f(dias_backlog) + peso_estado`

   - Ordenamiento del backlog según este score para obtener un **ranking de atención**.

3. **Visualización**
   - Gráfico de backlog por criticidad de OT.
   - Distribución de días en backlog.
   - Relación entre días en backlog y score de prioridad.

## 5. Resultados clave (ejemplo de interpretación)

- El análisis permite cuantificar el backlog total y entender qué proporción corresponde a OT de criticidad **Alta**.
- La distribución de `dias_backlog` muestra qué tan “envejecido” está el backlog y si existe una cola de órdenes con muchos días de antigüedad.
- El porcentaje de OT vencidas entrega una señal clara sobre el nivel de cumplimiento de los compromisos de atención.
- El score de prioridad genera un ranking transparente, donde las OT más críticas, asociadas a equipos críticos y con mayor tiempo en backlog, aparecen en los primeros lugares, facilitando la planificación semanal de mantenimiento.

## 6. Enfoque PDCA (mejora continua)

Este proyecto puede insertarse en una lógica de mejora continua (PDCA):

- **Plan**: Definir criterios de criticidad y una fórmula de score de prioridad alineada con la estrategia de la operación.
- **Do**: Aplicar el modelo al backlog real para ordenar y planificar recursos.
- **Check**: Monitorear el comportamiento del backlog (tamaño, edad, % vencido) tras algunas semanas de uso del modelo.
- **Act**: Ajustar pesos y criterios del score según resultados y feedback de planificación/mantenimiento.

De esta forma, el análisis no se queda solo en un reporte estático, sino que se convierte en una **herramienta de gestión** para la toma de decisiones en mantenimiento.

## 👤 About Me – Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

Me especializo en estructurar y escalar procesos de análisis basados en datos, generar valor desde la observación —desde la operación minera hasta la investigación astronómica— y traducir métricas complejas en decisiones claras. He trabajado en arquitectura de datos, integración de sistemas, automatización, gestión de plataformas TI y habilitación de equipos técnicos.

Exploro, investigo y construyo soluciones. Mi enfoque une el método científico, la ingeniería y la narrativa visual; desde modelos analíticos hasta proyectos de cielo profundo. Creo en el uso inteligente de la información, en la rigurosidad técnica y en la elegancia de las soluciones simples que funcionan.

---

### 🔗 Contacto & Presencia Online

- ✉️ **Email**: [teleobjetivo.boutique@gmail.com](mailto:teleobjetivo.boutique@gmail.com)  
- 🌐 **Web**: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- 📷 **Instagram**: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
- 💻 **GitHub (Portafolio)**: [teleobjetivo/mineria-performance-analytics](https://github.com/teleobjetivo/analytics-tech-portfolio)

---
