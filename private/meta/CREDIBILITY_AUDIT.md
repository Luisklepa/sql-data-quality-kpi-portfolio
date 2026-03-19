# Auditoría de credibilidad — LIMITLESS

Checklist aplicado a todos los entregables para no inflar ni contradecir el perfil.

---

## Reglas aplicadas

- [x] **Posicionamiento:** Technical Data Analyst / BI Analyst; no Data Scientist ni Senior.
- [x] **Stack declarado:** SQL, Power BI, DAX, Excel, Power Query, Python (automatización/prep), calidad de datos, reporting, KPIs.
- [x] **No claim:** No se afirma experiencia con Oracle, SSIS, ADF, Qlik, Tableau, Snowflake, dbt, Airflow, Kafka, Spark, Databricks.
- [x] **Formación:** No se reescribe el título a Business Administration ni Industrial Engineering.
- [x] **Power BI forecasting:** No se presenta como "machine learning avanzado".
- [x] **Consistencia:** Mismo mensaje en README raíz, STRATEGY, cada proyecto e INTERVIEW_DEFENSE.

---

## Por proyecto

| Proyecto | ¿Verdad? | ¿Defendible? | ¿Refuerza BI/Data Analyst? |
|----------|----------|----------------|-----------------------------|
| 01 SQL Lab | Sí: ejercicios y soluciones reales, schema estándar. | Sí: se puede ejecutar y explicar cada consulta. | Sí: modelo dimensional, KPIs, negocio retail. |
| 02 Data Quality | Sí: dataset sucio + limpio, detección, resumen y salida corregida con impacto en negocio. | Sí: lógica documentada, corrección reproducible. | Sí: reporting fiable, validación, KPIs. |
| 03 Tailoring | Sí: sugerencias basadas en perfil y no-claim. | Sí: no inventa herramientas. | Sí: mejora fit (herramienta privada). |
| 04 API Pipeline | Sí: API retail (Fake Store), productos/usuarios/carritos → modelo dimensional y CSV/SQLite para BI. | Sí: se admite demo, no producción. | Sí: datos → modelo analítico → reporting/KPIs. |
| 05 Mock Interview | Sí: preguntas y esqueletos alineados al perfil. | Sí: advierte sobre no claim. | Sí: preparación para rol analista. |

---

## Uso en CV / entrevistas

- **En el CV:** Enlazar el repo o nombrar "Portfolio: SQL exercises, data quality checks, ETL pipeline, interview prep tools".
- **En entrevista:** Explicar cada proyecto en 1–2 frases con enfoque negocio (KPIs, reporting, calidad) y ser honesto sobre limitaciones (dataset pequeño, script batch, sin producción).
- **Si preguntan por herramientas no usadas:** No afirmar; mencionar disposición a aprender y transferibilidad de conceptos.

Última revisión: coherente con perfil y no-claim-list en _shared/config.
