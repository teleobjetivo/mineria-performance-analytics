# P05 – Segmentación de riesgo de créditos retail

Este proyecto simula una **cartera de créditos retail** y construye un
**score de riesgo** que permite clasificar a cada cliente en segmentos
**Bajo / Medio / Alto** riesgo, utilizando reglas simples y explicables.

La idea es mostrar cómo, a partir de datos operacionales (monto, ingreso,
mora, score de buró), se puede construir una lógica de riesgo reproducible,
lista para alimentar reportes o dashboards.

---

## 1. Estructura del proyecto

```text
p05_creditos_riesgo/
├── data/
│   ├── creditos_raw.csv               # datos simulados de créditos
│   └── creditos_riesgo_segmentado.csv # salida con score y segmento de riesgo
├── img/
│   └── creditos_por_segmento_riesgo.png
├── notebooks/
│   └── p05_riesgo_creditos.ipynb      # notebook principal de análisis
└── README.md
```

---

## 2. Dataset simulado

El archivo `data/creditos_raw.csv` contiene, entre otras, columnas típicas
de una cartera de créditos de consumo:

- `id_cliente`: identificador del cliente.
- `monto`: monto del crédito.
- `plazo_meses`: plazo del crédito.
- `ingreso_mensual`: ingreso mensual del cliente.
- `segmento_comercial`: segmento (por ejemplo, Tradicional / Preferente).
- `atraso_maximo_dias`: máximo atraso histórico en días.
- `mora_30d`, `mora_60d`, `mora_90d`: banderas de mora por tramo de días (si están presentes).
- `score_buro`: score de buró de crédito (ejemplo, escala 300–900).

Los datos son **simulados**, pero respetan patrones realistas: distintos
niveles de ingreso, montos variados, clientes con y sin historial de mora,
y scores de buró heterogéneos.

---

## 3. Lógica de negocio: score de riesgo

En el notebook `notebooks/p05_riesgo_creditos.ipynb` se construye un
**score_total** a partir de cuatro componentes:

### 3.1 Score por mora (`score_mora`)

Se utiliza `atraso_maximo_dias` (o, si no existe, las banderas de mora):

```text
≥ 90 días        → 5 puntos
60 a 89 días     → 4 puntos
30 a 59 días     → 3 puntos
1 a 29 días      → 2 puntos
0 días           → 0 puntos
```

### 3.2 Score por ratio monto / ingreso (`score_ratio`)

Se calcula `ratio_monto_ingreso = monto / ingreso_mensual` y se asigna:

```text
≥ 0.60           → 3 puntos
0.40 a 0.59      → 2 puntos
0.20 a 0.39      → 1 punto
< 0.20           → 0 puntos
```

### 3.3 Score por monto absoluto (`score_monto`)

Se asigna un pequeño ajuste por el tamaño del crédito:

```text
monto ≥ 1.500.000  → 2 puntos
800.000–1.499.999  → 1 punto
< 800.000          → 0 puntos
```

(Los umbrales son ajustables según la realidad del negocio).

### 3.4 Score por buró de crédito (`score_buro_norm`)

Suponiendo que `score_buro` está en una escala aprox. 300–900:

```text
score_buro < 500   → 3 puntos    (peor buró → más riesgo)
500–649            → 2 puntos
650–749            → 1 punto
≥ 750              → 0 puntos
```

### 3.5 Score total y segmento de riesgo

El **score_total** es la suma de los cuatro componentes:

```text
score_total =
    score_mora
  + score_ratio
  + score_monto
  + score_buro_norm
```

A partir de `score_total` se define el segmento de riesgo:

```text
score_total ≥ 10   → "Alto"
score_total  7–9   → "Medio"
score_total ≤ 6    → "Bajo"
```

Estos umbrales también son ajustables según la política de riesgo de la
organización.

---

## 4. Salidas del proyecto

### 4.1 CSV segmentado

El archivo:

```text
data/creditos_riesgo_segmentado.csv
```

contiene todas las columnas originales del dataset, más:

- `ratio_monto_ingreso`
- `score_mora`
- `score_ratio`
- `score_monto`
- `score_buro_norm`
- `score_total`
- `segmento_riesgo`  (`Bajo`, `Medio`, `Alto`)

Este archivo está listo para:

- ser analizado en Excel,
- consumido por Power BI / Tableau,
- o integrado en un flujo de originación / cobranza.

### 4.2 Resumen por segmento

En el notebook se revisa la distribución de clientes por segmento:

- cantidad de créditos por `segmento_riesgo`,
- y, opcionalmente, métricas de `monto` por segmento
  (`count`, `mean`, `sum`).

Esto permite dimensionar cuánta exposición hay en cada nivel de riesgo.

### 4.3 Visualización: créditos por segmento de riesgo

Se genera la imagen:

```text
img/creditos_por_segmento_riesgo.png
```

que muestra un gráfico de barras con la cantidad de créditos en cada
segmento (`Bajo`, `Medio`, `Alto`).

Esta visualización es el típico gráfico que se llevaría a un comité de
riesgo o de negocio para discutir distribución de la cartera.

---

## 5. Cómo ejecutar el proyecto

1. Activar el entorno virtual (desde la raíz del repositorio general):

   ```bash
   cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
   source .venv/bin/activate
   ```

2. Entrar en la carpeta del proyecto P05:

   ```bash
   cd p05_creditos_riesgo
   ```

3. Abrir el notebook en VS Code o Jupyter:

   - `notebooks/p05_riesgo_creditos.ipynb`

4. Ejecutar todas las celdas en orden.  
   Al finalizar, deberías tener:

   - `data/creditos_riesgo_segmentado.csv` generado/actualizado.
   - `img/creditos_por_segmento_riesgo.png` creado.

---

## 6. Cómo interpretar los resultados

Este proyecto muestra cómo, con reglas claras y trazables:

- se puede construir un **score de riesgo simple pero útil** para priorizar
  análisis, controles o acciones de cobranza;
- se identifican clientes y créditos con **mayor riesgo** (por historial de mora,
  carga financiera y buró);
- y se genera un artefacto (`creditos_riesgo_segmentado.csv`) listo para
  integrarse en reportes y tableros ejecutivos.

La lógica es completamente **explicable y auditable**, lo que facilita su
discusión con equipos de Riesgo, Comercial y Data Analytics, y puede servir
como base para evolucionar a modelos más avanzados (por ejemplo, modelos
estadísticos o de machine learning).