# LIMITLESS — Estrategia unificada del ecosistema de empleabilidad

**Candidato:** Luis Eduardo Klepatzky Portocarrero  
**Posicionamiento:** Technical Data Analyst / BI Analyst  
**Objetivo:** Aumentar probabilidad de entrevista, tasa de pase técnico y potencial salarial.

---

## 1. Estrategia de repositorio

**Un solo repositorio.** Nombre público: **BI & SQL Analytics Portfolio**. Repo GitHub: `sql-data-quality-kpi-portfolio`. Carpeta local: LIMITLESS.

- Mensaje público: SQL, KPI reporting, data quality, dimensional modeling, business interpretation.
- No son “5 herramientas genéricas”: es **un activos públicos y herramientas privadas (ver bullet anterior)** con activos públicos y herramientas de apoyo privadas.

**Estructura:**

```
LIMITLESS/
├── README.md                 # Ecosistema creíble y orientado a empleabilidad
├── STRATEGY.md               # Este documento
├── CREDIBILITY_AUDIT.md
├── _shared/
│   ├── config/
│   ├── data/
│   └── docs/
├── 01-sql-interview-lab/      # [PUBLIC] Portfolio
├── 02-data-quality-kpi-pack/ # [PUBLIC] Portfolio
├── 03-jd-cv-tailoring/       # [PRIVATE] Employability tool
├── 04-api-sql-bi-pipeline/   # [PUBLIC] Portfolio
└── 05-mock-interview-generator/ # [PRIVATE] Employability tool
```

---

## 2. Prioridad: activos públicos vs herramientas privadas

### Activos públicos (portfolio principal)

El mensaje público debe reforzar **BI / Technical Data Analyst**: SQL, lógica de KPIs, reporting, calidad de datos, pensamiento dimensional, automatización e interpretación de negocio.

| Asset | Rol | Mensaje que refuerza |
|-------|-----|----------------------|
| **01 SQL Interview Lab** | Demostración de nivel SQL y modelado | Razonamiento SQL, KPIs, interpretación de negocio sobre datos retail. |
| **02 Data Quality + KPI Pack** | Demostración de rigor en datos | Validación, reconciliación, reporting fiable, impacto en negocio. |
| **04 API → SQL → BI Pipeline** | Demostración de flujo datos → BI | Ingestión, transformación y salida lista para reporting/KPIs (retail/transacciones). |

**Criterios para públicos:** Abrir con problema de negocio; enfoque técnico después; salidas claras; notas de defensa en entrevista; limitaciones honestas. Lenguaje recruiter-friendly y orientado a negocio.

### Herramientas privadas (empleabilidad)

Apoyan la búsqueda de empleo pero no son el foco del portfolio público. No se promocionan como “proyectos de portfolio” en CV o LinkedIn.

| Asset | Rol | Uso |
|-------|-----|-----|
| **03 JD/CV Tailoring** | Adaptar aplicaciones al JD | Uso interno; mejora fit sin inventar experiencia. |
| **05 Mock Interview Generator** | Preparar entrevistas | Uso interno; consistencia en respuestas y defensa. |

**Criterios para privados:** Funcionales, alineados al perfil y no-claim-list; documentación suficiente para ejecutar y mantener. No es necesario que sigan el estándar “business problem first” en el README raíz (sí en STRATEGY y en su propia carpeta si se comparten).

---

## 3. Componentes compartidos

| Componente | Uso | Formato |
|------------|-----|---------|
| Posicionamiento y reglas | 03, 05 | `_shared/config/profile.yaml` + `no-claim-list.txt` |
| Schema retail / KPIs | 01, 02, 04 | `_shared/data/schema.sql` + datos CSV/SQLite |
| Convenciones de docs | Todos | `_shared/docs/`; públicos: business-first |
| Utilidades Python | 02, 03, 04, 05 | `_shared/utils/` |

---

## 4. Criterios de aceptación por asset

### 01 SQL Interview Lab [PUBLIC]

