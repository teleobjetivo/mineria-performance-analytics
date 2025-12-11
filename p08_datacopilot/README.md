# P08 – DataCopilot Auto‑Analyst

Herramienta ligera en Python que actúa como un “copiloto de datos”:  
lee un archivo CSV cualquiera, calcula estadísticas clave y genera un **informe automático en Markdown** con:

- resumen de columnas,
- métricas descriptivas básicas,
- detección simple de valores faltantes,
- distribución de variables numéricas,
- comentarios interpretativos.

La idea es mostrar cómo **automatizar el análisis exploratorio inicial (EDA)** de forma reproducible y reutilizable, sin depender de notebooks gigantes ni de herramientas externas.

---

## 🎯 Objetivo del proyecto

Este proyecto responde a un escenario muy concreto:

> “Llega un CSV nuevo (minería, retail, banca, TI, etc.) y necesito una **mirada rápida e inteligente** sin perder tiempo armando gráficos a mano.”

**DataCopilot** permite:

1. Entregar un informe base consistente para cualquier dataset tabular.
2. Estandarizar la primera capa de análisis para equipos de datos.
3. Demostrar criterio analítico y automatización sin caer en complejidad innecesaria.

---

## 🧱 Estructura del proyecto

```bash
p08_datacopilot/
├── data/
│   └── ejemplo_dataset.csv        # CSV de muestra (puede ser reemplazado)
├── reports/
│   └── reporte_datacopilot.md     # Informe generado automáticamente
├── notebooks/
│   └── p08_datacopilot_demo.ipynb # Demo interactiva opcional
└── src/
    └── datacopilot.py             # Núcleo de la lógica del “auto‑analyst”
```

---

## ⚙️ Cómo usar DataCopilot

> Ejemplo asumiendo que estás en la carpeta raíz del portafolio  
> (`/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria`)

### 1️⃣ Activar entorno virtual

```bash
cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
source .venv/bin/activate
```

### 2️⃣ Ejecutar el análisis automático sobre el dataset de ejemplo

```bash
python p08_datacopilot/src/datacopilot.py     --input "p08_datacopilot/data/ejemplo_dataset.csv"     --output "p08_datacopilot/reports/reporte_datacopilot.md"
```

Si todo va bien, verás un mensaje indicando la ruta del informe generado.

### 3️⃣ Abrir el informe

- Desde Finder, navega a:
  - `p08_datacopilot/reports/reporte_datacopilot.md`
- O desde terminal:

```bash
open p08_datacopilot/reports/reporte_datacopilot.md
```

---

## 🧪 Probar con tu propio dataset

Puedes reutilizar DataCopilot para cualquier CSV con formato tabular razonable:

```bash
python p08_datacopilot/src/datacopilot.py     --input "RUTA/A/TU_ARCHIVO.csv"     --output "p08_datacopilot/reports/reporte_mi_dataset.md"
```

Recomendaciones:

- Que el CSV tenga encabezado en la primera fila.
- Separador estándar (`,` o `;`).
- Usar UTF‑8 para evitar problemas de caracteres.

---

## 🔍 Qué hace exactamente DataCopilot

A nivel técnico, el script:

1. Carga el dataset con **pandas**.
2. Identifica columnas numéricas y categóricas.
3. Calcula para columnas numéricas:
   - count, mean, std, min, max, quartiles.
4. Cuenta valores nulos y su porcentaje por columna.
5. Revisa número de categorías distintas en las columnas tipo “object”.
6. Genera un **reporte en Markdown** con secciones como:
   - Información general del dataset,
   - Tabla de resumen numérico,
   - Tabla de valores faltantes,
   - Comentarios interpretativos básicos.

---

## 🧩 Casos de uso

- Primer screening de datasets de:
  - minería,
  - mantenimiento,
  - retail,
  - finanzas,
  - tickets TI,
  - o incluso astrofotografía (catálogos de objetos, condiciones de cielo, etc.).
- Herramienta interna de equipo para unificar el “primer vistazo” a los datos.
- Demostración de criterio analítico + automatización en entrevistas técnicas.

---

## 👤 Sobre el autor

**Hugo Baghetti Calderón**  
Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital.  
Exploro, investigo y construyo soluciones que combinan datos, operación y narrativa visual; desde la gran minería hasta la astrofotografía de cielo profundo.

- 📧 Email: [teleobjetivo.boutique@gmail.com](mailto:teleobjetivo.boutique@gmail.com)  
- 🌐 Web: [www.teleobjetivo.cl](https://www.teleobjetivo.cl)  
- 📸 Instagram: [@tele.objetivo](https://www.instagram.com/tele.objetivo)  
- 💻 GitHub Portafolio: [analytics-tech-portfolio](https://github.com/teleobjetivo/analytics-tech-portfolio)
