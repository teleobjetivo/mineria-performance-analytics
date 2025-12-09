# P06 – Score de calidad de noche para cielo profundo

## 1. Contexto

Este mini–proyecto simula el problema real de **elegir las mejores noches para observación de cielo profundo**, combinando varias variables atmosféricas y de contaminación lumínica en un **score único de calidad de noche**.

Aunque está orientado a astrofotografía, la lógica es exactamente la misma que en un rol de *Performance & Analytics*:

- Partir de **múltiples señales** (seeing, nubes, humedad, fase lunar, oscuridad del cielo).
- Normalizarlas a una escala comparable.
- Definir un **modelo simple y explicable** para priorizar oportunidades (en este caso, las mejores noches).

## 2. Objetivo del proyecto

Construir un **score de 0 a 100** que mida la calidad de una noche para observar y fotografiar objetos de cielo profundo, a partir de:

- Oscuridad del cielo (SQM).
- Seeing atmosférico (arcsec).
- Porcentaje de nubes.
- Humedad relativa.
- Fase lunar.

El resultado final permite:

- Listar las **mejores noches** ordenadas por potencial de observación.
- Visualizar de forma rápida el ranking mediante un gráfico de barras.
- Dejar trazado un enfoque reproducible y fácil de explicar en entrevistas técnicas.

## 3. Datos de entrada

Archivo: `data/condiciones_cielo.csv`

Columnas principales (simuladas con valores realistas):

-----------------------------------------------------------------------------------------------------------------
| Columna               | Tipo      | Descripción                                                               |
|-----------------------|-----------|---------------------------------------------------------------------------|
| `fecha`               | string    | Fecha de la medición (YYYY-MM-DD).                                        |
| `ubicacion`           | string    | Sitio de observación (ej. “Valle del Elqui”, “Santiago”).                 |
| `sqm_mag`             | float     | Brillo del cielo en mag/arcsec² (mayor valor = cielo más oscuro).         |
| `seeing_arcsec`       | float     | Seeing atmosférico en arcsec (menor valor = estrellas más puntuales).     |
| `nubes_pct`           | float     | Porcentaje de nubosidad (0–100).                                          |
| `humedad_pct`         | float     | Porcentaje de humedad relativa (0–100).                                   |
| `fase_lunar_pct`      | float     | Porcentaje de fase lunar (0 = Luna nueva, 100 = Luna llena).              |
| `apto_cielo_profundo` | bool/int  | Etiqueta orientativa (1 = noche razonable para cielo profundo, 0 = no).   |
-----------------------------------------------------------------------------------------------------------------

> Nota: Los datos son **sintéticos**, pero con rangos y combinaciones coherentes con condiciones típicas de observación en Chile.

## 4. Lógica del score de calidad

En el notebook `notebooks/p06_analisis_cielo_profundo.ipynb` se construye una métrica `score_calidad_noche` en escala 0–100 combinando cinco factores:

1. **Oscuridad del cielo (`sqm_mag`)**  
   - Rango típico acotado: 18 a 21.8 mag/arcsec².  
   - Cuanto más alto el SQM, más oscuro el cielo.  
   - Se normaliza a \[0, 1\] con:
     - 18 → 0 (cielo muy contaminado).
     - 21.8 → 1 (cielo muy oscuro).

2. **Seeing (`seeing_arcsec`)**  
   - Rango acotado: 0.7 a 3.0 arcsec.
   - Menor valor = mejor estabilidad atmosférica.
   - Se transforma a \[0, 1\] donde 0.7 arcsec ≈ 1 (mejor) y 3.0 arcsec ≈ 0 (peor).

3. **Nubes (`nubes_pct`)**  
   - 0% nubes = 1 (óptimo).  
   - 100% nubes = 0 (inútil para cielo profundo).

4. **Humedad (`humedad_pct`)**  
   - 0% humedad = 1 (ideal).  
   - 100% humedad = 0 (muy mala para transparencia y rocío).

