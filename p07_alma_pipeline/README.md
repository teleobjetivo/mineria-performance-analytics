# P07 – ALMA Deep Sky Pipeline (from Chile)
**Integración de Datos ALMA para Análisis Científico**

Este proyecto implementa un pipeline completo para la exploración y análisis preliminar de datos astronómicos provenientes del observatorio ALMA, con enfoque educativo y científico. El pipeline simula una ingestión real a través de la API oficial de ALMA, con fallback automático a un dataset didáctico cuando la API no responde, garantizando usabilidad incluso en contextos de conectividad limitada.

Incluye extracción, catalogación, limpieza, visualización avanzada y una propuesta de integración educativa para cursos de *Data Science*, *Sistemas Distribuidos* y *Computación Científica*.

---

## 📡 Motivación Personal

Desarrollado desde Chile, país que alberga los cielos más limpios del planeta y la infraestructura astronómica más avanzada del hemisferio sur.  
Como astrofotógrafo (Nikon D7500 + William Optics RedCat 51 MK2.5 + ZWO ASI533MC Pro + Sky-Watcher GTi), entiendo la importancia del cielo profundo y la captura de señales reales desde el desierto de Atacama.

Este pipeline nace como puente entre mi trabajo fotográfico, el ecosistema ALMA y la formación de estudiantes que necesitan herramientas científicas accesibles.

---

## 🧭 Objetivos del Proyecto

1. **Simular una ingesta científica real desde ALMA**  
2. **Estandarizar catálogos y observaciones en un formato analítico**  
3. **Visualizar mapas, bandas y espectros básicos**  
4. **Crear una base para pipelines más complejos (ML, clasificación, detección de líneas)**  
5. **Entregar un recurso educativo robusto offline/online**

---

## 🧬 Arquitectura del Pipeline

```
fetch_alma_data.py  →  ingest.py  →  clean.py  →  plot_maps.py  →  metrics.py
```

Cada módulo cumple un rol:

- **fetch_alma_data.py**  
  Intenta descargar observaciones de ALMA vía API pública.  
  Si falla → genera un dataset pequeño, limpio y reproducible.

- **ingest.py**  
  Prepara las columnas y el formato unificado.

- **clean.py**  
  Aplica filtros de calidad y normalización de valores astrofísicos.

- **plot_maps.py**  
  Produce gráficos de distribución, intensidad y exploración básica del cielo profundo.

- **metrics.py**  
  Genera métricas resumidas del catálogo observado.

---

## 📁 Estructura del proyecto

```
p07_alma_pipeline/
│── data/
│     ├── alma_sample.csv
│── plots/
│── p07_alma_pipeline/
│     ├── fetch_alma_data.py
│     ├── ingest.py
│     ├── clean.py
│     ├── plot_maps.py
│     ├── metrics.py
│── README.md
```

---

## ▶️ Ejecución rápida (5 minutos)

```bash
cd p07_alma_pipeline
python p07_alma_pipeline/fetch_alma_data.py
python p07_alma_pipeline/ingest.py
python p07_alma_pipeline/clean.py
python p07_alma_pipeline/plot_maps.py
python p07_alma_pipeline/metrics.py
```

---

## 🌌 Resultados esperados

- Catálogo estandarizado de observaciones ALMA  
- Gráficos reproductibles  
- Métricas para análisis científico  
- Pipeline listo para agregar:  
  ✓ Machine Learning  
  ✓ Integración con FITS  
  ✓ Mapas avanzados con CARTA y APLpy  

---

## 👤 About Me — Hugo Baghetti Calderón

Ingeniero en Informática y Magíster en Gestión TI, con más de 15 años liderando proyectos de tecnología, analítica y transformación digital.  
Mi trabajo combina estrategia, ciencia de datos y operación real; integro visión ejecutiva con ejecución técnica rigurosa.

Exploro, investigo y construyo soluciones.  
Creo en la elegancia de los sistemas simples que funcionan, en el uso inteligente de la información y en la narrativa visual como herramienta científica.

---

## 🔗 Contacto Profesional

- 📧 **Email:** teleobjetivo.boutique@gmail.com  
- 🌐 **Sitio Web:** https://www.teleobjetivo.cl  
- 📸 **Instagram:** https://www.instagram.com/tele.objetivo  
- 💻 **GitHub (Portafolio):** https://github.com/teleobjetivo/analytics-tech-portfolio  

---

## 📄 Licencia

MIT License — libre uso educativo y profesional.

