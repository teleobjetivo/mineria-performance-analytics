
# P08 – DataCopilot Auto-Analyst
**Explorador Automático de Datasets con Reporte Inteligente**

DataCopilot es un analista automático en Python que toma un archivo CSV, inspecciona su estructura, calcula métricas clave, detecta outliers y genera un informe Markdown listo para compartir.

No entrena modelos complejos: se enfoca en **entender el dataset** rápidamente y producir un resumen limpio y accionable, ideal para:
- exploración inicial de datos de negocio,
- soporte a analistas y equipos TI,
- clases de Data Science y demostraciones técnicas.

---

## 🎯 Objetivo

Demostrar capacidad de:
- diseñar y construir herramientas internas de analítica,
- automatizar EDA (Exploratory Data Analysis),
- generar insights reproducibles,
- trabajar con datos heterogéneos sin depender de una UI gráfica.

Es un proyecto ligero, pero con mentalidad de **producto interno**: algo que un equipo real podría usar a diario para partir cualquier análisis.

---

## 🧱 Arquitectura del Proyecto

```text
p08_datacopilot/
│── data/
│     └── demo_sales.csv
│── img/
│     └── hist_amount.png              # se genera tras la ejecución
│── reports/
│     └── auto_report.md               # informe automático en Markdown
│── datacopilot.py                     # núcleo de la herramienta
│── README.md
```

---

## ⚙️ Setup rápido

Desde la raíz del repositorio:

```bash
source .venv/bin/activate        # si no está activo ya
python setup_p08_datacopilot.py  # se ejecuta una sola vez
```

Esto crea la carpeta `p08_datacopilot/`, el CSV de ejemplo y el script principal `datacopilot.py`.

---

## ▶️ Uso básico

### 1. Usar el dataset de ejemplo

```bash
cd p08_datacopilot
python datacopilot.py
```

El script:

- carga `data/demo_sales.csv`,
- analiza columnas, tipos y datos faltantes,
- calcula métricas para columnas numéricas,
- detecta outliers por columna (regla 1.5 IQR),
- genera un histograma de la métrica principal (`amount`),
- escribe un informe en `reports/auto_report.md`.

### 2. Usar cualquier otro CSV

```bash
cd p08_datacopilot
python datacopilot.py /ruta/a/tu_archivo.csv
```

Requisitos mínimos del CSV:
- tener encabezados en la primera fila;
- idealmente mezclar columnas numéricas y categóricas.

---

## 📊 ¿Qué contiene el informe?

El archivo `reports/auto_report.md` incluye:

1. **Resumen estructural**
   - filas, columnas,
   - listado de columnas y tipos.

2. **Porcentaje de datos faltantes por columna**  
   Permite detectar dónde hay problemas de calidad.

3. **Métricas numéricas (describe)**  
   - `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max`.

4. **Detección simple de outliers (regla 1.5 IQR)**  
   - cantidad de outliers potenciales por columna numérica.

5. **Insight automático en lenguaje natural**  
   - tamaño del dataset,
   - salud de datos faltantes,
   - columnas con outliers,
   - lectura rápida de la métrica principal (`amount` si existe).

6. **Referencia a la visualización principal**  
   - histograma de la columna principal generada en `img/`.

---

## 💡 Extensiones posibles

Este proyecto está diseñado para poder crecer fácilmente hacia:

- incorporación de scoring de calidad de dataset,
- generación de reportes en HTML o PDF,
- integración con notebooks Jupyter,
- ejecución como servicio batch (por ejemplo, en un cron),
- incorporación de modelos ligeros (regresiones simples o clustering).

---

## 👤 About Me — Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital. Mi trabajo combina estrategia, ciencia de datos y operación real de negocio, integrando capacidades técnicas con visión ejecutiva.

Exploro, investigo y construyo soluciones. Creo en el uso inteligente de la información, en la rigurosidad técnica y en la elegancia de las soluciones simples que funcionan.

---

## 🔗 Contacto Profesional

- 📧 **Email:** teleobjetivo.boutique@gmail.com  
- 🌐 **Sitio Web:** https://www.teleobjetivo.cl  
- 📸 **Instagram:** https://www.instagram.com/tele.objetivo  
- 💻 **GitHub (Portafolio):** https://github.com/teleobjetivo/analytics-tech-portfolio  

---

## 📄 Licencia

MIT License — libre uso educativo y profesional.
