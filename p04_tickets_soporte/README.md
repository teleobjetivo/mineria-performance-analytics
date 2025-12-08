# P04 – Prioridad de tickets de soporte TI

Este proyecto simula una **mesa de ayuda de TI** (tipo Jira / Service Desk) y construye un
**score de prioridad** para apoyar la decisión de “qué ticket atender primero”.

La idea es mostrar, de forma simple y transparente, cómo a partir de datos operacionales
(tickets, fechas, SLA) se puede construir una lógica de priorización clara, explicable y
reproducible.

---

## 1. Estructura del proyecto

```text
p04_tickets_soporte/
├── data/
│   ├── tickets_soporte_raw.csv        # datos simulados de tickets
│   └── tickets_priorizados.csv        # salida con score y orden de prioridad
├── img/
│   └── score_promedio_por_categoria.png
├── notebooks/
│   └── p04_priorizacion_tickets.ipynb # notebook principal de análisis
└── README.md
```

---

## 2. Dataset simulado

El archivo `data/tickets_soporte_raw.csv` contiene, entre otras, las siguientes columnas:

- `ticket_id`: identificador único del ticket (ej.: `T-0001`).
- `fecha_creacion`: fecha de creación del ticket.
- `fecha_cierre`: fecha de cierre (vacío si el ticket sigue abierto).
- `categoria`: tipo de incidente (Correo, VPN, SAP, Red, etc.).
- `prioridad`: prioridad declarada (Baja, Media, Alta, Crítica).
- `estado`: estado del ticket (Abierto, En curso, Resuelto, Cerrado).
- `asignado_a`: analista responsable.
- `canal`: canal de ingreso (Portal, Correo, Teléfono).
- `sla_vencido`: indicador de si el ticket incumplió el SLA (Sí/No).

Estos datos están **simulados**, pero respetan patrones realistas de una mesa de ayuda:
distintas categorías, prioridades mezcladas, tickets abiertos/cerrados y algunos SLA
vencidos.

---

## 3. Lógica de negocio: score de prioridad

En el notebook `notebooks/p04_priorizacion_tickets.ipynb` se construye un **score_total**
para cada ticket a partir de reglas explícitas. La lógica se basa en cuatro componentes:

### 3.1 Prioridad declarada (`score_prioridad_base`)

```text
Baja    → 1 punto
Media   → 2 puntos
Alta    → 3 puntos
Crítica → 4 puntos
```

### 3.2 SLA vencido (`score_sla`)

```text
sla_vencido = "Sí" → +3 puntos
sla_vencido = "No" → +0 puntos
```

### 3.3 Días abiertos (`score_dias`)

Se calcula la cantidad de días que el ticket ha estado abierto (o demoró en cerrarse) y
se asigna un puntaje:

```text
> 10 días        → +3 puntos
6 a 10 días      → +2 puntos
3 a 5 días       → +1 punto
0 a 2 días       → +0 puntos
```

### 3.4 Estado actual (`score_estado`)

```text
estado = Abierto o En curso → +2 puntos
estado = Resuelto o Cerrado → +0 puntos
```

### 3.5 Score total

El **score_total** es la suma:

```text
score_total =
    score_prioridad_base
  + score_sla
  + score_dias
  + score_estado
```

Finalmente, los tickets se ordenan de forma descendente por `score_total` y, en caso de
empate, por `dias_abierto`.

---

## 4. Salidas del proyecto

### 4.1 CSV priorizado

El archivo:

```text
data/tickets_priorizados.csv
```

contiene todos los tickets originales más las columnas de score:

- `score_prioridad_base`
- `score_sla`
- `score_dias`
- `score_estado`
- `score_total`

Este archivo se puede:

- cargar en Excel,
- consumir desde Power BI,
- o integrar en otro flujo de priorización.

### 4.2 Top 10 de tickets críticos

En el notebook se construye un **Top 10 de tickets más críticos**, mostrando para cada uno:

- `ticket_id`
- `categoria`
- `prioridad`
- `estado`
- `sla_vencido`
- `dias_abierto`
- `score_total`

Este listado es un ejemplo directo de cómo la lógica de negocio se traduce en una **cola
de atención priorizada**.

### 4.3 Visualización: score por categoría

Se genera la imagen:

```text
img/score_promedio_por_categoria.png
```

que muestra el **score promedio de prioridad por categoría de ticket**. Esto permite
identificar categorías que, en promedio, concentran más riesgo operacional (por ejemplo,
VPN o SAP frente a incidentes menores).

---

## 5. Cómo ejecutar el proyecto

1. Activar el entorno virtual (desde la raíz del repositorio general):

   ```bash
   cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
   source .venv/bin/activate
   ```

2. Entrar en la carpeta del proyecto P04:

   ```bash
   cd p04_tickets_soporte
   ```

3. Abrir el notebook en VS Code o Jupyter:

   - `notebooks/p04_priorizacion_tickets.ipynb`

4. Ejecutar todas las celdas en orden.  
   Al finalizar, deberías tener:

   - `data/tickets_priorizados.csv` generado/actualizado.
   - `img/score_promedio_por_categoria.png` creado.

---

## 6. Cómo interpretar los resultados

Este proyecto ejemplifica cómo, a partir de datos de tickets de soporte y algunas reglas
sencillas pero claras:

- se puede **formalizar criterios de priorización** que normalmente están “en la cabeza”
  del equipo,
- se identifican tickets con **alto riesgo operacional** (SLA vencido, alta criticidad,
  muchos días abiertos),
- y se genera un artefacto (`tickets_priorizados.csv`) listo para ser integrado en la
operación diaria o en un dashboard.

La lógica es completamente **explicable y auditable**, lo que facilita su adopción en
equipos de TI y operaciones.
