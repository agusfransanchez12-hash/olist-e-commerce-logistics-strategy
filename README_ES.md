Markdown
# 📦 Olist E-Commerce: Estrategia Logística y de Crecimiento de Ingresos
> **Proyecto de Análisis de Negocio End-to-End (SQL, Python, Power BI y Presentación Ejecutiva)**  
> 📌 *Read this in English / Leer esto en Inglés: [README.md](./README.md)*

---

## Resumen Ejecutivo
Este proyecto analiza el **dataset público de E-Commerce de Olist en Brasil** para identificar cuellos de botella logísticos, cuantificar la exposición financiera por retrasos en los SLAs y proponer una estrategia accionable para optimizar los ingresos y la satisfacción del cliente.

* **Impacto Financiero:** **$1.07M de GMV en riesgo** debido a pedidos demorados (~8.1% del GMV total de la plataforma).
* **Satisfacción del Cliente:** Los retrasos logísticos provocan una **caída en la calificación de 4.21★ a 2.55★**, multiplicando las reseñas de 1 estrella por **5.8x**.
* **Sobrecostos Operativos:** Los tickets de soporte tipo WISMO (*"Where Is My Order?"*) se triplican o quintuplican.

---

## 📊 Principales Hallazgos e Insights Visuales

### 1. Impacto Financiero y Caída de SLAs
Los retrasos logísticos dañan directamente la retención de clientes y la reputación de la marca.
![Impacto Financiero](./presentation/slide7.jpg)

### 2. Cuellos de Botella Geográficos
Los estados con mayores demoras (**AL, MA, SE**) superan el **20% de tasa de retraso**, siendo los principales puntos de fricción operativa.
![Cuellos de Botella Geográficos](./presentation/slide6.jpg)

---

## 🎯 Recomendaciones Estratégicas y ROI Esperado

1. **Pilar 1 | Logística (Alianzas con 3PL Regionales):** Asociarse con transportistas locales en estados críticos (**AL, MA, SE**) para reducir tiempos de tránsito en un **15%–20%**.  
   * **ROI Esperado:** Protege **+$250K+ de GMV regional**.

2. **Pilar 2 | Operaciones (Scorecards y Penalizaciones a Vendedores):** Implementar tableros de control automatizados para sancionar a vendedores con despachos crónicamente tardíos.  
   * **ROI Esperado:** Reduce los tickets WISMO en un **30%** y restaura la calificación promedio a **>4.0★**.

3. **Pilar 3 | Experiencia de Cliente (Estimaciones Dinámicas en Checkout):** Calcular fechas de entrega en el checkout dinámicamente según el rendimiento regional en tiempo real.  
   * **ROI Esperado:** Evita reseñas de **1 estrella** causadas por promesas de entrega no realistas.

---

## 🛠️ Tecnologías Utilizadas
* **SQL:** Extracción de datos, unión de esquemas relacionales y agregación de métricas.
* **Python (Pandas / Matplotlib / Seaborn):** Limpieza de datos, cálculo de SLAs y análisis de distribuciones.
* **Power BI y PowerPoint:** Narrativa visual y tableros ejecutivos.

---
```text
## 📂 Estructura del Repositorio
├── data/                  # Datasets o esquemas
├── notebooks/             # Notebooks de Python (EDA, Limpieza)
├── sql/                   # Consultas SQL
├── presentation/          # Diapositivas y PDFs (EN y ES)
├── README.md              # Versión en Inglés
└── README_ES.md           # Versión en Español
```

---
👤 **Autor:** Agustín F. Sánchez | *Data & Business Analyst*