- **Negocio:** Problema de negocio (retail, KPIs, decisiones) explicado primero.
- **Contenido:** Al menos 20 ejercicios organizados por nivel (core, intermediate, advanced); JOINs, agregaciones, CTEs, lógica de validación, window functions.
- **Cierre:** Mini-caso final con interpretación de negocio.
- **Salidas:** Schema, dataset realista, soluciones comentadas, interpretación.
- **Defensa:** 5 preguntas + 5 respuestas + 3 insights + 3 limitaciones.
- **Identidad:** Refuerza SQL, modelado dimensional y razonamiento analítico para BI.

### 02 Data Quality + KPI Pack [PUBLIC]

- **Negocio:** Por qué importa la calidad de datos y la reconciliación para el reporting y las decisiones.
- **Realismo:** Dataset limpio y dataset sucio; problemas intencionados: nulos, duplicados, valores fuera de rango, desajustes de reconciliación.
- **Flujo:** Detección → resumen → salida corregida; explicación del impacto en negocio.
- **Salidas:** Reporte de issues, resumen ejecutivo, dataset corregido (o reglas de corrección).
- **Defensa y limitaciones:** Incluidas y honestas.
- **Identidad:** Refuerza reporting fiable, validación y KPIs.

### 03 JD/CV Tailoring [PRIVATE]

- **Funcional:** Parsea JD; extrae keywords; gap vs perfil; sugiere headline, summary, bullets; “why I fit”; advierte sobre no-claim.
- **Consistencia:** No inventa experiencia; usa solo profile.yaml y no-claim-list.
- **Uso:** Documentación suficiente para ejecutar localmente.

### 04 API → SQL → BI Pipeline [PUBLIC]

- **Negocio:** Caso de uso alineado a retail, transacciones, pedidos, clientes o KPIs; mensaje final = soporte a posicionamiento BI, no ETL genérico.
- **Datos:** Fuente pública (API o dataset estático) con dominio retail/analytics; JSONPlaceholder solo como scaffolding temporal si hace falta.
- **Flujo:** Extracción → transformación → carga en tablas listas para SQL/BI; documentación clara.
- **Salidas:** Schema documentado; CSV o SQLite listo para Power BI o reporting.
- **Defensa y limitaciones:** Incluidas.
- **Identidad:** Refuerza “datos → modelo analítico → reporting/KPIs”.

### 05 Mock Interview Generator [PRIVATE]

- **Funcional:** Genera preguntas (reclutador + técnicas), esqueletos de respuesta, follow-ups, advertencias de respuestas débiles; usa perfil y no-claim.
- **Consistencia:** Respuestas alineadas al perfil real.
- **Uso:** Documentación suficiente para ejecutar.

---

## 5. Estándar de documentación (activos públicos)

Para **01, 02 y 04**:

1. **Problema de negocio** — Qué decisión o problema se aborda; por qué importan los datos/KPIs.
2. **Enfoque técnico** — Cómo se resuelve (schema, validaciones, pipeline); herramientas usadas.
3. **Salidas** — Qué se obtiene (archivos, reportes, datasets corregidos) y cómo se usan.
4. **Defensa en entrevista** — Enlace o resumen de preguntas, respuestas e insights.
5. **Limitaciones** — Qué no se afirma; alcance real del proyecto.

Lenguaje: orientado a negocio y reclutador; evitar jerga genérica de “dev”. Python como apoyo, no como identidad principal.

---

## 6. Reglas de credibilidad

Antes de cerrar cada deliverable:

- [ ] ¿Es verdad y defendible en entrevista?
- [ ] ¿Refuerza Technical Data Analyst / BI (SQL, Power BI, Excel, KPIs, calidad, reporting)?
- [ ] ¿Evita herramientas no usadas y claims exagerados?

Si no cumple, se reformula o se elimina.

---

## 7. Scope freeze

Do not add new modules or features unless they materially improve **interview probability** or **technical pass rate**. Prefer **polish** over expansion: tighter language, clearer pitches, consistent positioning. Public-facing content must reinforce SQL, KPI reporting, data quality, dimensional thinking, automation, and business interpretation. Python remains supporting value, not the headline.