5. **Fase lunar (`fase_lunar_pct`)**  
   - 0% (Luna nueva) = 1.  
   - 100% (Luna llena) = 0.  
   - Especialmente importante para objetos de bajo contraste (nebulosas, galaxias).

Estos factores se combinan en un score ponderado:

- 0.30 · oscuridad del cielo (SQM)  
- 0.25 · seeing  
- 0.20 · nubes  
- 0.15 · fase lunar  
- 0.10 · humedad  

Por último, el score se escala a 0–100 y se redondea a un decimal:

```python
df2["score_calidad_noche"] = (score * 100).round(1).clip(0, 100)
```

El resultado es una nueva columna que permite ordenar todas las noches de mejor a peor calidad para cielo profundo.

## 5. Salidas principales

1. **Dataset enriquecido en memoria**  
   - `df2` contiene la columna adicional `score_calidad_noche`.

2. **Top de noches recomendadas**  
   - Se construye una tabla con las mejores noches según el score:

   ```python
   TOP_N = 10
   top_n = (
       df2
       .sort_values("score_calidad_noche", ascending=False)
       .head(TOP_N)
       .reset_index(drop=True)
   )
   ```

   Esta tabla incluye:
   - fecha,
   - ubicación,
   - sqm_mag,
   - seeing_arcsec,
   - nubes_pct,
   - humedad_pct,
   - fase_lunar_pct,
   - score_calidad_noche.

3. **Gráfico de ranking de noches**  
   - Se genera y guarda un gráfico de barras en:

     ```text
     img/score_calidad_noche_top.png
     ```

   - El gráfico muestra, en el eje X, `fecha – ubicación`, y en el eje Y el `score_calidad_noche` (0–100).
   - Sirve como **visualización rápida** para explicar cómo se priorizan las noches “estrella”.

## 6. Cómo ejecutar el proyecto localmente

Desde la raíz del repositorio (por ejemplo `Proyecto Mineria`):

1. Activar el entorno virtual (si no está activo):

   ```bash
   cd "/Users/hugobaghetti/Desktop/PROYECTOS/Proyecto Mineria"
   source .venv/bin/activate
   ```

2. Abrir el notebook de P06:

   - En VS Code, abrir la carpeta del proyecto.
   - Ir a: `p06_cielo_profundo/notebooks/p06_analisis_cielo_profundo.ipynb`.
   - Seleccionar el kernel asociado al entorno `.venv`.

3. Ejecutar todas las celdas del notebook.

Al finalizar, deberías ver:

- La tabla con las mejores noches (`top_n`).
- El gráfico de barras guardado en `p06_cielo_profundo/img/score_calidad_noche_top.png`.

## 7. Cómo explicar este proyecto en una entrevista

Algunas frases que se pueden usar para presentar P06 en contexto profesional:

- “Construí un score de calidad de noche combinando cinco variables físicas (oscuridad, seeing, nubes, humedad y fase lunar), normalizadas y ponderadas en una escala de 0 a 100.”
- “El objetivo es priorizar las mejores noches para observación de cielo profundo, pero el enfoque es exactamente el mismo que usaría para priorizar activos, riesgos o iniciativas de mantenimiento.”
- “El modelo es deliberadamente simple y explicable: se puede ajustar el peso de cada factor según el criterio del negocio o de los expertos.”
- “Dejo trazado un flujo reproducible en Python: lectura del dataset, normalización de variables, cálculo de score y visualización final para soporte de decisiones.”

## 8. Posibles extensiones futuras

Algunas mejoras que se podrían implementar sobre esta base para las proximas versiones:

- Ajustar automáticamente los pesos del score usando feedback histórico (noches ‘buenas’ reales).  
- Incorporar restricciones logísticas (distancia al sitio, disponibilidad de equipo, etc.).  
- Integrar datos reales de estaciones meteorológicas o APIs astronómicas para automatizar la generación del ranking de noches.

---


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

